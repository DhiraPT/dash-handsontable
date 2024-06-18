/**
 * Every Dash components are given these props.
 * Use with your own props:
 * ```
 * type Props = {
 *     my_prop: string;
 * } & DashComponentProps;
 * ```
 * Recommended to use `type` instead of `interface` so you can define the
 * order of props with types concatenation.
 */
export type DashComponentProps = {
    /**
     * Unique ID to identify this component in Dash callbacks.
     */
    id?: string;
    /**
     * Update props to trigger callbacks.
     */
    setProps: (props: Record<string, any>) => void;
}

/**
 * Function props for HotTable component.
 */
export type FunctionProps = {
    // Configuration Options
    cells?: string;
    isEmptyCol?: string; // Configuration options methods
    isEmptyRow?: string; // Configuration options methods
    // Hooks
    afterAddChild?: string;
    afterAutofill?: string;
    afterBeginEditing?: string;
    afterCellMetaReset?: string;
    afterChange?: string;
    afterColumnCollapse?: string;
    afterColumnExpand?: string;
    afterColumnFreeze?: string;
    afterColumnMove?: string;
    afterColumnResize?: string;
    afterColumnSequenceChange?: string;
    afterColumnSort?: string;
    afterColumnUnfreeze?: string;
    afterContextMenuDefaultOptions?: string;
    afterContextMenuHide?: string;
    afterContextMenuShow?: string;
    afterCopy?: string;
    afterCopyLimit?: string;
    afterCreateCol?: string;
    afterCreateRow?: string;
    afterCut?: string;
    afterDeselect?: string;
    afterDestroy?: string;
    afterDetachChild?: string;
    afterDocumentKeyDown?: string;
    afterDrawSelection?: string;
    afterDropdownMenuDefaultOptions?: string;
    afterDropdownMenuHide?: string;
    afterDropdownMenuShow?: string;
    afterFilter?: string;
    afterFormulasValuesUpdate?: string;
    afterGetCellMeta?: string;
    afterGetColHeader?: string;
    afterGetColumnHeaderRenderers?: string;
    afterGetRowHeader?: string;
    afterGetRowHeaderRenderers?: string;
    afterHideColumns?: string;
    afterHideRows?: string;
    afterInit?: string;
    afterLanguageChange?: string;
    afterListen?: string;
    afterLoadData?: string;
    afterMergeCells?: string;
    afterModifyTransformEnd?: string;
    afterModifyTransformFocus?: string;
    afterModifyTransformStart?: string;
    afterMomentumScroll?: string;
    afterNamedExpressionAdded?: string;
    afterNamedExpressionRemoved?: string;
    afterOnCellContextMenu?: string;
    afterOnCellCornerDblClick?: string;
    afterOnCellCornerMouseDown?: string;
    afterOnCellMouseDown?: string;
    afterOnCellMouseOut?: string;
    afterOnCellMouseOver?: string;
    afterOnCellMouseUp?: string;
    afterPaste?: string;
    afterPluginsInitialized?: string;
    afterRedo?: string;
    afterRedoStackChange?: string;
    afterRefreshDimensions?: string;
    afterRemoveCellMeta?: string;
    afterRemoveCol?: string;
    afterRemoveRow?: string;
    afterRender?: string;
    afterRenderer?: string;
    afterRowMove?: string;
    afterRowResize?: string;
    afterRowSequenceChange?: string;
    afterScroll?: string;
    afterScrollHorizontally?: string;
    afterScrollVertically?: string;
    afterSelectColumns?: string;
    afterSelection?: string;
    afterSelectionByProp?: string;
    afterSelectionEnd?: string;
    afterSelectionEndByProp?: string;
    afterSelectionFocusSet?: string;
    afterSelectRows?: string;
    afterSetCellMeta?: string;
    afterSetDataAtCell?: string;
    afterSetDataAtRowProp?: string;
    afterSetSourceDataAtCell?: string;
    afterSheetAdded?: string;
    afterSheetRemoved?: string;
    afterSheetRenamed?: string;
    afterTrimRow?: string;
    afterUndo?: string;
    afterUndoStackChange?: string;
    afterUnhideColumns?: string;
    afterUnhideRows?: string;
    afterUnlisten?: string;
    afterUnmergeCells?: string;
    afterUntrimRow?: string;
    afterUpdateData?: string;
    afterUpdateSettings?: string;
    afterValidate?: string;
    afterViewportColumnCalculatorOverride?: string;
    afterViewportRowCalculatorOverride?: string;
    afterViewRender?: string;
    beforeAddChild?: string;
    beforeAutofill?: string;
    beforeBeginEditing?: string;
    beforeCellAlignment?: string;
    beforeChange?: string;
    beforeChangeRender?: string;
    beforeColumnCollapse?: string;
    beforeColumnExpand?: string;
    beforeColumnFreeze?: string;
    beforeColumnMove?: string;
    beforeColumnResize?: string;
    beforeColumnSort?: string;
    beforeColumnUnfreeze?: string;
    beforeColumnWrap?: string;
    beforeContextMenuSetItems?: string;
    beforeContextMenuShow?: string;
    beforeCopy?: string;
    beforeCreateCol?: string;
    beforeCreateRow?: string;
    beforeCut?: string;
    beforeDetachChild?: string;
    beforeDrawBorders?: string;
    beforeDropdownMenuSetItems?: string;
    beforeDropdownMenuShow?: string;
    beforeFilter?: string;
    beforeGetCellMeta?: string;
    beforeHideColumns?: string;
    beforeHideRows?: string;
    beforeHighlightingColumnHeader?: string;
    beforeHighlightingRowHeader?: string;
    beforeInit?: string;
    beforeInitWalkontable?: string;
    beforeKeyDown?: string;
    beforeLanguageChange?: string;
    beforeLoadData?: string;
    beforeMergeCells?: string;
    beforeOnCellContextMenu?: string;
    beforeOnCellMouseDown?: string;
    beforeOnCellMouseOut?: string;
    beforeOnCellMouseOver?: string;
    beforeOnCellMouseUp?: string;
    beforePaste?: string;
    beforeRedo?: string;
    beforeRedoStackChange?: string;
    beforeRefreshDimensions?: string;
    beforeRemoveCellClassNames?: string;
    beforeRemoveCellMeta?: string;
    beforeRemoveCol?: string;
    beforeRemoveRow?: string;
    beforeRender?: string;
    beforeRenderer?: string;
    beforeRowMove?: string;
    beforeRowResize?: string;
    beforeRowWrap?: string;
    beforeSelectColumns?: string;
    beforeSelectionFocusSet?: string;
    beforeSelectionHighlightSet?: string;
    beforeSelectRows?: string;
    beforeSetCellMeta?: string;
    beforeSetRangeEnd?: string;
    beforeSetRangeStart?: string;
    beforeSetRangeStartOnly?: string;
    beforeStretchingColumnWidth?: string;
    beforeTouchScroll?: string;
    beforeTrimRow?: string;
    beforeUndo?: string;
    beforeUndoStackChange?: string;
    beforeUnhideColumns?: string;
    beforeUnhideRows?: string;
    beforeUnmergeCells?: string;
    beforeUntrimRow?: string;
    beforeUpdateData?: string;
    beforeValidate?: string;
    beforeValueRender?: string;
    beforeViewportScroll?: string;
    beforeViewportScrollHorizontally?: string;
    beforeViewportScrollVertically?: string;
    beforeViewRender?: string;
    construct?: string;
    globalBucket?: string;
    init?: string;
    modifyAutoColumnSizeSeed?: string;
    modifyAutofillRange?: string;
    modifyColHeader?: string;
    modifyColumnHeaderHeight?: string;
    modifyColumnHeaderValue?: string;
    modifyColWidth?: string;
    modifyCopyableRange?: string;
    modifyData?: string;
    modifyFiltersMultiSelectValue?: string;
    modifyFocusedElement?: string;
    modifyFocusOnTabNavigation?: string;
    modifyGetCellCoords?: string;
    modifyRowData?: string;
    modifyRowHeader?: string;
    modifyRowHeaderWidth?: string;
    modifyRowHeight?: string;
    modifySourceData?: string;
    modifyTransformEnd?: string;
    modifyTransformFocus?: string;
    modifyTransformStart?: string;
    persistentStateLoad?: string;
    persistentStateReset?: string;
    persistentStateSave?: string;
};

/**
 * List of function props keys for the HotTable component.
 */
export const FUNCTION_PROPS_KEYS: string[] = [
    // Configuration Options
    'cells',
    'isEmptyCol', // Configuration options methods
    'isEmptyRow', // Configuration options methods
    // Hooks
    'afterAddChild',
    'afterAutofill',
    'afterBeginEditing',
    'afterCellMetaReset',
    'afterChange',
    'afterColumnCollapse',
    'afterColumnExpand',
    'afterColumnFreeze',
    'afterColumnMove',
    'afterColumnResize',
    'afterColumnSequenceChange',
    'afterColumnSort',
    'afterColumnUnfreeze',
    'afterContextMenuDefaultOptions',
    'afterContextMenuHide',
    'afterContextMenuShow',
    'afterCopy',
    'afterCopyLimit',
    'afterCreateCol',
    'afterCreateRow',
    'afterCut',
    'afterDeselect',
    'afterDestroy',
    'afterDetachChild',
    'afterDocumentKeyDown',
    'afterDrawSelection',
    'afterDropdownMenuDefaultOptions',
    'afterDropdownMenuHide',
    'afterDropdownMenuShow',
    'afterFilter',
    'afterFormulasValuesUpdate',
    'afterGetCellMeta',
    'afterGetColHeader',
    'afterGetColumnHeaderRenderers',
    'afterGetRowHeader',
    'afterGetRowHeaderRenderers',
    'afterHideColumns',
    'afterHideRows',
    'afterInit',
    'afterLanguageChange',
    'afterListen',
    'afterLoadData',
    'afterMergeCells',
    'afterModifyTransformEnd',
    'afterModifyTransformFocus',
    'afterModifyTransformStart',
    'afterMomentumScroll',
    'afterNamedExpressionAdded',
    'afterNamedExpressionRemoved',
    'afterOnCellContextMenu',
    'afterOnCellCornerDblClick',
    'afterOnCellCornerMouseDown',
    'afterOnCellMouseDown',
    'afterOnCellMouseOut',
    'afterOnCellMouseOver',
    'afterOnCellMouseUp',
    'afterPaste',
    'afterPluginsInitialized',
    'afterRedo',
    'afterRedoStackChange',
    'afterRefreshDimensions',
    'afterRemoveCellMeta',
    'afterRemoveCol',
    'afterRemoveRow',
    'afterRender',
    'afterRenderer',
    'afterRowMove',
    'afterRowResize',
    'afterRowSequenceChange',
    'afterScroll',
    'afterScrollHorizontally',
    'afterScrollVertically',
    'afterSelectColumns',
    'afterSelection',
    'afterSelectionByProp',
    'afterSelectionEnd',
    'afterSelectionEndByProp',
    'afterSelectionFocusSet',
    'afterSelectRows',
    'afterSetCellMeta',
    'afterSetDataAtCell',
    'afterSetDataAtRowProp',
    'afterSetSourceDataAtCell',
    'afterSheetAdded',
    'afterSheetRemoved',
    'afterSheetRenamed',
    'afterTrimRow',
    'afterUndo',
    'afterUndoStackChange',
    'afterUnhideColumns',
    'afterUnhideRows',
    'afterUnlisten',
    'afterUnmergeCells',
    'afterUntrimRow',
    'afterUpdateData',
    'afterUpdateSettings',
    'afterValidate',
    'afterViewportColumnCalculatorOverride',
    'afterViewportRowCalculatorOverride',
    'afterViewRender',
    'beforeAddChild',
    'beforeAutofill',
    'beforeBeginEditing',
    'beforeCellAlignment',
    'beforeChange',
    'beforeChangeRender',
    'beforeColumnCollapse',
    'beforeColumnExpand',
    'beforeColumnFreeze',
    'beforeColumnMove',
    'beforeColumnResize',
    'beforeColumnSort',
    'beforeColumnUnfreeze',
    'beforeColumnWrap',
    'beforeContextMenuSetItems',
    'beforeContextMenuShow',
    'beforeCopy',
    'beforeCreateCol',
    'beforeCreateRow',
    'beforeCut',
    'beforeDetachChild',
    'beforeDrawBorders',
    'beforeDropdownMenuSetItems',
    'beforeDropdownMenuShow',
    'beforeFilter',
    'beforeGetCellMeta',
    'beforeHideColumns',
    'beforeHideRows',
    'beforeHighlightingColumnHeader',
    'beforeHighlightingRowHeader',
    'beforeInit',
    'beforeInitWalkontable',
    'beforeKeyDown',
    'beforeLanguageChange',
    'beforeLoadData',
    'beforeMergeCells',
    'beforeOnCellContextMenu',
    'beforeOnCellMouseDown',
    'beforeOnCellMouseOut',
    'beforeOnCellMouseOver',
    'beforeOnCellMouseUp',
    'beforePaste',
    'beforeRedo',
    'beforeRedoStackChange',
    'beforeRefreshDimensions',
    'beforeRemoveCellClassNames',
    'beforeRemoveCellMeta',
    'beforeRemoveCol',
    'beforeRemoveRow',
    'beforeRender',
    'beforeRenderer',
    'beforeRowMove',
    'beforeRowResize',
    'beforeRowWrap',
    'beforeSelectColumns',
    'beforeSelectionFocusSet',
    'beforeSelectionHighlightSet',
    'beforeSelectRows',
    'beforeSetCellMeta',
    'beforeSetRangeEnd',
    'beforeSetRangeStart',
    'beforeSetRangeStartOnly',
    'beforeStretchingColumnWidth',
    'beforeTouchScroll',
    'beforeTrimRow',
    'beforeUndo',
    'beforeUndoStackChange',
    'beforeUnhideColumns',
    'beforeUnhideRows',
    'beforeUnmergeCells',
    'beforeUntrimRow',
    'beforeUpdateData',
    'beforeValidate',
    'beforeValueRender',
    'beforeViewportScroll',
    'beforeViewportScrollHorizontally',
    'beforeViewportScrollVertically',
    'beforeViewRender',
    'construct',
    'globalBucket',
    'init',
    'modifyAutoColumnSizeSeed',
    'modifyAutofillRange',
    'modifyColHeader',
    'modifyColumnHeaderHeight',
    'modifyColumnHeaderValue',
    'modifyColWidth',
    'modifyCopyableRange',
    'modifyData',
    'modifyFiltersMultiSelectValue',
    'modifyFocusedElement',
    'modifyFocusOnTabNavigation',
    'modifyGetCellCoords',
    'modifyRowData',
    'modifyRowHeader',
    'modifyRowHeaderWidth',
    'modifyRowHeight',
    'modifySourceData',
    'modifyTransformEnd',
    'modifyTransformFocus',
    'modifyTransformStart',
    'persistentStateLoad',
    'persistentStateReset',
    'persistentStateSave',
];