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

    useEffect(() => {
        if (props.exportData) {
            handleExportData(props.exportDataParams);
        }
    }, [props.exportData]);

    return (
        <ReactHotTable
            ref={hotRef}
            {...restProps}
        />
    );
}

HotTable.defaultProps = {
    ...ReactHotTable.defaultProps,
    exportData: false,
    exportDataParams: {},
};

export default HotTable;
