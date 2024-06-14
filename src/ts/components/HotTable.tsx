import React, { useEffect, useRef } from 'react';
import { DashComponentProps } from '../props';
import 'handsontable/dist/handsontable.full.min.css';
import Handsontable from 'handsontable/base';
import { registerAllModules } from 'handsontable/registry';
import { HotTableProps, HotTable as ReactHotTable } from '@handsontable/react';

registerAllModules();

type Props = HotTableProps & DashComponentProps & {
    exportData: boolean;
    exportDataParams: {
        filename?: string;
    };
    getData: { row?: number, col?: number, row2?: number, col2?: number } | false;
    currentData: any[][];
    getDataAtRow: { row: number, prop?: string } | false;
    currentDataAtRow: any[];
    selectedCells: [number, number, number, number][][] | null;
};

/**
 * HotTable is a Dash component that wraps the React HotTable component.
 */
const HotTable = (props: Props) => {
    const {...restProps} = props;
    const hotRef = useRef(null);

    const handleExportData = (exportDataParams: { filename?: string }) => {
        if (hotRef.current) {
            const exportPlugin = hotRef.current.hotInstance.getPlugin('exportFile');
            if (exportDataParams.filename !== undefined) {
                const fileExtension = exportDataParams.filename.substring(exportDataParams.filename.lastIndexOf(".") + 1);
                const fileNameWithoutExtension = exportDataParams.filename.substring(0, exportDataParams.filename.lastIndexOf("."));
                exportPlugin.downloadFile(fileExtension, { filename: fileNameWithoutExtension });
            } else {
                exportPlugin.downloadFile('csv');
            }
        }
        props.setProps({
            exportData: false,
        });
    };

    const handleGetData = (row?: number, col?: number, row2?: number, col2?: number) => {
        if (hotRef.current) {
            const hotInstance = hotRef.current.hotInstance;
            const data = hotInstance.getData(row, col, row2, col2);
            props.setProps({
                currentData: data,
            });
        }
        props.setProps({
            getData: false,
        });
    }

    const handleGetDataAtRow = (row: number, prop?: string) => {
        if (hotRef.current) {
            const hotInstance = hotRef.current.hotInstance;
            const data = hotInstance.getDataAtRow(row, prop);
            props.setProps({
                currentDataAtRow: data,
            });
        }
        props.setProps({
            getDataAtRow: false,
        });
    }

    useEffect(() => {
        if (props.exportData) {
            handleExportData(props.exportDataParams);
        }
    }, [props.exportData]);

    useEffect(() => {
        if (props.getData) {
            handleGetData(props.getData.row, props.getData.col, props.getData.row2, props.getData.col2);
        }
    }, [props.getData]);

    useEffect(() => {
        if (props.getDataAtRow) {
            handleGetDataAtRow(props.getDataAtRow.row, props.getDataAtRow.prop);
        }
    }, [props.getDataAtRow]);

    const handleAfterSelection = () => {
        if (hotRef.current) {
            const hotInstance = hotRef.current.hotInstance;
            const selectedCells = hotInstance.getSelected();
            props.setProps({
                selectedCells: selectedCells,
            });
        }
    };

    return (
        <ReactHotTable
            ref={hotRef}
            afterSelection={handleAfterSelection}
            {...restProps}
        />
    );
}

HotTable.defaultProps = {
    ...ReactHotTable.defaultProps,
    exportData: false,
    exportDataParams: {},
    getData: false,
    currentData: [],
    getDataAtRow: false,
    currentDataAtRow: [],
    selectedCells: null,
};

export default HotTable;
