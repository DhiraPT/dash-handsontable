import React, { useEffect, useRef } from 'react';
import { DashComponentProps, FunctionProps, FUNCTION_PROPS_KEYS } from '../props';
import 'handsontable/dist/handsontable.full.min.css';
import Handsontable from 'handsontable/base';
import { registerAllModules } from 'handsontable/registry';
import { HotTableProps, HotTable as ReactHotTable } from '@handsontable/react';
import { ExportFile, ExportOptions } from 'handsontable/plugins/exportFile';

registerAllModules();

type Props = Omit<HotTableProps, keyof FunctionProps> & {
    exportData: boolean;
    exportDataParams: ExportOptions;
} & FunctionProps & DashComponentProps;

/**
 * HotTable is a Dash component that wraps the React HotTable component.
 */
const HotTable = (props: Props) => {
    const hotRef = useRef(null);
    const currentProps = useRef({'lisenceKey': props.licenseKey});

    const handleExportData = (exportDataParams: ExportOptions) => {
        if (hotRef.current) {
            const exportPlugin = hotRef.current.hotInstance.getPlugin('exportFile');
            if (exportDataParams.filename !== undefined) {
                const fileExtension = exportDataParams.filename.substring(exportDataParams.filename.lastIndexOf(".") + 1);
                const fileNameWithoutExtension = exportDataParams.filename.substring(0, exportDataParams.filename.lastIndexOf("."));
                exportPlugin.downloadFile(fileExtension, { ...exportDataParams, filename: fileNameWithoutExtension });
            } else {
                exportPlugin.downloadFile('csv', exportDataParams);
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

    useEffect(() => {
        if (!hotRef.current) {
            return;
        }

        const updatedSettings = {};

        Object.entries(props).forEach(([key, value]) => {
            if (value && currentProps.current[key] !== value) {
                if (FUNCTION_PROPS_KEYS.includes(key)) {
                    updatedSettings[key] = new Function('return ' + value)();
                } else {
                    updatedSettings[key] = value;
                }
                currentProps.current[key] = value;
            }
        });

        if (Object.keys(updatedSettings).length > 0) {
            hotRef.current.hotInstance.updateSettings(updatedSettings);
        }
    }, [props]);


    return (
        <ReactHotTable
            ref={hotRef}
            licenseKey={props.licenseKey}
        />
    );
}

HotTable.defaultProps = {
    ...ReactHotTable.defaultProps,
    exportData: false,
    exportDataParams: {},
};

export default HotTable;
