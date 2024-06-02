# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HotTable(Component):
    """A HotTable component.
HotTable is a Dash component that wraps the React HotTable component.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- activeHeaderClassName (string; optional)

- allowEmpty (boolean; optional)

- allowHtml (boolean; optional)

- allowInsertColumn (boolean; optional)

- allowInsertRow (boolean; optional)

- allowInvalid (boolean; optional)

- allowRemoveColumn (boolean; optional)

- allowRemoveRow (boolean; optional)

- ariaTags (boolean; optional)

- autoColumnSize (boolean | number | string | dict | list; optional)

- autoRowSize (boolean | number | string | dict | list; optional)

- autoWrapCol (boolean; optional)

- autoWrapRow (boolean; optional)

- bindRowsWithHeaders (boolean | number | string | dict | list; optional)

- cell (list of dicts with strings as keys and values of type boolean | number | string | dict | list; optional)

- checkedTemplate (string | number; optional)

- className (string; optional)

- colHeaders (list of strings; optional)

- colWidths (string | number | list of strings | list of numbers; optional)

- collapsibleColumns (boolean | number | string | dict | list; optional)

- columnHeaderHeight (number | list of numbers; optional)

- columnSorting (boolean | number | string | dict | list; optional)

- columnSummary (optional)

- columns (optional)

- commentedCellClassName (string; optional)

- comments (boolean | number | string | dict | list; optional)

- contextMenu (boolean | number | string | dict | list; optional)

- copyPaste (boolean | number | string | dict | list; optional)

- copyable (boolean; optional)

- correctFormat (boolean; optional)

- currentColClassName (string; optional)

- currentHeaderClassName (string; optional)

- currentRowClassName (string; optional)

- customBorders (boolean | number | string | dict | list; optional)

- data (list of list of boolean | number | string | dict | listss; optional)

- dataSchema (list of boolean | number | string | dict | lists; optional)

- dateFormat (string; optional)

- datePickerConfig (dict; optional)

    `datePickerConfig` is a dict with keys:

    - ariaLabel (string; optional):
        Data-attribute on the input field with an aria assistance test
        (only applied when bound is set).

    - blurFieldOnSelect (boolean; optional):
        Defines if the field is blurred when a date is selected
        (default True).

    - bound (boolean; optional):
        Automatically show/hide the datepicker on field focus.
        Default: True if field is set.

    - container (dict; optional):
        DOM node to render calendar into, see container example.
        Default: undefined.

        `container` is a dict with keys:

        - ATTRIBUTE_NODE (number; required)

        - CDATA_SECTION_NODE (number; required):
            node is a CDATASection node.

        - COMMENT_NODE (number; required):
            node is a Comment node.

        - DOCUMENT_FRAGMENT_NODE (number; required):
            node is a DocumentFragment node.

        - DOCUMENT_NODE (number; required):
            node is a document.

        - DOCUMENT_POSITION_CONTAINED_BY (number; required):
            Set when other is a descendant of node.

        - DOCUMENT_POSITION_CONTAINS (number; required):
            Set when other is an ancestor of node.

        - DOCUMENT_POSITION_DISCONNECTED (number; required):
            Set when node and other are not in the same tree.

        - DOCUMENT_POSITION_FOLLOWING (number; required):
            Set when other is following node.

        - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

        - DOCUMENT_POSITION_PRECEDING (number; required):
            Set when other is preceding node.

        - DOCUMENT_TYPE_NODE (number; required):
            node is a doctype.

        - ELEMENT_NODE (number; required):
            node is an element.

        - ENTITY_NODE (number; required)

        - ENTITY_REFERENCE_NODE (number; required)

        - NOTATION_NODE (number; required)

        - PROCESSING_INSTRUCTION_NODE (number; required):
            node is a ProcessingInstruction node.

        - TEXT_NODE (number; required):
            node is a Text node.

        - accessKey (string; required)

        - accessKeyLabel (string; required)

        - addEventListener (required)

        - after (required):
            Inserts nodes just after node, while replacing strings in
            nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - animate (required)

        - append (required):
            Inserts nodes after the last child of node, while
            replacing strings in nodes with equivalent Text nodes.
            Throws a \"HierarchyRequestError\" DOMException if the
            constraints of the node tree are violated.

        - appendChild (required)

        - ariaAtomic (string; required)

        - ariaAutoComplete (string; required)

        - ariaBusy (string; required)

        - ariaChecked (string; required)

        - ariaColCount (string; required)

        - ariaColIndex (string; required)

        - ariaColIndexText (string; required)

        - ariaColSpan (string; required)

        - ariaCurrent (string; required)

        - ariaDisabled (string; required)

        - ariaExpanded (string; required)

        - ariaHasPopup (string; required)

        - ariaHidden (string; required)

        - ariaInvalid (string; required)

        - ariaKeyShortcuts (string; required)

        - ariaLabel (string; required)

        - ariaLevel (string; required)

        - ariaLive (string; required)

        - ariaModal (string; required)

        - ariaMultiLine (string; required)

        - ariaMultiSelectable (string; required)

        - ariaOrientation (string; required)

        - ariaPlaceholder (string; required)

        - ariaPosInSet (string; required)

        - ariaPressed (string; required)

        - ariaReadOnly (string; required)

        - ariaRequired (string; required)

        - ariaRoleDescription (string; required)

        - ariaRowCount (string; required)

        - ariaRowIndex (string; required)

        - ariaRowIndexText (string; required)

        - ariaRowSpan (string; required)

        - ariaSelected (string; required)

        - ariaSetSize (string; required)

        - ariaSort (string; required)

        - ariaValueMax (string; required)

        - ariaValueMin (string; required)

        - ariaValueNow (string; required)

        - ariaValueText (string; required)

        - assignedSlot (dict; required)

            `assignedSlot` is a dict with keys:

            - ATTRIBUTE_NODE (number; required)

            - CDATA_SECTION_NODE (number; required):
                node is a CDATASection node.

            - COMMENT_NODE (number; required):
                node is a Comment node.

            - DOCUMENT_FRAGMENT_NODE (number; required):
                node is a DocumentFragment node.

            - DOCUMENT_NODE (number; required):
                node is a document.

            - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                Set when other is a descendant of node.

            - DOCUMENT_POSITION_CONTAINS (number; required):
                Set when other is an ancestor of node.

            - DOCUMENT_POSITION_DISCONNECTED (number; required):
                Set when node and other are not in the same tree.

            - DOCUMENT_POSITION_FOLLOWING (number; required):
                Set when other is following node.

            - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

            - DOCUMENT_POSITION_PRECEDING (number; required):
                Set when other is preceding node.

            - DOCUMENT_TYPE_NODE (number; required):
                node is a doctype.

            - ELEMENT_NODE (number; required):
                node is an element.

            - ENTITY_NODE (number; required)

            - ENTITY_REFERENCE_NODE (number; required)

            - NOTATION_NODE (number; required)

            - PROCESSING_INSTRUCTION_NODE (number; required):
                node is a ProcessingInstruction node.

            - TEXT_NODE (number; required):
                node is a Text node.

            - accessKey (string; required)

            - accessKeyLabel (string; required)

            - addEventListener (required)

            - after (required):
                Inserts nodes just after node, while replacing strings
                in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - animate (required)

            - append (required):
                Inserts nodes after the last child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - appendChild (required)

            - ariaAtomic (string; required)

            - ariaAutoComplete (string; required)

            - ariaBusy (string; required)

            - ariaChecked (string; required)

            - ariaColCount (string; required)

            - ariaColIndex (string; required)

            - ariaColIndexText (string; required)

            - ariaColSpan (string; required)

            - ariaCurrent (string; required)

            - ariaDisabled (string; required)

            - ariaExpanded (string; required)

            - ariaHasPopup (string; required)

            - ariaHidden (string; required)

            - ariaInvalid (string; required)

            - ariaKeyShortcuts (string; required)

            - ariaLabel (string; required)

            - ariaLevel (string; required)

            - ariaLive (string; required)

            - ariaModal (string; required)

            - ariaMultiLine (string; required)

            - ariaMultiSelectable (string; required)

            - ariaOrientation (string; required)

            - ariaPlaceholder (string; required)

            - ariaPosInSet (string; required)

            - ariaPressed (string; required)

            - ariaReadOnly (string; required)

            - ariaRequired (string; required)

            - ariaRoleDescription (string; required)

            - ariaRowCount (string; required)

            - ariaRowIndex (string; required)

            - ariaRowIndexText (string; required)

            - ariaRowSpan (string; required)

            - ariaSelected (string; required)

            - ariaSetSize (string; required)

            - ariaSort (string; required)

            - ariaValueMax (string; required)

            - ariaValueMin (string; required)

            - ariaValueNow (string; required)

            - ariaValueText (string; required)

            - assign (required)

            - assignedElements (required)

            - assignedNodes (required)

            - assignedSlot (boolean | number | string | dict | list; required)

            - attachInternals (required)

            - attachShadow (required):
                Creates a shadow root for element and returns it.

            - attributes (dict; required)

                `attributes` is a dict with strings as keys and values
                of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

            - autocapitalize (string; required)

            - autofocus (boolean; required)

            - baseURI (string; required):
                Returns node's node document's document base URL.

            - before (required):
                Inserts nodes just before node, while replacing
                strings in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - blur (required)

            - childElementCount (number; required)

            - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                Returns the children.

            - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                Returns the child elements.

            - classList (dict with strings as keys and values of type string; required):
                Allows for manipulation of element's class content
                attribute as a set of whitespace-separated tokens
                through a DOMTokenList object.

            - className (string; required):
                Returns the value of element's class content
                attribute. Can be set to change it.

            - click (required)

            - clientHeight (number; required)

            - clientLeft (number; required)

            - clientTop (number; required)

            - clientWidth (number; required)

            - cloneNode (required):
                Returns a copy of node. If deep is True, the copy also
                includes the node's descendants.

            - closest (dict; required):
                Returns the first (starting at element) inclusive
                ancestor that matches selectors, and None otherwise.

                `closest` is a dict with keys:


            - compareDocumentPosition (required):
                Returns a bitmask indicating the position of other
                relative to node.

            - contains (required):
                Returns True if other is an inclusive descendant of
                node, and False otherwise.

            - contentEditable (string; required)

            - dataset (dict with strings as keys and values of type string; required)

            - dir (string; required)

            - dispatchEvent (required):
                Dispatches a synthetic event event to target and
                returns True if either event's cancelable attribute
                value is False or its preventDefault() method was not
                invoked, and False otherwise.

            - draggable (boolean; required)

            - enterKeyHint (string; required)

            - firstChild (boolean | number | string | dict | list; required):
                Returns the first child.

            - firstElementChild (a list of or a singular dash component, string or number; required):
                Returns the first child that is an element, and None
                otherwise.

            - focus (required)

            - getAnimations (required)

            - getAttribute (required):
                Returns element's first attribute whose qualified name
                is qualifiedName, and None if there is no such
                attribute otherwise.

            - getAttributeNS (required):
                Returns element's attribute whose namespace is
                namespace and local name is localName, and None if
                there is no such attribute otherwise.

            - getAttributeNames (required):
                Returns the qualified names of all element's
                attributes. Can contain duplicates.

            - getAttributeNode (required)

            - getAttributeNodeNS (required)

            - getBoundingClientRect (required)

            - getClientRects (required)

            - getElementsByClassName (required):
                Returns a HTMLCollection of the elements in the object
                on which the method was invoked (a document or an
                element) that have all the classes given by
                classNames. The classNames argument is interpreted as
                a space-separated list of classes.

            - getElementsByTagName (dict; required)

                `getElementsByTagName` is a dict with keys:


            - getElementsByTagNameNS (dict; required)

                `getElementsByTagNameNS` is a dict with keys:


            - getRootNode (required):
                Returns node's root.

            - hasAttribute (required):
                Returns True if element has an attribute whose
                qualified name is qualifiedName, and False otherwise.

            - hasAttributeNS (required):
                Returns True if element has an attribute whose
                namespace is namespace and local name is localName.

            - hasAttributes (required):
                Returns True if element has attributes, and False
                otherwise.

            - hasChildNodes (required):
                Returns whether node has children.

            - hasPointerCapture (required)

            - hidden (boolean; required)

            - id (string; required):
                Returns the value of element's id content attribute.
                Can be set to change it.

            - inert (boolean; required)

            - innerHTML (string; required)

            - innerText (string; required)

            - inputMode (string; required)

            - insertAdjacentElement (required)

            - insertAdjacentHTML (required)

            - insertAdjacentText (required)

            - insertBefore (required)

            - isConnected (boolean; required):
                Returns True if node is connected and False otherwise.

            - isContentEditable (boolean; required)

            - isDefaultNamespace (required)

            - isEqualNode (required):
                Returns whether node and otherNode have the same
                properties.

            - isSameNode (required)

            - lang (string; required)

            - lastChild (boolean | number | string | dict | list; required):
                Returns the last child.

            - lastElementChild (a list of or a singular dash component, string or number; required):
                Returns the last child that is an element, and None
                otherwise.

            - localName (string; required):
                Returns the local name.

            - lookupNamespaceURI (required)

            - lookupPrefix (required)

            - matches (required):
                Returns True if matching selectors against element's
                root yields element, and False otherwise.

            - name (string; required)

            - namespaceURI (string; required):
                Returns the namespace.

            - nextElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first following sibling that is an
                element, and None otherwise.

            - nextSibling (boolean | number | string | dict | list; required):
                Returns the next sibling.

            - nodeName (string; required):
                Returns a string appropriate for the type of node.

            - nodeType (number; required):
                Returns the type of node.

            - nodeValue (string; required)

            - nonce (string; optional)

            - normalize (required):
                Removes empty exclusive Text nodes and concatenates
                the data of remaining contiguous exclusive Text nodes
                into the first of their nodes.

            - offsetHeight (number; required)

            - offsetLeft (number; required)

            - offsetParent (a list of or a singular dash component, string or number; required)

            - offsetTop (number; required)

            - offsetWidth (number; required)

            - onabort (required):
                Fires when the user aborts the download. @,param,ev,
                ,The event.

            - onanimationcancel (required)

            - onanimationend (required)

            - onanimationiteration (required)

            - onanimationstart (required)

            - onauxclick (required)

            - onbeforeinput (required)

            - onblur (required):
                Fires when the object loses the input focus.
                @,param,ev, ,The focus event.

            - oncancel (required)

            - oncanplay (required):
                Occurs when playback is possible, but would require
                further buffering. @,param,ev, ,The event.

            - oncanplaythrough (required)

            - onchange (required):
                Fires when the contents of the object or selection
                have changed. @,param,ev, ,The event.

            - onclick (required):
                Fires when the user clicks the left mouse button on
                the object @,param,ev, ,The mouse event.

            - onclose (required)

            - oncontextmenu (required):
                Fires when the user clicks the right mouse button in
                the client area, opening the context menu. @,param,ev,
                ,The mouse event.

            - oncopy (required)

            - oncuechange (required)

            - oncut (required)

            - ondblclick (required):
                Fires when the user double-clicks the object.
                @,param,ev, ,The mouse event.

            - ondrag (required):
                Fires on the source object continuously during a drag
                operation. @,param,ev, ,The event.

            - ondragend (required):
                Fires on the source object when the user releases the
                mouse at the close of a drag operation. @,param,ev,
                ,The event.

            - ondragenter (required):
                Fires on the target element when the user drags the
                object to a valid drop target. @,param,ev, ,The drag
                event.

            - ondragleave (required):
                Fires on the target object when the user moves the
                mouse out of a valid drop target during a drag
                operation. @,param,ev, ,The drag event.

            - ondragover (required):
                Fires on the target element continuously while the
                user drags the object over a valid drop target.
                @,param,ev, ,The event.

            - ondragstart (required):
                Fires on the source object when the user starts to
                drag a text selection or selected object. @,param,ev,
                ,The event.

            - ondrop (required)

            - ondurationchange (required):
                Occurs when the duration attribute is updated.
                @,param,ev, ,The event.

            - onemptied (required):
                Occurs when the media element is reset to its initial
                state. @,param,ev, ,The event.

            - onended (required):
                Occurs when the end of playback is reached.
                @,param,ev, ,The event.

            - onerror (dict; required):
                Fires when an error occurs during object loading.
                @,param,ev, ,The event.

                `onerror` is a dict with keys:


            - onfocus (required):
                Fires when the object receives focus. @,param,ev, ,The
                event.

            - onformdata (required)

            - onfullscreenchange (required)

            - onfullscreenerror (required)

            - ongotpointercapture (required)

            - oninput (required)

            - oninvalid (required)

            - onkeydown (required):
                Fires when the user presses a key. @,param,ev, ,The
                keyboard event.

            - onkeypress (required):
                Fires when the user presses an alphanumeric key.
                @,param,ev, ,The event. @,deprecated.

            - onkeyup (required):
                Fires when the user releases a key. @,param,ev, ,The
                keyboard event.

            - onload (required):
                Fires immediately after the browser loads the object.
                @,param,ev, ,The event.

            - onloadeddata (required):
                Occurs when media data is loaded at the current
                playback position. @,param,ev, ,The event.

            - onloadedmetadata (required):
                Occurs when the duration and dimensions of the media
                have been determined. @,param,ev, ,The event.

            - onloadstart (required):
                Occurs when Internet Explorer begins looking for media
                data. @,param,ev, ,The event.

            - onlostpointercapture (required)

            - onmousedown (required):
                Fires when the user clicks the object with either
                mouse button. @,param,ev, ,The mouse event.

            - onmouseenter (required)

            - onmouseleave (required)

            - onmousemove (required):
                Fires when the user moves the mouse over the object.
                @,param,ev, ,The mouse event.

            - onmouseout (required):
                Fires when the user moves the mouse pointer outside
                the boundaries of the object. @,param,ev, ,The mouse
                event.

            - onmouseover (required):
                Fires when the user moves the mouse pointer into the
                object. @,param,ev, ,The mouse event.

            - onmouseup (required):
                Fires when the user releases a mouse button while the
                mouse is over the object. @,param,ev, ,The mouse
                event.

            - onpaste (required)

            - onpause (required):
                Occurs when playback is paused. @,param,ev, ,The
                event.

            - onplay (required):
                Occurs when the play method is requested. @,param,ev,
                ,The event.

            - onplaying (required):
                Occurs when the audio or video has started playing.
                @,param,ev, ,The event.

            - onpointercancel (required)

            - onpointerdown (required)

            - onpointerenter (required)

            - onpointerleave (required)

            - onpointermove (required)

            - onpointerout (required)

            - onpointerover (required)

            - onpointerup (required)

            - onprogress (required):
                Occurs to indicate progress while downloading media
                data. @,param,ev, ,The event.

            - onratechange (required):
                Occurs when the playback rate is increased or
                decreased. @,param,ev, ,The event.

            - onreset (required):
                Fires when the user resets a form. @,param,ev, ,The
                event.

            - onresize (required)

            - onscroll (required):
                Fires when the user repositions the scroll box in the
                scroll bar on the object. @,param,ev, ,The event.

            - onsecuritypolicyviolation (required)

            - onseeked (required):
                Occurs when the seek operation ends. @,param,ev, ,The
                event.

            - onseeking (required):
                Occurs when the current playback position is moved.
                @,param,ev, ,The event.

            - onselect (required):
                Fires when the current selection changes. @,param,ev,
                ,The event.

            - onselectionchange (required)

            - onselectstart (required)

            - onslotchange (required)

            - onstalled (required):
                Occurs when the download has stopped. @,param,ev, ,The
                event.

            - onsubmit (required)

            - onsuspend (required):
                Occurs if the load operation has been intentionally
                halted. @,param,ev, ,The event.

            - ontimeupdate (required):
                Occurs to indicate the current playback position.
                @,param,ev, ,The event.

            - ontoggle (required)

            - ontouchcancel (optional)

            - ontouchend (optional)

            - ontouchmove (optional)

            - ontouchstart (optional)

            - ontransitioncancel (required)

            - ontransitionend (required)

            - ontransitionrun (required)

            - ontransitionstart (required)

            - onvolumechange (required):
                Occurs when the volume is changed, or playback is
                muted or unmuted. @,param,ev, ,The event.

            - onwaiting (required):
                Occurs when playback stops because the next frame of a
                video resource is not available. @,param,ev, ,The
                event.

            - onwebkitanimationend (required)

            - onwebkitanimationiteration (required)

            - onwebkitanimationstart (required)

            - onwebkittransitionend (required)

            - onwheel (required)

            - outerHTML (string; required)

            - outerText (string; required)

            - ownerDocument (boolean | number | string | dict | list; required)

            - parentElement (boolean | number | string | dict | list; required):
                Returns the parent element.

            - parentNode (boolean | number | string | dict | list; required):
                Returns the parent.

            - part (dict with strings as keys and values of type string; required)

            - prefix (string; required):
                Returns the namespace prefix.

            - prepend (required):
                Inserts nodes before the first child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - previousElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first preceding sibling that is an
                element, and None otherwise.

            - previousSibling (boolean | number | string | dict | list; required):
                Returns the previous sibling.

            - querySelector (dict; required):
                Returns the first element that is a descendant of node
                that matches selectors.

                `querySelector` is a dict with keys:


            - querySelectorAll (dict; required):
                Returns all element descendants of node that match
                selectors.

                `querySelectorAll` is a dict with keys:


            - releasePointerCapture (required)

            - remove (required):
                Removes node.

            - removeAttribute (required):
                Removes element's first attribute whose qualified name
                is qualifiedName.

            - removeAttributeNS (required):
                Removes element's attribute whose namespace is
                namespace and local name is localName.

            - removeAttributeNode (required)

            - removeChild (required)

            - removeEventListener (required)

            - replaceChild (required)

            - replaceChildren (required):
                Replace all children of node with nodes, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - replaceWith (required):
                Replaces node with nodes, while replacing strings in
                nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - requestFullscreen (required):
                Displays element fullscreen and resolves promise when
                done.  When supplied, options's navigationUI member
                indicates whether showing navigation UI while in
                fullscreen is preferred or not. If set to \"show\",
                navigation simplicity is preferred over screen space,
                and if set to \"hide\", more screen space is
                preferred. User agents are always free to honor user
                preference over the application's. The default value
                \"auto\" indicates no application preference.

            - requestPointerLock (required)

            - role (string; required)

            - scroll (dict; required)

                `scroll` is a dict with keys:


            - scrollBy (dict; required)

                `scrollBy` is a dict with keys:


            - scrollHeight (number; required)

            - scrollIntoView (required)

            - scrollLeft (number; required)

            - scrollTo (dict; required)

                `scrollTo` is a dict with keys:


            - scrollTop (number; required)

            - scrollWidth (number; required)

            - setAttribute (required):
                Sets the value of element's first attribute whose
                qualified name is qualifiedName to value.

            - setAttributeNS (required):
                Sets the value of element's attribute whose namespace
                is namespace and local name is localName to value.

            - setAttributeNode (required)

            - setAttributeNodeNS (required)

            - setPointerCapture (required)

            - shadowRoot (boolean | number | string | dict | list; required):
                Returns element's shadow root, if any, and if shadow
                root's mode is \"open\", and None otherwise.

            - slot (string; required):
                Returns the value of element's slot content attribute.
                Can be set to change it.

            - spellcheck (boolean; required)

            - style (dict with strings as keys and values of type string; required)

            - tabIndex (number; required)

            - tagName (string; required):
                Returns the HTML-uppercased qualified name.

            - textContent (string; required)

            - title (string; required)

            - toggleAttribute (required):
                If force is not given, \"toggles\" qualifiedName,
                removing it if it is present and adding it if it is
                not present. If force is True, adds qualifiedName. If
                force is False, removes qualifiedName.  Returns True
                if qualifiedName is now present, and False otherwise.

            - translate (boolean; required)

            - webkitMatchesSelector (required)

        - attachInternals (required)

        - attachShadow (required):
            Creates a shadow root for element and returns it.

        - attributes (dict; required)

            `attributes` is a dict with strings as keys and values of
            type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

        - autocapitalize (string; required)

        - autofocus (boolean; required)

        - baseURI (string; required):
            Returns node's node document's document base URL.

        - before (required):
            Inserts nodes just before node, while replacing strings in
            nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - blur (required)

        - childElementCount (number; required)

        - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
            Returns the children.

        - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
            Returns the child elements.

        - classList (dict with strings as keys and values of type string; required):
            Allows for manipulation of element's class content
            attribute as a set of whitespace-separated tokens through
            a DOMTokenList object.

        - className (string; required):
            Returns the value of element's class content attribute.
            Can be set to change it.

        - click (required)

        - clientHeight (number; required)

        - clientLeft (number; required)

        - clientTop (number; required)

        - clientWidth (number; required)

        - cloneNode (required):
            Returns a copy of node. If deep is True, the copy also
            includes the node's descendants.

        - closest (dict; required):
            Returns the first (starting at element) inclusive ancestor
            that matches selectors, and None otherwise.

            `closest` is a dict with keys:


        - compareDocumentPosition (required):
            Returns a bitmask indicating the position of other
            relative to node.

        - contains (required):
            Returns True if other is an inclusive descendant of node,
            and False otherwise.

        - contentEditable (string; required)

        - dataset (dict with strings as keys and values of type string; required)

        - dir (string; required)

        - dispatchEvent (required):
            Dispatches a synthetic event event to target and returns
            True if either event's cancelable attribute value is False
            or its preventDefault() method was not invoked, and False
            otherwise.

        - draggable (boolean; required)

        - enterKeyHint (string; required)

        - firstChild (boolean | number | string | dict | list; required):
            Returns the first child.

        - firstElementChild (a list of or a singular dash component, string or number; required):
            Returns the first child that is an element, and None
            otherwise.

        - focus (required)

        - getAnimations (required)

        - getAttribute (required):
            Returns element's first attribute whose qualified name is
            qualifiedName, and None if there is no such attribute
            otherwise.

        - getAttributeNS (required):
            Returns element's attribute whose namespace is namespace
            and local name is localName, and None if there is no such
            attribute otherwise.

        - getAttributeNames (required):
            Returns the qualified names of all element's attributes.
            Can contain duplicates.

        - getAttributeNode (required)

        - getAttributeNodeNS (required)

        - getBoundingClientRect (required)

        - getClientRects (required)

        - getElementsByClassName (required):
            Returns a HTMLCollection of the elements in the object on
            which the method was invoked (a document or an element)
            that have all the classes given by classNames. The
            classNames argument is interpreted as a space-separated
            list of classes.

        - getElementsByTagName (dict; required)

            `getElementsByTagName` is a dict with keys:


        - getElementsByTagNameNS (dict; required)

            `getElementsByTagNameNS` is a dict with keys:


        - getRootNode (required):
            Returns node's root.

        - hasAttribute (required):
            Returns True if element has an attribute whose qualified
            name is qualifiedName, and False otherwise.

        - hasAttributeNS (required):
            Returns True if element has an attribute whose namespace
            is namespace and local name is localName.

        - hasAttributes (required):
            Returns True if element has attributes, and False
            otherwise.

        - hasChildNodes (required):
            Returns whether node has children.

        - hasPointerCapture (required)

        - hidden (boolean; required)

        - id (string; required):
            Returns the value of element's id content attribute. Can
            be set to change it.

        - inert (boolean; required)

        - innerHTML (string; required)

        - innerText (string; required)

        - inputMode (string; required)

        - insertAdjacentElement (required)

        - insertAdjacentHTML (required)

        - insertAdjacentText (required)

        - insertBefore (required)

        - isConnected (boolean; required):
            Returns True if node is connected and False otherwise.

        - isContentEditable (boolean; required)

        - isDefaultNamespace (required)

        - isEqualNode (required):
            Returns whether node and otherNode have the same
            properties.

        - isSameNode (required)

        - lang (string; required)

        - lastChild (boolean | number | string | dict | list; required):
            Returns the last child.

        - lastElementChild (a list of or a singular dash component, string or number; required):
            Returns the last child that is an element, and None
            otherwise.

        - localName (string; required):
            Returns the local name.

        - lookupNamespaceURI (required)

        - lookupPrefix (required)

        - matches (required):
            Returns True if matching selectors against element's root
            yields element, and False otherwise.

        - namespaceURI (string; required):
            Returns the namespace.

        - nextElementSibling (a list of or a singular dash component, string or number; required):
            Returns the first following sibling that is an element,
            and None otherwise.

        - nextSibling (boolean | number | string | dict | list; required):
            Returns the next sibling.

        - nodeName (string; required):
            Returns a string appropriate for the type of node.

        - nodeType (number; required):
            Returns the type of node.

        - nodeValue (string; required)

        - nonce (string; optional)

        - normalize (required):
            Removes empty exclusive Text nodes and concatenates the
            data of remaining contiguous exclusive Text nodes into the
            first of their nodes.

        - offsetHeight (number; required)

        - offsetLeft (number; required)

        - offsetParent (a list of or a singular dash component, string or number; required)

        - offsetTop (number; required)

        - offsetWidth (number; required)

        - onabort (required):
            Fires when the user aborts the download. @,param,ev, ,The
            event.

        - onanimationcancel (required)

        - onanimationend (required)

        - onanimationiteration (required)

        - onanimationstart (required)

        - onauxclick (required)

        - onbeforeinput (required)

        - onblur (required):
            Fires when the object loses the input focus. @,param,ev,
            ,The focus event.

        - oncancel (required)

        - oncanplay (required):
            Occurs when playback is possible, but would require
            further buffering. @,param,ev, ,The event.

        - oncanplaythrough (required)

        - onchange (required):
            Fires when the contents of the object or selection have
            changed. @,param,ev, ,The event.

        - onclick (required):
            Fires when the user clicks the left mouse button on the
            object @,param,ev, ,The mouse event.

        - onclose (required)

        - oncontextmenu (required):
            Fires when the user clicks the right mouse button in the
            client area, opening the context menu. @,param,ev, ,The
            mouse event.

        - oncopy (required)

        - oncuechange (required)

        - oncut (required)

        - ondblclick (required):
            Fires when the user double-clicks the object. @,param,ev,
            ,The mouse event.

        - ondrag (required):
            Fires on the source object continuously during a drag
            operation. @,param,ev, ,The event.

        - ondragend (required):
            Fires on the source object when the user releases the
            mouse at the close of a drag operation. @,param,ev, ,The
            event.

        - ondragenter (required):
            Fires on the target element when the user drags the object
            to a valid drop target. @,param,ev, ,The drag event.

        - ondragleave (required):
            Fires on the target object when the user moves the mouse
            out of a valid drop target during a drag operation.
            @,param,ev, ,The drag event.

        - ondragover (required):
            Fires on the target element continuously while the user
            drags the object over a valid drop target. @,param,ev,
            ,The event.

        - ondragstart (required):
            Fires on the source object when the user starts to drag a
            text selection or selected object. @,param,ev, ,The event.

        - ondrop (required)

        - ondurationchange (required):
            Occurs when the duration attribute is updated. @,param,ev,
            ,The event.

        - onemptied (required):
            Occurs when the media element is reset to its initial
            state. @,param,ev, ,The event.

        - onended (required):
            Occurs when the end of playback is reached. @,param,ev,
            ,The event.

        - onerror (dict; required):
            Fires when an error occurs during object loading.
            @,param,ev, ,The event.

            `onerror` is a dict with keys:


        - onfocus (required):
            Fires when the object receives focus. @,param,ev, ,The
            event.

        - onformdata (required)

        - onfullscreenchange (required)

        - onfullscreenerror (required)

        - ongotpointercapture (required)

        - oninput (required)

        - oninvalid (required)

        - onkeydown (required):
            Fires when the user presses a key. @,param,ev, ,The
            keyboard event.

        - onkeypress (required):
            Fires when the user presses an alphanumeric key.
            @,param,ev, ,The event. @,deprecated.

        - onkeyup (required):
            Fires when the user releases a key. @,param,ev, ,The
            keyboard event.

        - onload (required):
            Fires immediately after the browser loads the object.
            @,param,ev, ,The event.

        - onloadeddata (required):
            Occurs when media data is loaded at the current playback
            position. @,param,ev, ,The event.

        - onloadedmetadata (required):
            Occurs when the duration and dimensions of the media have
            been determined. @,param,ev, ,The event.

        - onloadstart (required):
            Occurs when Internet Explorer begins looking for media
            data. @,param,ev, ,The event.

        - onlostpointercapture (required)

        - onmousedown (required):
            Fires when the user clicks the object with either mouse
            button. @,param,ev, ,The mouse event.

        - onmouseenter (required)

        - onmouseleave (required)

        - onmousemove (required):
            Fires when the user moves the mouse over the object.
            @,param,ev, ,The mouse event.

        - onmouseout (required):
            Fires when the user moves the mouse pointer outside the
            boundaries of the object. @,param,ev, ,The mouse event.

        - onmouseover (required):
            Fires when the user moves the mouse pointer into the
            object. @,param,ev, ,The mouse event.

        - onmouseup (required):
            Fires when the user releases a mouse button while the
            mouse is over the object. @,param,ev, ,The mouse event.

        - onpaste (required)

        - onpause (required):
            Occurs when playback is paused. @,param,ev, ,The event.

        - onplay (required):
            Occurs when the play method is requested. @,param,ev, ,The
            event.

        - onplaying (required):
            Occurs when the audio or video has started playing.
            @,param,ev, ,The event.

        - onpointercancel (required)

        - onpointerdown (required)

        - onpointerenter (required)

        - onpointerleave (required)

        - onpointermove (required)

        - onpointerout (required)

        - onpointerover (required)

        - onpointerup (required)

        - onprogress (required):
            Occurs to indicate progress while downloading media data.
            @,param,ev, ,The event.

        - onratechange (required):
            Occurs when the playback rate is increased or decreased.
            @,param,ev, ,The event.

        - onreset (required):
            Fires when the user resets a form. @,param,ev, ,The event.

        - onresize (required)

        - onscroll (required):
            Fires when the user repositions the scroll box in the
            scroll bar on the object. @,param,ev, ,The event.

        - onsecuritypolicyviolation (required)

        - onseeked (required):
            Occurs when the seek operation ends. @,param,ev, ,The
            event.

        - onseeking (required):
            Occurs when the current playback position is moved.
            @,param,ev, ,The event.

        - onselect (required):
            Fires when the current selection changes. @,param,ev, ,The
            event.

        - onselectionchange (required)

        - onselectstart (required)

        - onslotchange (required)

        - onstalled (required):
            Occurs when the download has stopped. @,param,ev, ,The
            event.

        - onsubmit (required)

        - onsuspend (required):
            Occurs if the load operation has been intentionally
            halted. @,param,ev, ,The event.

        - ontimeupdate (required):
            Occurs to indicate the current playback position.
            @,param,ev, ,The event.

        - ontoggle (required)

        - ontouchcancel (optional)

        - ontouchend (optional)

        - ontouchmove (optional)

        - ontouchstart (optional)

        - ontransitioncancel (required)

        - ontransitionend (required)

        - ontransitionrun (required)

        - ontransitionstart (required)

        - onvolumechange (required):
            Occurs when the volume is changed, or playback is muted or
            unmuted. @,param,ev, ,The event.

        - onwaiting (required):
            Occurs when playback stops because the next frame of a
            video resource is not available. @,param,ev, ,The event.

        - onwebkitanimationend (required)

        - onwebkitanimationiteration (required)

        - onwebkitanimationstart (required)

        - onwebkittransitionend (required)

        - onwheel (required)

        - outerHTML (string; required)

        - outerText (string; required)

        - ownerDocument (boolean | number | string | dict | list; required)

        - parentElement (boolean | number | string | dict | list; required):
            Returns the parent element.

        - parentNode (boolean | number | string | dict | list; required):
            Returns the parent.

        - part (dict with strings as keys and values of type string; required)

        - prefix (string; required):
            Returns the namespace prefix.

        - prepend (required):
            Inserts nodes before the first child of node, while
            replacing strings in nodes with equivalent Text nodes.
            Throws a \"HierarchyRequestError\" DOMException if the
            constraints of the node tree are violated.

        - previousElementSibling (a list of or a singular dash component, string or number; required):
            Returns the first preceding sibling that is an element,
            and None otherwise.

        - previousSibling (boolean | number | string | dict | list; required):
            Returns the previous sibling.

        - querySelector (dict; required):
            Returns the first element that is a descendant of node
            that matches selectors.

            `querySelector` is a dict with keys:


        - querySelectorAll (dict; required):
            Returns all element descendants of node that match
            selectors.

            `querySelectorAll` is a dict with keys:


        - releasePointerCapture (required)

        - remove (required):
            Removes node.

        - removeAttribute (required):
            Removes element's first attribute whose qualified name is
            qualifiedName.

        - removeAttributeNS (required):
            Removes element's attribute whose namespace is namespace
            and local name is localName.

        - removeAttributeNode (required)

        - removeChild (required)

        - removeEventListener (required)

        - replaceChild (required)

        - replaceChildren (required):
            Replace all children of node with nodes, while replacing
            strings in nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - replaceWith (required):
            Replaces node with nodes, while replacing strings in nodes
            with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - requestFullscreen (required):
            Displays element fullscreen and resolves promise when
            done.  When supplied, options's navigationUI member
            indicates whether showing navigation UI while in
            fullscreen is preferred or not. If set to \"show\",
            navigation simplicity is preferred over screen space, and
            if set to \"hide\", more screen space is preferred. User
            agents are always free to honor user preference over the
            application's. The default value \"auto\" indicates no
            application preference.

        - requestPointerLock (required)

        - role (string; required)

        - scroll (dict; required)

            `scroll` is a dict with keys:


        - scrollBy (dict; required)

            `scrollBy` is a dict with keys:


        - scrollHeight (number; required)

        - scrollIntoView (required)

        - scrollLeft (number; required)

        - scrollTo (dict; required)

            `scrollTo` is a dict with keys:


        - scrollTop (number; required)

        - scrollWidth (number; required)

        - setAttribute (required):
            Sets the value of element's first attribute whose
            qualified name is qualifiedName to value.

        - setAttributeNS (required):
            Sets the value of element's attribute whose namespace is
            namespace and local name is localName to value.

        - setAttributeNode (required)

        - setAttributeNodeNS (required)

        - setPointerCapture (required)

        - shadowRoot (boolean | number | string | dict | list; required):
            Returns element's shadow root, if any, and if shadow
            root's mode is \"open\", and None otherwise.

        - slot (string; required):
            Returns the value of element's slot content attribute. Can
            be set to change it.

        - spellcheck (boolean; required)

        - style (dict with strings as keys and values of type string; required)

        - tabIndex (number; required)

        - tagName (string; required):
            Returns the HTML-uppercased qualified name.

        - textContent (string; required)

        - title (string; required)

        - toggleAttribute (required):
            If force is not given, \"toggles\" qualifiedName, removing
            it if it is present and adding it if it is not present. If
            force is True, adds qualifiedName. If force is False,
            removes qualifiedName.  Returns True if qualifiedName is
            now present, and False otherwise.

        - translate (boolean; required)

        - webkitMatchesSelector (required)

    - defaultDate (dict; optional):
        The initial date to view when first opened.

        `defaultDate` is a dict with keys:

        - __@toPrimitive@4735 (dict; required):
            Converts a Date object to a string.   Converts a Date
            object to a number.   Converts a Date object to a string
            or number. @,param,hint, ,The strings \"number\",
            \"string\", or \"default\" to specify what primitive to
            return. @,throws,{TypeError} If 'hint' was given something
            other than \"number\", \"string\", or \"default\".
            @,returns,A number if 'hint' was \"number\", a string if
            'hint' was \"string\" or \"default\".

            `__@toPrimitive@4735` is a dict with keys:


        - getDate (required):
            Gets the day-of-the-month, using local time.

        - getDay (required):
            Gets the day of the week, using local time.

        - getFullYear (required):
            Gets the year, using local time.

        - getHours (required):
            Gets the hours in a date, using local time.

        - getMilliseconds (required):
            Gets the milliseconds of a Date, using local time.

        - getMinutes (required):
            Gets the minutes of a Date object, using local time.

        - getMonth (required):
            Gets the month, using local time.

        - getSeconds (required):
            Gets the seconds of a Date object, using local time.

        - getTime (required):
            Gets the time value in milliseconds.

        - getTimezoneOffset (required):
            Gets the difference in minutes between the time on the
            local computer and Universal Coordinated Time (UTC).

        - getUTCDate (required):
            Gets the day-of-the-month, using Universal Coordinated
            Time (UTC).

        - getUTCDay (required):
            Gets the day of the week using Universal Coordinated Time
            (UTC).

        - getUTCFullYear (required):
            Gets the year using Universal Coordinated Time (UTC).

        - getUTCHours (required):
            Gets the hours value in a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMilliseconds (required):
            Gets the milliseconds of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMinutes (required):
            Gets the minutes of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMonth (required):
            Gets the month of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCSeconds (required):
            Gets the seconds of a Date object using Universal
            Coordinated Time (UTC).

        - getVarDate (required)

        - setDate (required):
            Sets the numeric day-of-the-month value of the Date object
            using local time. @,param,date, ,A numeric value equal to
            the day of the month.

        - setFullYear (required):
            Sets the year of the Date object using local time.
            @,param,year, ,A numeric value for the year.
            @,param,month, ,A zero-based numeric value for the month
            (0 for January, 11 for December). Must be specified if
            numDate is specified. @,param,date, ,A numeric value equal
            for the day of the month.

        - setHours (required):
            Sets the hour value in the Date object using local time.
            @,param,hours, ,A numeric value equal to the hours value.
            @,param,min, ,A numeric value equal to the minutes value.
            @,param,sec, ,A numeric value equal to the seconds value.
            @,param,ms, ,A numeric value equal to the milliseconds
            value.

        - setMilliseconds (required):
            Sets the milliseconds value in the Date object using local
            time. @,param,ms, ,A numeric value equal to the
            millisecond value.

        - setMinutes (required):
            Sets the minutes value in the Date object using local
            time. @,param,min, ,A numeric value equal to the minutes
            value. @,param,sec, ,A numeric value equal to the seconds
            value. @,param,ms, ,A numeric value equal to the
            milliseconds value.

        - setMonth (required):
            Sets the month value in the Date object using local time.
            @,param,month, ,A numeric value equal to the month. The
            value for January is 0, and other month values follow
            consecutively. @,param,date, ,A numeric value representing
            the day of the month. If this value is not supplied, the
            value from a call to the getDate method is used.

        - setSeconds (required):
            Sets the seconds value in the Date object using local
            time. @,param,sec, ,A numeric value equal to the seconds
            value. @,param,ms, ,A numeric value equal to the
            milliseconds value.

        - setTime (required):
            Sets the date and time value in the Date object.
            @,param,time, ,A numeric value representing the number of
            elapsed milliseconds since midnight, January 1, 1970 GMT.

        - setUTCDate (required):
            Sets the numeric day of the month in the Date object using
            Universal Coordinated Time (UTC). @,param,date, ,A numeric
            value equal to the day of the month.

        - setUTCFullYear (required):
            Sets the year value in the Date object using Universal
            Coordinated Time (UTC). @,param,year, ,A numeric value
            equal to the year. @,param,month, ,A numeric value equal
            to the month. The value for January is 0, and other month
            values follow consecutively. Must be supplied if numDate
            is supplied. @,param,date, ,A numeric value equal to the
            day of the month.

        - setUTCHours (required):
            Sets the hours value in the Date object using Universal
            Coordinated Time (UTC). @,param,hours, ,A numeric value
            equal to the hours value. @,param,min, ,A numeric value
            equal to the minutes value. @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - setUTCMilliseconds (required):
            Sets the milliseconds value in the Date object using
            Universal Coordinated Time (UTC). @,param,ms, ,A numeric
            value equal to the millisecond value.

        - setUTCMinutes (required):
            Sets the minutes value in the Date object using Universal
            Coordinated Time (UTC). @,param,min, ,A numeric value
            equal to the minutes value. @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - setUTCMonth (required):
            Sets the month value in the Date object using Universal
            Coordinated Time (UTC). @,param,month, ,A numeric value
            equal to the month. The value for January is 0, and other
            month values follow consecutively. @,param,date, ,A
            numeric value representing the day of the month. If it is
            not supplied, the value from a call to the getUTCDate
            method is used.

        - setUTCSeconds (required):
            Sets the seconds value in the Date object using Universal
            Coordinated Time (UTC). @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - toDateString (required):
            Returns a date as a string value.

        - toISOString (required):
            Returns a date as a string value in ISO format.

        - toJSON (required):
            Used by the JSON.stringify method to enable the
            transformation of an object's data for JavaScript Object
            Notation (JSON) serialization.

        - toLocaleDateString (dict; required):
            Returns a date as a string value appropriate to the host
            environment's current locale.   Converts a date to a
            string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleDateString` is a dict with keys:


        - toLocaleString (dict; optional):
            Returns a value as a string value appropriate to the host
            environment's current locale.   Converts a date and time
            to a string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleString` is a dict with keys:


        - toLocaleTimeString (dict; required):
            Returns a time as a string value appropriate to the host
            environment's current locale.   Converts a time to a
            string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleTimeString` is a dict with keys:


        - toString (optional):
            Returns a string representation of a date. The format of
            the string depends on the locale.

        - toTimeString (required):
            Returns a time as a string value.

        - toUTCString (required):
            Returns a date converted to a string using Universal
            Coordinated Time (UTC).

        - valueOf (optional):
            Returns the stored time value in milliseconds since
            midnight, January 1, 1970 UTC.

    - disableDayFn (optional):
        Callback function that gets passed a Date object for each day
        in view. Should return True to disable selection of that day.

    - disableWeekends (boolean; optional):
        Disallow selection of Saturdays and Sundays.

    - enableSelectionDaysInNextAndPreviousMonths (boolean; optional):
        Allows user to select date that is in the next or previous
        months (default: False).

    - events (list of strings; optional):
        Array of dates that you would like to differentiate from
        regular days (e.g. ['Sat Jun 28 2017', 'Sun Jun 29 2017', 'Tue
        Jul 01 2017',]).

    - field (dict; optional):
        Bind the datepicker to a form field.

        `field` is a dict with keys:

        - ATTRIBUTE_NODE (number; required)

        - CDATA_SECTION_NODE (number; required):
            node is a CDATASection node.

        - COMMENT_NODE (number; required):
            node is a Comment node.

        - DOCUMENT_FRAGMENT_NODE (number; required):
            node is a DocumentFragment node.

        - DOCUMENT_NODE (number; required):
            node is a document.

        - DOCUMENT_POSITION_CONTAINED_BY (number; required):
            Set when other is a descendant of node.

        - DOCUMENT_POSITION_CONTAINS (number; required):
            Set when other is an ancestor of node.

        - DOCUMENT_POSITION_DISCONNECTED (number; required):
            Set when node and other are not in the same tree.

        - DOCUMENT_POSITION_FOLLOWING (number; required):
            Set when other is following node.

        - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

        - DOCUMENT_POSITION_PRECEDING (number; required):
            Set when other is preceding node.

        - DOCUMENT_TYPE_NODE (number; required):
            node is a doctype.

        - ELEMENT_NODE (number; required):
            node is an element.

        - ENTITY_NODE (number; required)

        - ENTITY_REFERENCE_NODE (number; required)

        - NOTATION_NODE (number; required)

        - PROCESSING_INSTRUCTION_NODE (number; required):
            node is a ProcessingInstruction node.

        - TEXT_NODE (number; required):
            node is a Text node.

        - accessKey (string; required)

        - accessKeyLabel (string; required)

        - addEventListener (required)

        - after (required):
            Inserts nodes just after node, while replacing strings in
            nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - animate (required)

        - append (required):
            Inserts nodes after the last child of node, while
            replacing strings in nodes with equivalent Text nodes.
            Throws a \"HierarchyRequestError\" DOMException if the
            constraints of the node tree are violated.

        - appendChild (required)

        - ariaAtomic (string; required)

        - ariaAutoComplete (string; required)

        - ariaBusy (string; required)

        - ariaChecked (string; required)

        - ariaColCount (string; required)

        - ariaColIndex (string; required)

        - ariaColIndexText (string; required)

        - ariaColSpan (string; required)

        - ariaCurrent (string; required)

        - ariaDisabled (string; required)

        - ariaExpanded (string; required)

        - ariaHasPopup (string; required)

        - ariaHidden (string; required)

        - ariaInvalid (string; required)

        - ariaKeyShortcuts (string; required)

        - ariaLabel (string; required)

        - ariaLevel (string; required)

        - ariaLive (string; required)

        - ariaModal (string; required)

        - ariaMultiLine (string; required)

        - ariaMultiSelectable (string; required)

        - ariaOrientation (string; required)

        - ariaPlaceholder (string; required)

        - ariaPosInSet (string; required)

        - ariaPressed (string; required)

        - ariaReadOnly (string; required)

        - ariaRequired (string; required)

        - ariaRoleDescription (string; required)

        - ariaRowCount (string; required)

        - ariaRowIndex (string; required)

        - ariaRowIndexText (string; required)

        - ariaRowSpan (string; required)

        - ariaSelected (string; required)

        - ariaSetSize (string; required)

        - ariaSort (string; required)

        - ariaValueMax (string; required)

        - ariaValueMin (string; required)

        - ariaValueNow (string; required)

        - ariaValueText (string; required)

        - assignedSlot (dict; required)

            `assignedSlot` is a dict with keys:

            - ATTRIBUTE_NODE (number; required)

            - CDATA_SECTION_NODE (number; required):
                node is a CDATASection node.

            - COMMENT_NODE (number; required):
                node is a Comment node.

            - DOCUMENT_FRAGMENT_NODE (number; required):
                node is a DocumentFragment node.

            - DOCUMENT_NODE (number; required):
                node is a document.

            - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                Set when other is a descendant of node.

            - DOCUMENT_POSITION_CONTAINS (number; required):
                Set when other is an ancestor of node.

            - DOCUMENT_POSITION_DISCONNECTED (number; required):
                Set when node and other are not in the same tree.

            - DOCUMENT_POSITION_FOLLOWING (number; required):
                Set when other is following node.

            - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

            - DOCUMENT_POSITION_PRECEDING (number; required):
                Set when other is preceding node.

            - DOCUMENT_TYPE_NODE (number; required):
                node is a doctype.

            - ELEMENT_NODE (number; required):
                node is an element.

            - ENTITY_NODE (number; required)

            - ENTITY_REFERENCE_NODE (number; required)

            - NOTATION_NODE (number; required)

            - PROCESSING_INSTRUCTION_NODE (number; required):
                node is a ProcessingInstruction node.

            - TEXT_NODE (number; required):
                node is a Text node.

            - accessKey (string; required)

            - accessKeyLabel (string; required)

            - addEventListener (required)

            - after (required):
                Inserts nodes just after node, while replacing strings
                in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - animate (required)

            - append (required):
                Inserts nodes after the last child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - appendChild (required)

            - ariaAtomic (string; required)

            - ariaAutoComplete (string; required)

            - ariaBusy (string; required)

            - ariaChecked (string; required)

            - ariaColCount (string; required)

            - ariaColIndex (string; required)

            - ariaColIndexText (string; required)

            - ariaColSpan (string; required)

            - ariaCurrent (string; required)

            - ariaDisabled (string; required)

            - ariaExpanded (string; required)

            - ariaHasPopup (string; required)

            - ariaHidden (string; required)

            - ariaInvalid (string; required)

            - ariaKeyShortcuts (string; required)

            - ariaLabel (string; required)

            - ariaLevel (string; required)

            - ariaLive (string; required)

            - ariaModal (string; required)

            - ariaMultiLine (string; required)

            - ariaMultiSelectable (string; required)

            - ariaOrientation (string; required)

            - ariaPlaceholder (string; required)

            - ariaPosInSet (string; required)

            - ariaPressed (string; required)

            - ariaReadOnly (string; required)

            - ariaRequired (string; required)

            - ariaRoleDescription (string; required)

            - ariaRowCount (string; required)

            - ariaRowIndex (string; required)

            - ariaRowIndexText (string; required)

            - ariaRowSpan (string; required)

            - ariaSelected (string; required)

            - ariaSetSize (string; required)

            - ariaSort (string; required)

            - ariaValueMax (string; required)

            - ariaValueMin (string; required)

            - ariaValueNow (string; required)

            - ariaValueText (string; required)

            - assign (required)

            - assignedElements (required)

            - assignedNodes (required)

            - assignedSlot (boolean | number | string | dict | list; required)

            - attachInternals (required)

            - attachShadow (required):
                Creates a shadow root for element and returns it.

            - attributes (dict; required)

                `attributes` is a dict with strings as keys and values
                of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

            - autocapitalize (string; required)

            - autofocus (boolean; required)

            - baseURI (string; required):
                Returns node's node document's document base URL.

            - before (required):
                Inserts nodes just before node, while replacing
                strings in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - blur (required)

            - childElementCount (number; required)

            - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                Returns the children.

            - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                Returns the child elements.

            - classList (dict with strings as keys and values of type string; required):
                Allows for manipulation of element's class content
                attribute as a set of whitespace-separated tokens
                through a DOMTokenList object.

            - className (string; required):
                Returns the value of element's class content
                attribute. Can be set to change it.

            - click (required)

            - clientHeight (number; required)

            - clientLeft (number; required)

            - clientTop (number; required)

            - clientWidth (number; required)

            - cloneNode (required):
                Returns a copy of node. If deep is True, the copy also
                includes the node's descendants.

            - closest (dict; required):
                Returns the first (starting at element) inclusive
                ancestor that matches selectors, and None otherwise.

                `closest` is a dict with keys:


            - compareDocumentPosition (required):
                Returns a bitmask indicating the position of other
                relative to node.

            - contains (required):
                Returns True if other is an inclusive descendant of
                node, and False otherwise.

            - contentEditable (string; required)

            - dataset (dict with strings as keys and values of type string; required)

            - dir (string; required)

            - dispatchEvent (required):
                Dispatches a synthetic event event to target and
                returns True if either event's cancelable attribute
                value is False or its preventDefault() method was not
                invoked, and False otherwise.

            - draggable (boolean; required)

            - enterKeyHint (string; required)

            - firstChild (boolean | number | string | dict | list; required):
                Returns the first child.

            - firstElementChild (a list of or a singular dash component, string or number; required):
                Returns the first child that is an element, and None
                otherwise.

            - focus (required)

            - getAnimations (required)

            - getAttribute (required):
                Returns element's first attribute whose qualified name
                is qualifiedName, and None if there is no such
                attribute otherwise.

            - getAttributeNS (required):
                Returns element's attribute whose namespace is
                namespace and local name is localName, and None if
                there is no such attribute otherwise.

            - getAttributeNames (required):
                Returns the qualified names of all element's
                attributes. Can contain duplicates.

            - getAttributeNode (required)

            - getAttributeNodeNS (required)

            - getBoundingClientRect (required)

            - getClientRects (required)

            - getElementsByClassName (required):
                Returns a HTMLCollection of the elements in the object
                on which the method was invoked (a document or an
                element) that have all the classes given by
                classNames. The classNames argument is interpreted as
                a space-separated list of classes.

            - getElementsByTagName (dict; required)

                `getElementsByTagName` is a dict with keys:


            - getElementsByTagNameNS (dict; required)

                `getElementsByTagNameNS` is a dict with keys:


            - getRootNode (required):
                Returns node's root.

            - hasAttribute (required):
                Returns True if element has an attribute whose
                qualified name is qualifiedName, and False otherwise.

            - hasAttributeNS (required):
                Returns True if element has an attribute whose
                namespace is namespace and local name is localName.

            - hasAttributes (required):
                Returns True if element has attributes, and False
                otherwise.

            - hasChildNodes (required):
                Returns whether node has children.

            - hasPointerCapture (required)

            - hidden (boolean; required)

            - id (string; required):
                Returns the value of element's id content attribute.
                Can be set to change it.

            - inert (boolean; required)

            - innerHTML (string; required)

            - innerText (string; required)

            - inputMode (string; required)

            - insertAdjacentElement (required)

            - insertAdjacentHTML (required)

            - insertAdjacentText (required)

            - insertBefore (required)

            - isConnected (boolean; required):
                Returns True if node is connected and False otherwise.

            - isContentEditable (boolean; required)

            - isDefaultNamespace (required)

            - isEqualNode (required):
                Returns whether node and otherNode have the same
                properties.

            - isSameNode (required)

            - lang (string; required)

            - lastChild (boolean | number | string | dict | list; required):
                Returns the last child.

            - lastElementChild (a list of or a singular dash component, string or number; required):
                Returns the last child that is an element, and None
                otherwise.

            - localName (string; required):
                Returns the local name.

            - lookupNamespaceURI (required)

            - lookupPrefix (required)

            - matches (required):
                Returns True if matching selectors against element's
                root yields element, and False otherwise.

            - name (string; required)

            - namespaceURI (string; required):
                Returns the namespace.

            - nextElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first following sibling that is an
                element, and None otherwise.

            - nextSibling (boolean | number | string | dict | list; required):
                Returns the next sibling.

            - nodeName (string; required):
                Returns a string appropriate for the type of node.

            - nodeType (number; required):
                Returns the type of node.

            - nodeValue (string; required)

            - nonce (string; optional)

            - normalize (required):
                Removes empty exclusive Text nodes and concatenates
                the data of remaining contiguous exclusive Text nodes
                into the first of their nodes.

            - offsetHeight (number; required)

            - offsetLeft (number; required)

            - offsetParent (a list of or a singular dash component, string or number; required)

            - offsetTop (number; required)

            - offsetWidth (number; required)

            - onabort (required):
                Fires when the user aborts the download. @,param,ev,
                ,The event.

            - onanimationcancel (required)

            - onanimationend (required)

            - onanimationiteration (required)

            - onanimationstart (required)

            - onauxclick (required)

            - onbeforeinput (required)

            - onblur (required):
                Fires when the object loses the input focus.
                @,param,ev, ,The focus event.

            - oncancel (required)

            - oncanplay (required):
                Occurs when playback is possible, but would require
                further buffering. @,param,ev, ,The event.

            - oncanplaythrough (required)

            - onchange (required):
                Fires when the contents of the object or selection
                have changed. @,param,ev, ,The event.

            - onclick (required):
                Fires when the user clicks the left mouse button on
                the object @,param,ev, ,The mouse event.

            - onclose (required)

            - oncontextmenu (required):
                Fires when the user clicks the right mouse button in
                the client area, opening the context menu. @,param,ev,
                ,The mouse event.

            - oncopy (required)

            - oncuechange (required)

            - oncut (required)

            - ondblclick (required):
                Fires when the user double-clicks the object.
                @,param,ev, ,The mouse event.

            - ondrag (required):
                Fires on the source object continuously during a drag
                operation. @,param,ev, ,The event.

            - ondragend (required):
                Fires on the source object when the user releases the
                mouse at the close of a drag operation. @,param,ev,
                ,The event.

            - ondragenter (required):
                Fires on the target element when the user drags the
                object to a valid drop target. @,param,ev, ,The drag
                event.

            - ondragleave (required):
                Fires on the target object when the user moves the
                mouse out of a valid drop target during a drag
                operation. @,param,ev, ,The drag event.

            - ondragover (required):
                Fires on the target element continuously while the
                user drags the object over a valid drop target.
                @,param,ev, ,The event.

            - ondragstart (required):
                Fires on the source object when the user starts to
                drag a text selection or selected object. @,param,ev,
                ,The event.

            - ondrop (required)

            - ondurationchange (required):
                Occurs when the duration attribute is updated.
                @,param,ev, ,The event.

            - onemptied (required):
                Occurs when the media element is reset to its initial
                state. @,param,ev, ,The event.

            - onended (required):
                Occurs when the end of playback is reached.
                @,param,ev, ,The event.

            - onerror (dict; required):
                Fires when an error occurs during object loading.
                @,param,ev, ,The event.

                `onerror` is a dict with keys:


            - onfocus (required):
                Fires when the object receives focus. @,param,ev, ,The
                event.

            - onformdata (required)

            - onfullscreenchange (required)

            - onfullscreenerror (required)

            - ongotpointercapture (required)

            - oninput (required)

            - oninvalid (required)

            - onkeydown (required):
                Fires when the user presses a key. @,param,ev, ,The
                keyboard event.

            - onkeypress (required):
                Fires when the user presses an alphanumeric key.
                @,param,ev, ,The event. @,deprecated.

            - onkeyup (required):
                Fires when the user releases a key. @,param,ev, ,The
                keyboard event.

            - onload (required):
                Fires immediately after the browser loads the object.
                @,param,ev, ,The event.

            - onloadeddata (required):
                Occurs when media data is loaded at the current
                playback position. @,param,ev, ,The event.

            - onloadedmetadata (required):
                Occurs when the duration and dimensions of the media
                have been determined. @,param,ev, ,The event.

            - onloadstart (required):
                Occurs when Internet Explorer begins looking for media
                data. @,param,ev, ,The event.

            - onlostpointercapture (required)

            - onmousedown (required):
                Fires when the user clicks the object with either
                mouse button. @,param,ev, ,The mouse event.

            - onmouseenter (required)

            - onmouseleave (required)

            - onmousemove (required):
                Fires when the user moves the mouse over the object.
                @,param,ev, ,The mouse event.

            - onmouseout (required):
                Fires when the user moves the mouse pointer outside
                the boundaries of the object. @,param,ev, ,The mouse
                event.

            - onmouseover (required):
                Fires when the user moves the mouse pointer into the
                object. @,param,ev, ,The mouse event.

            - onmouseup (required):
                Fires when the user releases a mouse button while the
                mouse is over the object. @,param,ev, ,The mouse
                event.

            - onpaste (required)

            - onpause (required):
                Occurs when playback is paused. @,param,ev, ,The
                event.

            - onplay (required):
                Occurs when the play method is requested. @,param,ev,
                ,The event.

            - onplaying (required):
                Occurs when the audio or video has started playing.
                @,param,ev, ,The event.

            - onpointercancel (required)

            - onpointerdown (required)

            - onpointerenter (required)

            - onpointerleave (required)

            - onpointermove (required)

            - onpointerout (required)

            - onpointerover (required)

            - onpointerup (required)

            - onprogress (required):
                Occurs to indicate progress while downloading media
                data. @,param,ev, ,The event.

            - onratechange (required):
                Occurs when the playback rate is increased or
                decreased. @,param,ev, ,The event.

            - onreset (required):
                Fires when the user resets a form. @,param,ev, ,The
                event.

            - onresize (required)

            - onscroll (required):
                Fires when the user repositions the scroll box in the
                scroll bar on the object. @,param,ev, ,The event.

            - onsecuritypolicyviolation (required)

            - onseeked (required):
                Occurs when the seek operation ends. @,param,ev, ,The
                event.

            - onseeking (required):
                Occurs when the current playback position is moved.
                @,param,ev, ,The event.

            - onselect (required):
                Fires when the current selection changes. @,param,ev,
                ,The event.

            - onselectionchange (required)

            - onselectstart (required)

            - onslotchange (required)

            - onstalled (required):
                Occurs when the download has stopped. @,param,ev, ,The
                event.

            - onsubmit (required)

            - onsuspend (required):
                Occurs if the load operation has been intentionally
                halted. @,param,ev, ,The event.

            - ontimeupdate (required):
                Occurs to indicate the current playback position.
                @,param,ev, ,The event.

            - ontoggle (required)

            - ontouchcancel (optional)

            - ontouchend (optional)

            - ontouchmove (optional)

            - ontouchstart (optional)

            - ontransitioncancel (required)

            - ontransitionend (required)

            - ontransitionrun (required)

            - ontransitionstart (required)

            - onvolumechange (required):
                Occurs when the volume is changed, or playback is
                muted or unmuted. @,param,ev, ,The event.

            - onwaiting (required):
                Occurs when playback stops because the next frame of a
                video resource is not available. @,param,ev, ,The
                event.

            - onwebkitanimationend (required)

            - onwebkitanimationiteration (required)

            - onwebkitanimationstart (required)

            - onwebkittransitionend (required)

            - onwheel (required)

            - outerHTML (string; required)

            - outerText (string; required)

            - ownerDocument (boolean | number | string | dict | list; required)

            - parentElement (boolean | number | string | dict | list; required):
                Returns the parent element.

            - parentNode (boolean | number | string | dict | list; required):
                Returns the parent.

            - part (dict with strings as keys and values of type string; required)

            - prefix (string; required):
                Returns the namespace prefix.

            - prepend (required):
                Inserts nodes before the first child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - previousElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first preceding sibling that is an
                element, and None otherwise.

            - previousSibling (boolean | number | string | dict | list; required):
                Returns the previous sibling.

            - querySelector (dict; required):
                Returns the first element that is a descendant of node
                that matches selectors.

                `querySelector` is a dict with keys:


            - querySelectorAll (dict; required):
                Returns all element descendants of node that match
                selectors.

                `querySelectorAll` is a dict with keys:


            - releasePointerCapture (required)

            - remove (required):
                Removes node.

            - removeAttribute (required):
                Removes element's first attribute whose qualified name
                is qualifiedName.

            - removeAttributeNS (required):
                Removes element's attribute whose namespace is
                namespace and local name is localName.

            - removeAttributeNode (required)

            - removeChild (required)

            - removeEventListener (required)

            - replaceChild (required)

            - replaceChildren (required):
                Replace all children of node with nodes, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - replaceWith (required):
                Replaces node with nodes, while replacing strings in
                nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - requestFullscreen (required):
                Displays element fullscreen and resolves promise when
                done.  When supplied, options's navigationUI member
                indicates whether showing navigation UI while in
                fullscreen is preferred or not. If set to \"show\",
                navigation simplicity is preferred over screen space,
                and if set to \"hide\", more screen space is
                preferred. User agents are always free to honor user
                preference over the application's. The default value
                \"auto\" indicates no application preference.

            - requestPointerLock (required)

            - role (string; required)

            - scroll (dict; required)

                `scroll` is a dict with keys:


            - scrollBy (dict; required)

                `scrollBy` is a dict with keys:


            - scrollHeight (number; required)

            - scrollIntoView (required)

            - scrollLeft (number; required)

            - scrollTo (dict; required)

                `scrollTo` is a dict with keys:


            - scrollTop (number; required)

            - scrollWidth (number; required)

            - setAttribute (required):
                Sets the value of element's first attribute whose
                qualified name is qualifiedName to value.

            - setAttributeNS (required):
                Sets the value of element's attribute whose namespace
                is namespace and local name is localName to value.

            - setAttributeNode (required)

            - setAttributeNodeNS (required)

            - setPointerCapture (required)

            - shadowRoot (boolean | number | string | dict | list; required):
                Returns element's shadow root, if any, and if shadow
                root's mode is \"open\", and None otherwise.

            - slot (string; required):
                Returns the value of element's slot content attribute.
                Can be set to change it.

            - spellcheck (boolean; required)

            - style (dict with strings as keys and values of type string; required)

            - tabIndex (number; required)

            - tagName (string; required):
                Returns the HTML-uppercased qualified name.

            - textContent (string; required)

            - title (string; required)

            - toggleAttribute (required):
                If force is not given, \"toggles\" qualifiedName,
                removing it if it is present and adding it if it is
                not present. If force is True, adds qualifiedName. If
                force is False, removes qualifiedName.  Returns True
                if qualifiedName is now present, and False otherwise.

            - translate (boolean; required)

            - webkitMatchesSelector (required)

        - attachInternals (required)

        - attachShadow (required):
            Creates a shadow root for element and returns it.

        - attributes (dict; required)

            `attributes` is a dict with strings as keys and values of
            type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

        - autocapitalize (string; required)

        - autofocus (boolean; required)

        - baseURI (string; required):
            Returns node's node document's document base URL.

        - before (required):
            Inserts nodes just before node, while replacing strings in
            nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - blur (required)

        - childElementCount (number; required)

        - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
            Returns the children.

        - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
            Returns the child elements.

        - classList (dict with strings as keys and values of type string; required):
            Allows for manipulation of element's class content
            attribute as a set of whitespace-separated tokens through
            a DOMTokenList object.

        - className (string; required):
            Returns the value of element's class content attribute.
            Can be set to change it.

        - click (required)

        - clientHeight (number; required)

        - clientLeft (number; required)

        - clientTop (number; required)

        - clientWidth (number; required)

        - cloneNode (required):
            Returns a copy of node. If deep is True, the copy also
            includes the node's descendants.

        - closest (dict; required):
            Returns the first (starting at element) inclusive ancestor
            that matches selectors, and None otherwise.

            `closest` is a dict with keys:


        - compareDocumentPosition (required):
            Returns a bitmask indicating the position of other
            relative to node.

        - contains (required):
            Returns True if other is an inclusive descendant of node,
            and False otherwise.

        - contentEditable (string; required)

        - dataset (dict with strings as keys and values of type string; required)

        - dir (string; required)

        - dispatchEvent (required):
            Dispatches a synthetic event event to target and returns
            True if either event's cancelable attribute value is False
            or its preventDefault() method was not invoked, and False
            otherwise.

        - draggable (boolean; required)

        - enterKeyHint (string; required)

        - firstChild (boolean | number | string | dict | list; required):
            Returns the first child.

        - firstElementChild (a list of or a singular dash component, string or number; required):
            Returns the first child that is an element, and None
            otherwise.

        - focus (required)

        - getAnimations (required)

        - getAttribute (required):
            Returns element's first attribute whose qualified name is
            qualifiedName, and None if there is no such attribute
            otherwise.

        - getAttributeNS (required):
            Returns element's attribute whose namespace is namespace
            and local name is localName, and None if there is no such
            attribute otherwise.

        - getAttributeNames (required):
            Returns the qualified names of all element's attributes.
            Can contain duplicates.

        - getAttributeNode (required)

        - getAttributeNodeNS (required)

        - getBoundingClientRect (required)

        - getClientRects (required)

        - getElementsByClassName (required):
            Returns a HTMLCollection of the elements in the object on
            which the method was invoked (a document or an element)
            that have all the classes given by classNames. The
            classNames argument is interpreted as a space-separated
            list of classes.

        - getElementsByTagName (dict; required)

            `getElementsByTagName` is a dict with keys:


        - getElementsByTagNameNS (dict; required)

            `getElementsByTagNameNS` is a dict with keys:


        - getRootNode (required):
            Returns node's root.

        - hasAttribute (required):
            Returns True if element has an attribute whose qualified
            name is qualifiedName, and False otherwise.

        - hasAttributeNS (required):
            Returns True if element has an attribute whose namespace
            is namespace and local name is localName.

        - hasAttributes (required):
            Returns True if element has attributes, and False
            otherwise.

        - hasChildNodes (required):
            Returns whether node has children.

        - hasPointerCapture (required)

        - hidden (boolean; required)

        - id (string; required):
            Returns the value of element's id content attribute. Can
            be set to change it.

        - inert (boolean; required)

        - innerHTML (string; required)

        - innerText (string; required)

        - inputMode (string; required)

        - insertAdjacentElement (required)

        - insertAdjacentHTML (required)

        - insertAdjacentText (required)

        - insertBefore (required)

        - isConnected (boolean; required):
            Returns True if node is connected and False otherwise.

        - isContentEditable (boolean; required)

        - isDefaultNamespace (required)

        - isEqualNode (required):
            Returns whether node and otherNode have the same
            properties.

        - isSameNode (required)

        - lang (string; required)

        - lastChild (boolean | number | string | dict | list; required):
            Returns the last child.

        - lastElementChild (a list of or a singular dash component, string or number; required):
            Returns the last child that is an element, and None
            otherwise.

        - localName (string; required):
            Returns the local name.

        - lookupNamespaceURI (required)

        - lookupPrefix (required)

        - matches (required):
            Returns True if matching selectors against element's root
            yields element, and False otherwise.

        - namespaceURI (string; required):
            Returns the namespace.

        - nextElementSibling (a list of or a singular dash component, string or number; required):
            Returns the first following sibling that is an element,
            and None otherwise.

        - nextSibling (boolean | number | string | dict | list; required):
            Returns the next sibling.

        - nodeName (string; required):
            Returns a string appropriate for the type of node.

        - nodeType (number; required):
            Returns the type of node.

        - nodeValue (string; required)

        - nonce (string; optional)

        - normalize (required):
            Removes empty exclusive Text nodes and concatenates the
            data of remaining contiguous exclusive Text nodes into the
            first of their nodes.

        - offsetHeight (number; required)

        - offsetLeft (number; required)

        - offsetParent (a list of or a singular dash component, string or number; required)

        - offsetTop (number; required)

        - offsetWidth (number; required)

        - onabort (required):
            Fires when the user aborts the download. @,param,ev, ,The
            event.

        - onanimationcancel (required)

        - onanimationend (required)

        - onanimationiteration (required)

        - onanimationstart (required)

        - onauxclick (required)

        - onbeforeinput (required)

        - onblur (required):
            Fires when the object loses the input focus. @,param,ev,
            ,The focus event.

        - oncancel (required)

        - oncanplay (required):
            Occurs when playback is possible, but would require
            further buffering. @,param,ev, ,The event.

        - oncanplaythrough (required)

        - onchange (required):
            Fires when the contents of the object or selection have
            changed. @,param,ev, ,The event.

        - onclick (required):
            Fires when the user clicks the left mouse button on the
            object @,param,ev, ,The mouse event.

        - onclose (required)

        - oncontextmenu (required):
            Fires when the user clicks the right mouse button in the
            client area, opening the context menu. @,param,ev, ,The
            mouse event.

        - oncopy (required)

        - oncuechange (required)

        - oncut (required)

        - ondblclick (required):
            Fires when the user double-clicks the object. @,param,ev,
            ,The mouse event.

        - ondrag (required):
            Fires on the source object continuously during a drag
            operation. @,param,ev, ,The event.

        - ondragend (required):
            Fires on the source object when the user releases the
            mouse at the close of a drag operation. @,param,ev, ,The
            event.

        - ondragenter (required):
            Fires on the target element when the user drags the object
            to a valid drop target. @,param,ev, ,The drag event.

        - ondragleave (required):
            Fires on the target object when the user moves the mouse
            out of a valid drop target during a drag operation.
            @,param,ev, ,The drag event.

        - ondragover (required):
            Fires on the target element continuously while the user
            drags the object over a valid drop target. @,param,ev,
            ,The event.

        - ondragstart (required):
            Fires on the source object when the user starts to drag a
            text selection or selected object. @,param,ev, ,The event.

        - ondrop (required)

        - ondurationchange (required):
            Occurs when the duration attribute is updated. @,param,ev,
            ,The event.

        - onemptied (required):
            Occurs when the media element is reset to its initial
            state. @,param,ev, ,The event.

        - onended (required):
            Occurs when the end of playback is reached. @,param,ev,
            ,The event.

        - onerror (dict; required):
            Fires when an error occurs during object loading.
            @,param,ev, ,The event.

            `onerror` is a dict with keys:


        - onfocus (required):
            Fires when the object receives focus. @,param,ev, ,The
            event.

        - onformdata (required)

        - onfullscreenchange (required)

        - onfullscreenerror (required)

        - ongotpointercapture (required)

        - oninput (required)

        - oninvalid (required)

        - onkeydown (required):
            Fires when the user presses a key. @,param,ev, ,The
            keyboard event.

        - onkeypress (required):
            Fires when the user presses an alphanumeric key.
            @,param,ev, ,The event. @,deprecated.

        - onkeyup (required):
            Fires when the user releases a key. @,param,ev, ,The
            keyboard event.

        - onload (required):
            Fires immediately after the browser loads the object.
            @,param,ev, ,The event.

        - onloadeddata (required):
            Occurs when media data is loaded at the current playback
            position. @,param,ev, ,The event.

        - onloadedmetadata (required):
            Occurs when the duration and dimensions of the media have
            been determined. @,param,ev, ,The event.

        - onloadstart (required):
            Occurs when Internet Explorer begins looking for media
            data. @,param,ev, ,The event.

        - onlostpointercapture (required)

        - onmousedown (required):
            Fires when the user clicks the object with either mouse
            button. @,param,ev, ,The mouse event.

        - onmouseenter (required)

        - onmouseleave (required)

        - onmousemove (required):
            Fires when the user moves the mouse over the object.
            @,param,ev, ,The mouse event.

        - onmouseout (required):
            Fires when the user moves the mouse pointer outside the
            boundaries of the object. @,param,ev, ,The mouse event.

        - onmouseover (required):
            Fires when the user moves the mouse pointer into the
            object. @,param,ev, ,The mouse event.

        - onmouseup (required):
            Fires when the user releases a mouse button while the
            mouse is over the object. @,param,ev, ,The mouse event.

        - onpaste (required)

        - onpause (required):
            Occurs when playback is paused. @,param,ev, ,The event.

        - onplay (required):
            Occurs when the play method is requested. @,param,ev, ,The
            event.

        - onplaying (required):
            Occurs when the audio or video has started playing.
            @,param,ev, ,The event.

        - onpointercancel (required)

        - onpointerdown (required)

        - onpointerenter (required)

        - onpointerleave (required)

        - onpointermove (required)

        - onpointerout (required)

        - onpointerover (required)

        - onpointerup (required)

        - onprogress (required):
            Occurs to indicate progress while downloading media data.
            @,param,ev, ,The event.

        - onratechange (required):
            Occurs when the playback rate is increased or decreased.
            @,param,ev, ,The event.

        - onreset (required):
            Fires when the user resets a form. @,param,ev, ,The event.

        - onresize (required)

        - onscroll (required):
            Fires when the user repositions the scroll box in the
            scroll bar on the object. @,param,ev, ,The event.

        - onsecuritypolicyviolation (required)

        - onseeked (required):
            Occurs when the seek operation ends. @,param,ev, ,The
            event.

        - onseeking (required):
            Occurs when the current playback position is moved.
            @,param,ev, ,The event.

        - onselect (required):
            Fires when the current selection changes. @,param,ev, ,The
            event.

        - onselectionchange (required)

        - onselectstart (required)

        - onslotchange (required)

        - onstalled (required):
            Occurs when the download has stopped. @,param,ev, ,The
            event.

        - onsubmit (required)

        - onsuspend (required):
            Occurs if the load operation has been intentionally
            halted. @,param,ev, ,The event.

        - ontimeupdate (required):
            Occurs to indicate the current playback position.
            @,param,ev, ,The event.

        - ontoggle (required)

        - ontouchcancel (optional)

        - ontouchend (optional)

        - ontouchmove (optional)

        - ontouchstart (optional)

        - ontransitioncancel (required)

        - ontransitionend (required)

        - ontransitionrun (required)

        - ontransitionstart (required)

        - onvolumechange (required):
            Occurs when the volume is changed, or playback is muted or
            unmuted. @,param,ev, ,The event.

        - onwaiting (required):
            Occurs when playback stops because the next frame of a
            video resource is not available. @,param,ev, ,The event.

        - onwebkitanimationend (required)

        - onwebkitanimationiteration (required)

        - onwebkitanimationstart (required)

        - onwebkittransitionend (required)

        - onwheel (required)

        - outerHTML (string; required)

        - outerText (string; required)

        - ownerDocument (boolean | number | string | dict | list; required)

        - parentElement (boolean | number | string | dict | list; required):
            Returns the parent element.

        - parentNode (boolean | number | string | dict | list; required):
            Returns the parent.

        - part (dict with strings as keys and values of type string; required)

        - prefix (string; required):
            Returns the namespace prefix.

        - prepend (required):
            Inserts nodes before the first child of node, while
            replacing strings in nodes with equivalent Text nodes.
            Throws a \"HierarchyRequestError\" DOMException if the
            constraints of the node tree are violated.

        - previousElementSibling (a list of or a singular dash component, string or number; required):
            Returns the first preceding sibling that is an element,
            and None otherwise.

        - previousSibling (boolean | number | string | dict | list; required):
            Returns the previous sibling.

        - querySelector (dict; required):
            Returns the first element that is a descendant of node
            that matches selectors.

            `querySelector` is a dict with keys:


        - querySelectorAll (dict; required):
            Returns all element descendants of node that match
            selectors.

            `querySelectorAll` is a dict with keys:


        - releasePointerCapture (required)

        - remove (required):
            Removes node.

        - removeAttribute (required):
            Removes element's first attribute whose qualified name is
            qualifiedName.

        - removeAttributeNS (required):
            Removes element's attribute whose namespace is namespace
            and local name is localName.

        - removeAttributeNode (required)

        - removeChild (required)

        - removeEventListener (required)

        - replaceChild (required)

        - replaceChildren (required):
            Replace all children of node with nodes, while replacing
            strings in nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - replaceWith (required):
            Replaces node with nodes, while replacing strings in nodes
            with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - requestFullscreen (required):
            Displays element fullscreen and resolves promise when
            done.  When supplied, options's navigationUI member
            indicates whether showing navigation UI while in
            fullscreen is preferred or not. If set to \"show\",
            navigation simplicity is preferred over screen space, and
            if set to \"hide\", more screen space is preferred. User
            agents are always free to honor user preference over the
            application's. The default value \"auto\" indicates no
            application preference.

        - requestPointerLock (required)

        - role (string; required)

        - scroll (dict; required)

            `scroll` is a dict with keys:


        - scrollBy (dict; required)

            `scrollBy` is a dict with keys:


        - scrollHeight (number; required)

        - scrollIntoView (required)

        - scrollLeft (number; required)

        - scrollTo (dict; required)

            `scrollTo` is a dict with keys:


        - scrollTop (number; required)

        - scrollWidth (number; required)

        - setAttribute (required):
            Sets the value of element's first attribute whose
            qualified name is qualifiedName to value.

        - setAttributeNS (required):
            Sets the value of element's attribute whose namespace is
            namespace and local name is localName to value.

        - setAttributeNode (required)

        - setAttributeNodeNS (required)

        - setPointerCapture (required)

        - shadowRoot (boolean | number | string | dict | list; required):
            Returns element's shadow root, if any, and if shadow
            root's mode is \"open\", and None otherwise.

        - slot (string; required):
            Returns the value of element's slot content attribute. Can
            be set to change it.

        - spellcheck (boolean; required)

        - style (dict with strings as keys and values of type string; required)

        - tabIndex (number; required)

        - tagName (string; required):
            Returns the HTML-uppercased qualified name.

        - textContent (string; required)

        - title (string; required)

        - toggleAttribute (required):
            If force is not given, \"toggles\" qualifiedName, removing
            it if it is present and adding it if it is not present. If
            force is True, adds qualifiedName. If force is False,
            removes qualifiedName.  Returns True if qualifiedName is
            now present, and False otherwise.

        - translate (boolean; required)

        - webkitMatchesSelector (required)

    - firstDay (number; optional):
        First day of the week (0: Sunday, 1: Monday, etc).

    - format (string; optional):
        The default output format for toString() and field value.
        Requires Moment.js for custom formatting.

    - formatStrict (boolean; optional):
        The default flag for moment's strict date parsing (requires
        Moment.js for custom formatting). Default: False.

    - i18n (dict; optional):
        Language defaults for month and weekday names.

        `i18n` is a dict with keys:

        - months (list of strings; required)

        - nextMonth (string; required)

        - previousMonth (string; required)

        - weekdays (list of strings; required)

        - weekdaysShort (list of strings; required)

    - isRTL (boolean; optional):
        Reverse the calendar for right-to-left languages. Default:
        False.

    - keyboardInput (boolean; optional):
        Enable keyboard input support. Default: True.

    - mainCalendar (string; optional):
        When numberOfMonths is used, this will help you to choose
        where the main calendar will be (default left, can be set to
        right). Only used for the first display or when a selected
        date is not already visible.

    - maxDate (dict; optional):
        The latest date that can be selected (this should be a native
        Date object - e.g. new Date() or moment().toDate()).

        `maxDate` is a dict with keys:

        - __@toPrimitive@4735 (dict; required):
            Converts a Date object to a string.   Converts a Date
            object to a number.   Converts a Date object to a string
            or number. @,param,hint, ,The strings \"number\",
            \"string\", or \"default\" to specify what primitive to
            return. @,throws,{TypeError} If 'hint' was given something
            other than \"number\", \"string\", or \"default\".
            @,returns,A number if 'hint' was \"number\", a string if
            'hint' was \"string\" or \"default\".

            `__@toPrimitive@4735` is a dict with keys:


        - getDate (required):
            Gets the day-of-the-month, using local time.

        - getDay (required):
            Gets the day of the week, using local time.

        - getFullYear (required):
            Gets the year, using local time.

        - getHours (required):
            Gets the hours in a date, using local time.

        - getMilliseconds (required):
            Gets the milliseconds of a Date, using local time.

        - getMinutes (required):
            Gets the minutes of a Date object, using local time.

        - getMonth (required):
            Gets the month, using local time.

        - getSeconds (required):
            Gets the seconds of a Date object, using local time.

        - getTime (required):
            Gets the time value in milliseconds.

        - getTimezoneOffset (required):
            Gets the difference in minutes between the time on the
            local computer and Universal Coordinated Time (UTC).

        - getUTCDate (required):
            Gets the day-of-the-month, using Universal Coordinated
            Time (UTC).

        - getUTCDay (required):
            Gets the day of the week using Universal Coordinated Time
            (UTC).

        - getUTCFullYear (required):
            Gets the year using Universal Coordinated Time (UTC).

        - getUTCHours (required):
            Gets the hours value in a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMilliseconds (required):
            Gets the milliseconds of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMinutes (required):
            Gets the minutes of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMonth (required):
            Gets the month of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCSeconds (required):
            Gets the seconds of a Date object using Universal
            Coordinated Time (UTC).

        - getVarDate (required)

        - setDate (required):
            Sets the numeric day-of-the-month value of the Date object
            using local time. @,param,date, ,A numeric value equal to
            the day of the month.

        - setFullYear (required):
            Sets the year of the Date object using local time.
            @,param,year, ,A numeric value for the year.
            @,param,month, ,A zero-based numeric value for the month
            (0 for January, 11 for December). Must be specified if
            numDate is specified. @,param,date, ,A numeric value equal
            for the day of the month.

        - setHours (required):
            Sets the hour value in the Date object using local time.
            @,param,hours, ,A numeric value equal to the hours value.
            @,param,min, ,A numeric value equal to the minutes value.
            @,param,sec, ,A numeric value equal to the seconds value.
            @,param,ms, ,A numeric value equal to the milliseconds
            value.

        - setMilliseconds (required):
            Sets the milliseconds value in the Date object using local
            time. @,param,ms, ,A numeric value equal to the
            millisecond value.

        - setMinutes (required):
            Sets the minutes value in the Date object using local
            time. @,param,min, ,A numeric value equal to the minutes
            value. @,param,sec, ,A numeric value equal to the seconds
            value. @,param,ms, ,A numeric value equal to the
            milliseconds value.

        - setMonth (required):
            Sets the month value in the Date object using local time.
            @,param,month, ,A numeric value equal to the month. The
            value for January is 0, and other month values follow
            consecutively. @,param,date, ,A numeric value representing
            the day of the month. If this value is not supplied, the
            value from a call to the getDate method is used.

        - setSeconds (required):
            Sets the seconds value in the Date object using local
            time. @,param,sec, ,A numeric value equal to the seconds
            value. @,param,ms, ,A numeric value equal to the
            milliseconds value.

        - setTime (required):
            Sets the date and time value in the Date object.
            @,param,time, ,A numeric value representing the number of
            elapsed milliseconds since midnight, January 1, 1970 GMT.

        - setUTCDate (required):
            Sets the numeric day of the month in the Date object using
            Universal Coordinated Time (UTC). @,param,date, ,A numeric
            value equal to the day of the month.

        - setUTCFullYear (required):
            Sets the year value in the Date object using Universal
            Coordinated Time (UTC). @,param,year, ,A numeric value
            equal to the year. @,param,month, ,A numeric value equal
            to the month. The value for January is 0, and other month
            values follow consecutively. Must be supplied if numDate
            is supplied. @,param,date, ,A numeric value equal to the
            day of the month.

        - setUTCHours (required):
            Sets the hours value in the Date object using Universal
            Coordinated Time (UTC). @,param,hours, ,A numeric value
            equal to the hours value. @,param,min, ,A numeric value
            equal to the minutes value. @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - setUTCMilliseconds (required):
            Sets the milliseconds value in the Date object using
            Universal Coordinated Time (UTC). @,param,ms, ,A numeric
            value equal to the millisecond value.

        - setUTCMinutes (required):
            Sets the minutes value in the Date object using Universal
            Coordinated Time (UTC). @,param,min, ,A numeric value
            equal to the minutes value. @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - setUTCMonth (required):
            Sets the month value in the Date object using Universal
            Coordinated Time (UTC). @,param,month, ,A numeric value
            equal to the month. The value for January is 0, and other
            month values follow consecutively. @,param,date, ,A
            numeric value representing the day of the month. If it is
            not supplied, the value from a call to the getUTCDate
            method is used.

        - setUTCSeconds (required):
            Sets the seconds value in the Date object using Universal
            Coordinated Time (UTC). @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - toDateString (required):
            Returns a date as a string value.

        - toISOString (required):
            Returns a date as a string value in ISO format.

        - toJSON (required):
            Used by the JSON.stringify method to enable the
            transformation of an object's data for JavaScript Object
            Notation (JSON) serialization.

        - toLocaleDateString (dict; required):
            Returns a date as a string value appropriate to the host
            environment's current locale.   Converts a date to a
            string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleDateString` is a dict with keys:


        - toLocaleString (dict; optional):
            Returns a value as a string value appropriate to the host
            environment's current locale.   Converts a date and time
            to a string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleString` is a dict with keys:


        - toLocaleTimeString (dict; required):
            Returns a time as a string value appropriate to the host
            environment's current locale.   Converts a time to a
            string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleTimeString` is a dict with keys:


        - toString (optional):
            Returns a string representation of a date. The format of
            the string depends on the locale.

        - toTimeString (required):
            Returns a time as a string value.

        - toUTCString (required):
            Returns a date converted to a string using Universal
            Coordinated Time (UTC).

        - valueOf (optional):
            Returns the stored time value in milliseconds since
            midnight, January 1, 1970 UTC.

    - minDate (dict; optional):
        The earliest date that can be selected (this should be a
        native Date object - e.g. new Date() or moment().toDate()).

        `minDate` is a dict with keys:

        - __@toPrimitive@4735 (dict; required):
            Converts a Date object to a string.   Converts a Date
            object to a number.   Converts a Date object to a string
            or number. @,param,hint, ,The strings \"number\",
            \"string\", or \"default\" to specify what primitive to
            return. @,throws,{TypeError} If 'hint' was given something
            other than \"number\", \"string\", or \"default\".
            @,returns,A number if 'hint' was \"number\", a string if
            'hint' was \"string\" or \"default\".

            `__@toPrimitive@4735` is a dict with keys:


        - getDate (required):
            Gets the day-of-the-month, using local time.

        - getDay (required):
            Gets the day of the week, using local time.

        - getFullYear (required):
            Gets the year, using local time.

        - getHours (required):
            Gets the hours in a date, using local time.

        - getMilliseconds (required):
            Gets the milliseconds of a Date, using local time.

        - getMinutes (required):
            Gets the minutes of a Date object, using local time.

        - getMonth (required):
            Gets the month, using local time.

        - getSeconds (required):
            Gets the seconds of a Date object, using local time.

        - getTime (required):
            Gets the time value in milliseconds.

        - getTimezoneOffset (required):
            Gets the difference in minutes between the time on the
            local computer and Universal Coordinated Time (UTC).

        - getUTCDate (required):
            Gets the day-of-the-month, using Universal Coordinated
            Time (UTC).

        - getUTCDay (required):
            Gets the day of the week using Universal Coordinated Time
            (UTC).

        - getUTCFullYear (required):
            Gets the year using Universal Coordinated Time (UTC).

        - getUTCHours (required):
            Gets the hours value in a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMilliseconds (required):
            Gets the milliseconds of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMinutes (required):
            Gets the minutes of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCMonth (required):
            Gets the month of a Date object using Universal
            Coordinated Time (UTC).

        - getUTCSeconds (required):
            Gets the seconds of a Date object using Universal
            Coordinated Time (UTC).

        - getVarDate (required)

        - setDate (required):
            Sets the numeric day-of-the-month value of the Date object
            using local time. @,param,date, ,A numeric value equal to
            the day of the month.

        - setFullYear (required):
            Sets the year of the Date object using local time.
            @,param,year, ,A numeric value for the year.
            @,param,month, ,A zero-based numeric value for the month
            (0 for January, 11 for December). Must be specified if
            numDate is specified. @,param,date, ,A numeric value equal
            for the day of the month.

        - setHours (required):
            Sets the hour value in the Date object using local time.
            @,param,hours, ,A numeric value equal to the hours value.
            @,param,min, ,A numeric value equal to the minutes value.
            @,param,sec, ,A numeric value equal to the seconds value.
            @,param,ms, ,A numeric value equal to the milliseconds
            value.

        - setMilliseconds (required):
            Sets the milliseconds value in the Date object using local
            time. @,param,ms, ,A numeric value equal to the
            millisecond value.

        - setMinutes (required):
            Sets the minutes value in the Date object using local
            time. @,param,min, ,A numeric value equal to the minutes
            value. @,param,sec, ,A numeric value equal to the seconds
            value. @,param,ms, ,A numeric value equal to the
            milliseconds value.

        - setMonth (required):
            Sets the month value in the Date object using local time.
            @,param,month, ,A numeric value equal to the month. The
            value for January is 0, and other month values follow
            consecutively. @,param,date, ,A numeric value representing
            the day of the month. If this value is not supplied, the
            value from a call to the getDate method is used.

        - setSeconds (required):
            Sets the seconds value in the Date object using local
            time. @,param,sec, ,A numeric value equal to the seconds
            value. @,param,ms, ,A numeric value equal to the
            milliseconds value.

        - setTime (required):
            Sets the date and time value in the Date object.
            @,param,time, ,A numeric value representing the number of
            elapsed milliseconds since midnight, January 1, 1970 GMT.

        - setUTCDate (required):
            Sets the numeric day of the month in the Date object using
            Universal Coordinated Time (UTC). @,param,date, ,A numeric
            value equal to the day of the month.

        - setUTCFullYear (required):
            Sets the year value in the Date object using Universal
            Coordinated Time (UTC). @,param,year, ,A numeric value
            equal to the year. @,param,month, ,A numeric value equal
            to the month. The value for January is 0, and other month
            values follow consecutively. Must be supplied if numDate
            is supplied. @,param,date, ,A numeric value equal to the
            day of the month.

        - setUTCHours (required):
            Sets the hours value in the Date object using Universal
            Coordinated Time (UTC). @,param,hours, ,A numeric value
            equal to the hours value. @,param,min, ,A numeric value
            equal to the minutes value. @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - setUTCMilliseconds (required):
            Sets the milliseconds value in the Date object using
            Universal Coordinated Time (UTC). @,param,ms, ,A numeric
            value equal to the millisecond value.

        - setUTCMinutes (required):
            Sets the minutes value in the Date object using Universal
            Coordinated Time (UTC). @,param,min, ,A numeric value
            equal to the minutes value. @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - setUTCMonth (required):
            Sets the month value in the Date object using Universal
            Coordinated Time (UTC). @,param,month, ,A numeric value
            equal to the month. The value for January is 0, and other
            month values follow consecutively. @,param,date, ,A
            numeric value representing the day of the month. If it is
            not supplied, the value from a call to the getUTCDate
            method is used.

        - setUTCSeconds (required):
            Sets the seconds value in the Date object using Universal
            Coordinated Time (UTC). @,param,sec, ,A numeric value
            equal to the seconds value. @,param,ms, ,A numeric value
            equal to the milliseconds value.

        - toDateString (required):
            Returns a date as a string value.

        - toISOString (required):
            Returns a date as a string value in ISO format.

        - toJSON (required):
            Used by the JSON.stringify method to enable the
            transformation of an object's data for JavaScript Object
            Notation (JSON) serialization.

        - toLocaleDateString (dict; required):
            Returns a date as a string value appropriate to the host
            environment's current locale.   Converts a date to a
            string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleDateString` is a dict with keys:


        - toLocaleString (dict; optional):
            Returns a value as a string value appropriate to the host
            environment's current locale.   Converts a date and time
            to a string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleString` is a dict with keys:


        - toLocaleTimeString (dict; required):
            Returns a time as a string value appropriate to the host
            environment's current locale.   Converts a time to a
            string by using the current or specified locale.
            @,param,locales, ,A locale string or array of locale
            strings that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.
            @,param,locales, ,A locale string, array of locale
            strings, Intl.Locale object, or array of Intl.Locale
            objects that contain one or more language or locale tags.
            If you include more than one locale string, list them in
            descending order of priority so that the first entry is
            the preferred locale. If you omit this parameter, the
            default locale of the JavaScript runtime is used.
            @,param,options, ,An object that contains one or more
            properties that specify comparison options.

            `toLocaleTimeString` is a dict with keys:


        - toString (optional):
            Returns a string representation of a date. The format of
            the string depends on the locale.

        - toTimeString (required):
            Returns a time as a string value.

        - toUTCString (required):
            Returns a date converted to a string using Universal
            Coordinated Time (UTC).

        - valueOf (optional):
            Returns the stored time value in milliseconds since
            midnight, January 1, 1970 UTC.

    - numberOfMonths (number; optional):
        Number of visible calendars.

    - onClose (optional):
        Callback function for when the picker is hidden.

    - onDraw (optional):
        Callback function for when the picker draws a new month.

    - onOpen (optional):
        Callback function for when the picker becomes visible.

    - onSelect (optional):
        Callback function for when a date is selected.

    - parse (optional):
        Function which will be used for parsing input string and
        getting a date object from it. This function will take
        precedence over moment.

    - pickWholeWeek (boolean; optional):
        Select a whole week instead of a day (default False).

    - position (string; optional):
        Preferred position of the datepicker relative to the form
        field (e.g. 'top right'). Automatic adjustment may occur to
        avoid displaying outside the viewport. Default: 'bottom left'.

    - reposition (boolean; optional):
        Can be set to False to not reposition the datepicker within
        the viewport, forcing it to take the configured position.
        Default: True.

    - setDefaultDate (boolean; optional):
        Make the defaultDate the initial selected value.

    - showDaysInNextAndPreviousMonths (boolean; optional):
        Render days of the calendar grid that fall in the next or
        previous months to the current month instead of rendering an
        empty table cell. Default: False.

    - showMonthAfterYear (boolean; optional):
        Render the month after the year in the title. Default: False.

    - showWeekNumber (boolean; optional):
        Show the ISO week number at the head of the row. Default:
        False.

    - theme (string; optional):
        Define a class name that can be used as a hook for styling
        different themes. Default: None.

    - toString (optional):
        Function which will be used for formatting date object to
        string. This function will take precedence over moment.

    - trigger (dict; optional):
        Use a different element to trigger opening the datepicker.
        Default: field element.

        `trigger` is a dict with keys:

        - ATTRIBUTE_NODE (number; required)

        - CDATA_SECTION_NODE (number; required):
            node is a CDATASection node.

        - COMMENT_NODE (number; required):
            node is a Comment node.

        - DOCUMENT_FRAGMENT_NODE (number; required):
            node is a DocumentFragment node.

        - DOCUMENT_NODE (number; required):
            node is a document.

        - DOCUMENT_POSITION_CONTAINED_BY (number; required):
            Set when other is a descendant of node.

        - DOCUMENT_POSITION_CONTAINS (number; required):
            Set when other is an ancestor of node.

        - DOCUMENT_POSITION_DISCONNECTED (number; required):
            Set when node and other are not in the same tree.

        - DOCUMENT_POSITION_FOLLOWING (number; required):
            Set when other is following node.

        - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

        - DOCUMENT_POSITION_PRECEDING (number; required):
            Set when other is preceding node.

        - DOCUMENT_TYPE_NODE (number; required):
            node is a doctype.

        - ELEMENT_NODE (number; required):
            node is an element.

        - ENTITY_NODE (number; required)

        - ENTITY_REFERENCE_NODE (number; required)

        - NOTATION_NODE (number; required)

        - PROCESSING_INSTRUCTION_NODE (number; required):
            node is a ProcessingInstruction node.

        - TEXT_NODE (number; required):
            node is a Text node.

        - accessKey (string; required)

        - accessKeyLabel (string; required)

        - addEventListener (required)

        - after (required):
            Inserts nodes just after node, while replacing strings in
            nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - animate (required)

        - append (required):
            Inserts nodes after the last child of node, while
            replacing strings in nodes with equivalent Text nodes.
            Throws a \"HierarchyRequestError\" DOMException if the
            constraints of the node tree are violated.

        - appendChild (required)

        - ariaAtomic (string; required)

        - ariaAutoComplete (string; required)

        - ariaBusy (string; required)

        - ariaChecked (string; required)

        - ariaColCount (string; required)

        - ariaColIndex (string; required)

        - ariaColIndexText (string; required)

        - ariaColSpan (string; required)

        - ariaCurrent (string; required)

        - ariaDisabled (string; required)

        - ariaExpanded (string; required)

        - ariaHasPopup (string; required)

        - ariaHidden (string; required)

        - ariaInvalid (string; required)

        - ariaKeyShortcuts (string; required)

        - ariaLabel (string; required)

        - ariaLevel (string; required)

        - ariaLive (string; required)

        - ariaModal (string; required)

        - ariaMultiLine (string; required)

        - ariaMultiSelectable (string; required)

        - ariaOrientation (string; required)

        - ariaPlaceholder (string; required)

        - ariaPosInSet (string; required)

        - ariaPressed (string; required)

        - ariaReadOnly (string; required)

        - ariaRequired (string; required)

        - ariaRoleDescription (string; required)

        - ariaRowCount (string; required)

        - ariaRowIndex (string; required)

        - ariaRowIndexText (string; required)

        - ariaRowSpan (string; required)

        - ariaSelected (string; required)

        - ariaSetSize (string; required)

        - ariaSort (string; required)

        - ariaValueMax (string; required)

        - ariaValueMin (string; required)

        - ariaValueNow (string; required)

        - ariaValueText (string; required)

        - assignedSlot (dict; required)

            `assignedSlot` is a dict with keys:

            - ATTRIBUTE_NODE (number; required)

            - CDATA_SECTION_NODE (number; required):
                node is a CDATASection node.

            - COMMENT_NODE (number; required):
                node is a Comment node.

            - DOCUMENT_FRAGMENT_NODE (number; required):
                node is a DocumentFragment node.

            - DOCUMENT_NODE (number; required):
                node is a document.

            - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                Set when other is a descendant of node.

            - DOCUMENT_POSITION_CONTAINS (number; required):
                Set when other is an ancestor of node.

            - DOCUMENT_POSITION_DISCONNECTED (number; required):
                Set when node and other are not in the same tree.

            - DOCUMENT_POSITION_FOLLOWING (number; required):
                Set when other is following node.

            - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

            - DOCUMENT_POSITION_PRECEDING (number; required):
                Set when other is preceding node.

            - DOCUMENT_TYPE_NODE (number; required):
                node is a doctype.

            - ELEMENT_NODE (number; required):
                node is an element.

            - ENTITY_NODE (number; required)

            - ENTITY_REFERENCE_NODE (number; required)

            - NOTATION_NODE (number; required)

            - PROCESSING_INSTRUCTION_NODE (number; required):
                node is a ProcessingInstruction node.

            - TEXT_NODE (number; required):
                node is a Text node.

            - accessKey (string; required)

            - accessKeyLabel (string; required)

            - addEventListener (required)

            - after (required):
                Inserts nodes just after node, while replacing strings
                in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - animate (required)

            - append (required):
                Inserts nodes after the last child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - appendChild (required)

            - ariaAtomic (string; required)

            - ariaAutoComplete (string; required)

            - ariaBusy (string; required)

            - ariaChecked (string; required)

            - ariaColCount (string; required)

            - ariaColIndex (string; required)

            - ariaColIndexText (string; required)

            - ariaColSpan (string; required)

            - ariaCurrent (string; required)

            - ariaDisabled (string; required)

            - ariaExpanded (string; required)

            - ariaHasPopup (string; required)

            - ariaHidden (string; required)

            - ariaInvalid (string; required)

            - ariaKeyShortcuts (string; required)

            - ariaLabel (string; required)

            - ariaLevel (string; required)

            - ariaLive (string; required)

            - ariaModal (string; required)

            - ariaMultiLine (string; required)

            - ariaMultiSelectable (string; required)

            - ariaOrientation (string; required)

            - ariaPlaceholder (string; required)

            - ariaPosInSet (string; required)

            - ariaPressed (string; required)

            - ariaReadOnly (string; required)

            - ariaRequired (string; required)

            - ariaRoleDescription (string; required)

            - ariaRowCount (string; required)

            - ariaRowIndex (string; required)

            - ariaRowIndexText (string; required)

            - ariaRowSpan (string; required)

            - ariaSelected (string; required)

            - ariaSetSize (string; required)

            - ariaSort (string; required)

            - ariaValueMax (string; required)

            - ariaValueMin (string; required)

            - ariaValueNow (string; required)

            - ariaValueText (string; required)

            - assign (required)

            - assignedElements (required)

            - assignedNodes (required)

            - assignedSlot (boolean | number | string | dict | list; required)

            - attachInternals (required)

            - attachShadow (required):
                Creates a shadow root for element and returns it.

            - attributes (dict; required)

                `attributes` is a dict with strings as keys and values
                of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

            - autocapitalize (string; required)

            - autofocus (boolean; required)

            - baseURI (string; required):
                Returns node's node document's document base URL.

            - before (required):
                Inserts nodes just before node, while replacing
                strings in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - blur (required)

            - childElementCount (number; required)

            - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                Returns the children.

            - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                Returns the child elements.

            - classList (dict with strings as keys and values of type string; required):
                Allows for manipulation of element's class content
                attribute as a set of whitespace-separated tokens
                through a DOMTokenList object.

            - className (string; required):
                Returns the value of element's class content
                attribute. Can be set to change it.

            - click (required)

            - clientHeight (number; required)

            - clientLeft (number; required)

            - clientTop (number; required)

            - clientWidth (number; required)

            - cloneNode (required):
                Returns a copy of node. If deep is True, the copy also
                includes the node's descendants.

            - closest (dict; required):
                Returns the first (starting at element) inclusive
                ancestor that matches selectors, and None otherwise.

                `closest` is a dict with keys:


            - compareDocumentPosition (required):
                Returns a bitmask indicating the position of other
                relative to node.

            - contains (required):
                Returns True if other is an inclusive descendant of
                node, and False otherwise.

            - contentEditable (string; required)

            - dataset (dict with strings as keys and values of type string; required)

            - dir (string; required)

            - dispatchEvent (required):
                Dispatches a synthetic event event to target and
                returns True if either event's cancelable attribute
                value is False or its preventDefault() method was not
                invoked, and False otherwise.

            - draggable (boolean; required)

            - enterKeyHint (string; required)

            - firstChild (boolean | number | string | dict | list; required):
                Returns the first child.

            - firstElementChild (a list of or a singular dash component, string or number; required):
                Returns the first child that is an element, and None
                otherwise.

            - focus (required)

            - getAnimations (required)

            - getAttribute (required):
                Returns element's first attribute whose qualified name
                is qualifiedName, and None if there is no such
                attribute otherwise.

            - getAttributeNS (required):
                Returns element's attribute whose namespace is
                namespace and local name is localName, and None if
                there is no such attribute otherwise.

            - getAttributeNames (required):
                Returns the qualified names of all element's
                attributes. Can contain duplicates.

            - getAttributeNode (required)

            - getAttributeNodeNS (required)

            - getBoundingClientRect (required)

            - getClientRects (required)

            - getElementsByClassName (required):
                Returns a HTMLCollection of the elements in the object
                on which the method was invoked (a document or an
                element) that have all the classes given by
                classNames. The classNames argument is interpreted as
                a space-separated list of classes.

            - getElementsByTagName (dict; required)

                `getElementsByTagName` is a dict with keys:


            - getElementsByTagNameNS (dict; required)

                `getElementsByTagNameNS` is a dict with keys:


            - getRootNode (required):
                Returns node's root.

            - hasAttribute (required):
                Returns True if element has an attribute whose
                qualified name is qualifiedName, and False otherwise.

            - hasAttributeNS (required):
                Returns True if element has an attribute whose
                namespace is namespace and local name is localName.

            - hasAttributes (required):
                Returns True if element has attributes, and False
                otherwise.

            - hasChildNodes (required):
                Returns whether node has children.

            - hasPointerCapture (required)

            - hidden (boolean; required)

            - id (string; required):
                Returns the value of element's id content attribute.
                Can be set to change it.

            - inert (boolean; required)

            - innerHTML (string; required)

            - innerText (string; required)

            - inputMode (string; required)

            - insertAdjacentElement (required)

            - insertAdjacentHTML (required)

            - insertAdjacentText (required)

            - insertBefore (required)

            - isConnected (boolean; required):
                Returns True if node is connected and False otherwise.

            - isContentEditable (boolean; required)

            - isDefaultNamespace (required)

            - isEqualNode (required):
                Returns whether node and otherNode have the same
                properties.

            - isSameNode (required)

            - lang (string; required)

            - lastChild (boolean | number | string | dict | list; required):
                Returns the last child.

            - lastElementChild (a list of or a singular dash component, string or number; required):
                Returns the last child that is an element, and None
                otherwise.

            - localName (string; required):
                Returns the local name.

            - lookupNamespaceURI (required)

            - lookupPrefix (required)

            - matches (required):
                Returns True if matching selectors against element's
                root yields element, and False otherwise.

            - name (string; required)

            - namespaceURI (string; required):
                Returns the namespace.

            - nextElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first following sibling that is an
                element, and None otherwise.

            - nextSibling (boolean | number | string | dict | list; required):
                Returns the next sibling.

            - nodeName (string; required):
                Returns a string appropriate for the type of node.

            - nodeType (number; required):
                Returns the type of node.

            - nodeValue (string; required)

            - nonce (string; optional)

            - normalize (required):
                Removes empty exclusive Text nodes and concatenates
                the data of remaining contiguous exclusive Text nodes
                into the first of their nodes.

            - offsetHeight (number; required)

            - offsetLeft (number; required)

            - offsetParent (a list of or a singular dash component, string or number; required)

            - offsetTop (number; required)

            - offsetWidth (number; required)

            - onabort (required):
                Fires when the user aborts the download. @,param,ev,
                ,The event.

            - onanimationcancel (required)

            - onanimationend (required)

            - onanimationiteration (required)

            - onanimationstart (required)

            - onauxclick (required)

            - onbeforeinput (required)

            - onblur (required):
                Fires when the object loses the input focus.
                @,param,ev, ,The focus event.

            - oncancel (required)

            - oncanplay (required):
                Occurs when playback is possible, but would require
                further buffering. @,param,ev, ,The event.

            - oncanplaythrough (required)

            - onchange (required):
                Fires when the contents of the object or selection
                have changed. @,param,ev, ,The event.

            - onclick (required):
                Fires when the user clicks the left mouse button on
                the object @,param,ev, ,The mouse event.

            - onclose (required)

            - oncontextmenu (required):
                Fires when the user clicks the right mouse button in
                the client area, opening the context menu. @,param,ev,
                ,The mouse event.

            - oncopy (required)

            - oncuechange (required)

            - oncut (required)

            - ondblclick (required):
                Fires when the user double-clicks the object.
                @,param,ev, ,The mouse event.

            - ondrag (required):
                Fires on the source object continuously during a drag
                operation. @,param,ev, ,The event.

            - ondragend (required):
                Fires on the source object when the user releases the
                mouse at the close of a drag operation. @,param,ev,
                ,The event.

            - ondragenter (required):
                Fires on the target element when the user drags the
                object to a valid drop target. @,param,ev, ,The drag
                event.

            - ondragleave (required):
                Fires on the target object when the user moves the
                mouse out of a valid drop target during a drag
                operation. @,param,ev, ,The drag event.

            - ondragover (required):
                Fires on the target element continuously while the
                user drags the object over a valid drop target.
                @,param,ev, ,The event.

            - ondragstart (required):
                Fires on the source object when the user starts to
                drag a text selection or selected object. @,param,ev,
                ,The event.

            - ondrop (required)

            - ondurationchange (required):
                Occurs when the duration attribute is updated.
                @,param,ev, ,The event.

            - onemptied (required):
                Occurs when the media element is reset to its initial
                state. @,param,ev, ,The event.

            - onended (required):
                Occurs when the end of playback is reached.
                @,param,ev, ,The event.

            - onerror (dict; required):
                Fires when an error occurs during object loading.
                @,param,ev, ,The event.

                `onerror` is a dict with keys:


            - onfocus (required):
                Fires when the object receives focus. @,param,ev, ,The
                event.

            - onformdata (required)

            - onfullscreenchange (required)

            - onfullscreenerror (required)

            - ongotpointercapture (required)

            - oninput (required)

            - oninvalid (required)

            - onkeydown (required):
                Fires when the user presses a key. @,param,ev, ,The
                keyboard event.

            - onkeypress (required):
                Fires when the user presses an alphanumeric key.
                @,param,ev, ,The event. @,deprecated.

            - onkeyup (required):
                Fires when the user releases a key. @,param,ev, ,The
                keyboard event.

            - onload (required):
                Fires immediately after the browser loads the object.
                @,param,ev, ,The event.

            - onloadeddata (required):
                Occurs when media data is loaded at the current
                playback position. @,param,ev, ,The event.

            - onloadedmetadata (required):
                Occurs when the duration and dimensions of the media
                have been determined. @,param,ev, ,The event.

            - onloadstart (required):
                Occurs when Internet Explorer begins looking for media
                data. @,param,ev, ,The event.

            - onlostpointercapture (required)

            - onmousedown (required):
                Fires when the user clicks the object with either
                mouse button. @,param,ev, ,The mouse event.

            - onmouseenter (required)

            - onmouseleave (required)

            - onmousemove (required):
                Fires when the user moves the mouse over the object.
                @,param,ev, ,The mouse event.

            - onmouseout (required):
                Fires when the user moves the mouse pointer outside
                the boundaries of the object. @,param,ev, ,The mouse
                event.

            - onmouseover (required):
                Fires when the user moves the mouse pointer into the
                object. @,param,ev, ,The mouse event.

            - onmouseup (required):
                Fires when the user releases a mouse button while the
                mouse is over the object. @,param,ev, ,The mouse
                event.

            - onpaste (required)

            - onpause (required):
                Occurs when playback is paused. @,param,ev, ,The
                event.

            - onplay (required):
                Occurs when the play method is requested. @,param,ev,
                ,The event.

            - onplaying (required):
                Occurs when the audio or video has started playing.
                @,param,ev, ,The event.

            - onpointercancel (required)

            - onpointerdown (required)

            - onpointerenter (required)

            - onpointerleave (required)

            - onpointermove (required)

            - onpointerout (required)

            - onpointerover (required)

            - onpointerup (required)

            - onprogress (required):
                Occurs to indicate progress while downloading media
                data. @,param,ev, ,The event.

            - onratechange (required):
                Occurs when the playback rate is increased or
                decreased. @,param,ev, ,The event.

            - onreset (required):
                Fires when the user resets a form. @,param,ev, ,The
                event.

            - onresize (required)

            - onscroll (required):
                Fires when the user repositions the scroll box in the
                scroll bar on the object. @,param,ev, ,The event.

            - onsecuritypolicyviolation (required)

            - onseeked (required):
                Occurs when the seek operation ends. @,param,ev, ,The
                event.

            - onseeking (required):
                Occurs when the current playback position is moved.
                @,param,ev, ,The event.

            - onselect (required):
                Fires when the current selection changes. @,param,ev,
                ,The event.

            - onselectionchange (required)

            - onselectstart (required)

            - onslotchange (required)

            - onstalled (required):
                Occurs when the download has stopped. @,param,ev, ,The
                event.

            - onsubmit (required)

            - onsuspend (required):
                Occurs if the load operation has been intentionally
                halted. @,param,ev, ,The event.

            - ontimeupdate (required):
                Occurs to indicate the current playback position.
                @,param,ev, ,The event.

            - ontoggle (required)

            - ontouchcancel (optional)

            - ontouchend (optional)

            - ontouchmove (optional)

            - ontouchstart (optional)

            - ontransitioncancel (required)

            - ontransitionend (required)

            - ontransitionrun (required)

            - ontransitionstart (required)

            - onvolumechange (required):
                Occurs when the volume is changed, or playback is
                muted or unmuted. @,param,ev, ,The event.

            - onwaiting (required):
                Occurs when playback stops because the next frame of a
                video resource is not available. @,param,ev, ,The
                event.

            - onwebkitanimationend (required)

            - onwebkitanimationiteration (required)

            - onwebkitanimationstart (required)

            - onwebkittransitionend (required)

            - onwheel (required)

            - outerHTML (string; required)

            - outerText (string; required)

            - ownerDocument (boolean | number | string | dict | list; required)

            - parentElement (boolean | number | string | dict | list; required):
                Returns the parent element.

            - parentNode (boolean | number | string | dict | list; required):
                Returns the parent.

            - part (dict with strings as keys and values of type string; required)

            - prefix (string; required):
                Returns the namespace prefix.

            - prepend (required):
                Inserts nodes before the first child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - previousElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first preceding sibling that is an
                element, and None otherwise.

            - previousSibling (boolean | number | string | dict | list; required):
                Returns the previous sibling.

            - querySelector (dict; required):
                Returns the first element that is a descendant of node
                that matches selectors.

                `querySelector` is a dict with keys:


            - querySelectorAll (dict; required):
                Returns all element descendants of node that match
                selectors.

                `querySelectorAll` is a dict with keys:


            - releasePointerCapture (required)

            - remove (required):
                Removes node.

            - removeAttribute (required):
                Removes element's first attribute whose qualified name
                is qualifiedName.

            - removeAttributeNS (required):
                Removes element's attribute whose namespace is
                namespace and local name is localName.

            - removeAttributeNode (required)

            - removeChild (required)

            - removeEventListener (required)

            - replaceChild (required)

            - replaceChildren (required):
                Replace all children of node with nodes, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - replaceWith (required):
                Replaces node with nodes, while replacing strings in
                nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - requestFullscreen (required):
                Displays element fullscreen and resolves promise when
                done.  When supplied, options's navigationUI member
                indicates whether showing navigation UI while in
                fullscreen is preferred or not. If set to \"show\",
                navigation simplicity is preferred over screen space,
                and if set to \"hide\", more screen space is
                preferred. User agents are always free to honor user
                preference over the application's. The default value
                \"auto\" indicates no application preference.

            - requestPointerLock (required)

            - role (string; required)

            - scroll (dict; required)

                `scroll` is a dict with keys:


            - scrollBy (dict; required)

                `scrollBy` is a dict with keys:


            - scrollHeight (number; required)

            - scrollIntoView (required)

            - scrollLeft (number; required)

            - scrollTo (dict; required)

                `scrollTo` is a dict with keys:


            - scrollTop (number; required)

            - scrollWidth (number; required)

            - setAttribute (required):
                Sets the value of element's first attribute whose
                qualified name is qualifiedName to value.

            - setAttributeNS (required):
                Sets the value of element's attribute whose namespace
                is namespace and local name is localName to value.

            - setAttributeNode (required)

            - setAttributeNodeNS (required)

            - setPointerCapture (required)

            - shadowRoot (boolean | number | string | dict | list; required):
                Returns element's shadow root, if any, and if shadow
                root's mode is \"open\", and None otherwise.

            - slot (string; required):
                Returns the value of element's slot content attribute.
                Can be set to change it.

            - spellcheck (boolean; required)

            - style (dict with strings as keys and values of type string; required)

            - tabIndex (number; required)

            - tagName (string; required):
                Returns the HTML-uppercased qualified name.

            - textContent (string; required)

            - title (string; required)

            - toggleAttribute (required):
                If force is not given, \"toggles\" qualifiedName,
                removing it if it is present and adding it if it is
                not present. If force is True, adds qualifiedName. If
                force is False, removes qualifiedName.  Returns True
                if qualifiedName is now present, and False otherwise.

            - translate (boolean; required)

            - webkitMatchesSelector (required)

        - attachInternals (required)

        - attachShadow (required):
            Creates a shadow root for element and returns it.

        - attributes (dict; required)

            `attributes` is a dict with strings as keys and values of
            type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

        - autocapitalize (string; required)

        - autofocus (boolean; required)

        - baseURI (string; required):
            Returns node's node document's document base URL.

        - before (required):
            Inserts nodes just before node, while replacing strings in
            nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - blur (required)

        - childElementCount (number; required)

        - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
            Returns the children.

        - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
            Returns the child elements.

        - classList (dict with strings as keys and values of type string; required):
            Allows for manipulation of element's class content
            attribute as a set of whitespace-separated tokens through
            a DOMTokenList object.

        - className (string; required):
            Returns the value of element's class content attribute.
            Can be set to change it.

        - click (required)

        - clientHeight (number; required)

        - clientLeft (number; required)

        - clientTop (number; required)

        - clientWidth (number; required)

        - cloneNode (required):
            Returns a copy of node. If deep is True, the copy also
            includes the node's descendants.

        - closest (dict; required):
            Returns the first (starting at element) inclusive ancestor
            that matches selectors, and None otherwise.

            `closest` is a dict with keys:


        - compareDocumentPosition (required):
            Returns a bitmask indicating the position of other
            relative to node.

        - contains (required):
            Returns True if other is an inclusive descendant of node,
            and False otherwise.

        - contentEditable (string; required)

        - dataset (dict with strings as keys and values of type string; required)

        - dir (string; required)

        - dispatchEvent (required):
            Dispatches a synthetic event event to target and returns
            True if either event's cancelable attribute value is False
            or its preventDefault() method was not invoked, and False
            otherwise.

        - draggable (boolean; required)

        - enterKeyHint (string; required)

        - firstChild (boolean | number | string | dict | list; required):
            Returns the first child.

        - firstElementChild (a list of or a singular dash component, string or number; required):
            Returns the first child that is an element, and None
            otherwise.

        - focus (required)

        - getAnimations (required)

        - getAttribute (required):
            Returns element's first attribute whose qualified name is
            qualifiedName, and None if there is no such attribute
            otherwise.

        - getAttributeNS (required):
            Returns element's attribute whose namespace is namespace
            and local name is localName, and None if there is no such
            attribute otherwise.

        - getAttributeNames (required):
            Returns the qualified names of all element's attributes.
            Can contain duplicates.

        - getAttributeNode (required)

        - getAttributeNodeNS (required)

        - getBoundingClientRect (required)

        - getClientRects (required)

        - getElementsByClassName (required):
            Returns a HTMLCollection of the elements in the object on
            which the method was invoked (a document or an element)
            that have all the classes given by classNames. The
            classNames argument is interpreted as a space-separated
            list of classes.

        - getElementsByTagName (dict; required)

            `getElementsByTagName` is a dict with keys:


        - getElementsByTagNameNS (dict; required)

            `getElementsByTagNameNS` is a dict with keys:


        - getRootNode (required):
            Returns node's root.

        - hasAttribute (required):
            Returns True if element has an attribute whose qualified
            name is qualifiedName, and False otherwise.

        - hasAttributeNS (required):
            Returns True if element has an attribute whose namespace
            is namespace and local name is localName.

        - hasAttributes (required):
            Returns True if element has attributes, and False
            otherwise.

        - hasChildNodes (required):
            Returns whether node has children.

        - hasPointerCapture (required)

        - hidden (boolean; required)

        - id (string; required):
            Returns the value of element's id content attribute. Can
            be set to change it.

        - inert (boolean; required)

        - innerHTML (string; required)

        - innerText (string; required)

        - inputMode (string; required)

        - insertAdjacentElement (required)

        - insertAdjacentHTML (required)

        - insertAdjacentText (required)

        - insertBefore (required)

        - isConnected (boolean; required):
            Returns True if node is connected and False otherwise.

        - isContentEditable (boolean; required)

        - isDefaultNamespace (required)

        - isEqualNode (required):
            Returns whether node and otherNode have the same
            properties.

        - isSameNode (required)

        - lang (string; required)

        - lastChild (boolean | number | string | dict | list; required):
            Returns the last child.

        - lastElementChild (a list of or a singular dash component, string or number; required):
            Returns the last child that is an element, and None
            otherwise.

        - localName (string; required):
            Returns the local name.

        - lookupNamespaceURI (required)

        - lookupPrefix (required)

        - matches (required):
            Returns True if matching selectors against element's root
            yields element, and False otherwise.

        - namespaceURI (string; required):
            Returns the namespace.

        - nextElementSibling (a list of or a singular dash component, string or number; required):
            Returns the first following sibling that is an element,
            and None otherwise.

        - nextSibling (boolean | number | string | dict | list; required):
            Returns the next sibling.

        - nodeName (string; required):
            Returns a string appropriate for the type of node.

        - nodeType (number; required):
            Returns the type of node.

        - nodeValue (string; required)

        - nonce (string; optional)

        - normalize (required):
            Removes empty exclusive Text nodes and concatenates the
            data of remaining contiguous exclusive Text nodes into the
            first of their nodes.

        - offsetHeight (number; required)

        - offsetLeft (number; required)

        - offsetParent (a list of or a singular dash component, string or number; required)

        - offsetTop (number; required)

        - offsetWidth (number; required)

        - onabort (required):
            Fires when the user aborts the download. @,param,ev, ,The
            event.

        - onanimationcancel (required)

        - onanimationend (required)

        - onanimationiteration (required)

        - onanimationstart (required)

        - onauxclick (required)

        - onbeforeinput (required)

        - onblur (required):
            Fires when the object loses the input focus. @,param,ev,
            ,The focus event.

        - oncancel (required)

        - oncanplay (required):
            Occurs when playback is possible, but would require
            further buffering. @,param,ev, ,The event.

        - oncanplaythrough (required)

        - onchange (required):
            Fires when the contents of the object or selection have
            changed. @,param,ev, ,The event.

        - onclick (required):
            Fires when the user clicks the left mouse button on the
            object @,param,ev, ,The mouse event.

        - onclose (required)

        - oncontextmenu (required):
            Fires when the user clicks the right mouse button in the
            client area, opening the context menu. @,param,ev, ,The
            mouse event.

        - oncopy (required)

        - oncuechange (required)

        - oncut (required)

        - ondblclick (required):
            Fires when the user double-clicks the object. @,param,ev,
            ,The mouse event.

        - ondrag (required):
            Fires on the source object continuously during a drag
            operation. @,param,ev, ,The event.

        - ondragend (required):
            Fires on the source object when the user releases the
            mouse at the close of a drag operation. @,param,ev, ,The
            event.

        - ondragenter (required):
            Fires on the target element when the user drags the object
            to a valid drop target. @,param,ev, ,The drag event.

        - ondragleave (required):
            Fires on the target object when the user moves the mouse
            out of a valid drop target during a drag operation.
            @,param,ev, ,The drag event.

        - ondragover (required):
            Fires on the target element continuously while the user
            drags the object over a valid drop target. @,param,ev,
            ,The event.

        - ondragstart (required):
            Fires on the source object when the user starts to drag a
            text selection or selected object. @,param,ev, ,The event.

        - ondrop (required)

        - ondurationchange (required):
            Occurs when the duration attribute is updated. @,param,ev,
            ,The event.

        - onemptied (required):
            Occurs when the media element is reset to its initial
            state. @,param,ev, ,The event.

        - onended (required):
            Occurs when the end of playback is reached. @,param,ev,
            ,The event.

        - onerror (dict; required):
            Fires when an error occurs during object loading.
            @,param,ev, ,The event.

            `onerror` is a dict with keys:


        - onfocus (required):
            Fires when the object receives focus. @,param,ev, ,The
            event.

        - onformdata (required)

        - onfullscreenchange (required)

        - onfullscreenerror (required)

        - ongotpointercapture (required)

        - oninput (required)

        - oninvalid (required)

        - onkeydown (required):
            Fires when the user presses a key. @,param,ev, ,The
            keyboard event.

        - onkeypress (required):
            Fires when the user presses an alphanumeric key.
            @,param,ev, ,The event. @,deprecated.

        - onkeyup (required):
            Fires when the user releases a key. @,param,ev, ,The
            keyboard event.

        - onload (required):
            Fires immediately after the browser loads the object.
            @,param,ev, ,The event.

        - onloadeddata (required):
            Occurs when media data is loaded at the current playback
            position. @,param,ev, ,The event.

        - onloadedmetadata (required):
            Occurs when the duration and dimensions of the media have
            been determined. @,param,ev, ,The event.

        - onloadstart (required):
            Occurs when Internet Explorer begins looking for media
            data. @,param,ev, ,The event.

        - onlostpointercapture (required)

        - onmousedown (required):
            Fires when the user clicks the object with either mouse
            button. @,param,ev, ,The mouse event.

        - onmouseenter (required)

        - onmouseleave (required)

        - onmousemove (required):
            Fires when the user moves the mouse over the object.
            @,param,ev, ,The mouse event.

        - onmouseout (required):
            Fires when the user moves the mouse pointer outside the
            boundaries of the object. @,param,ev, ,The mouse event.

        - onmouseover (required):
            Fires when the user moves the mouse pointer into the
            object. @,param,ev, ,The mouse event.

        - onmouseup (required):
            Fires when the user releases a mouse button while the
            mouse is over the object. @,param,ev, ,The mouse event.

        - onpaste (required)

        - onpause (required):
            Occurs when playback is paused. @,param,ev, ,The event.

        - onplay (required):
            Occurs when the play method is requested. @,param,ev, ,The
            event.

        - onplaying (required):
            Occurs when the audio or video has started playing.
            @,param,ev, ,The event.

        - onpointercancel (required)

        - onpointerdown (required)

        - onpointerenter (required)

        - onpointerleave (required)

        - onpointermove (required)

        - onpointerout (required)

        - onpointerover (required)

        - onpointerup (required)

        - onprogress (required):
            Occurs to indicate progress while downloading media data.
            @,param,ev, ,The event.

        - onratechange (required):
            Occurs when the playback rate is increased or decreased.
            @,param,ev, ,The event.

        - onreset (required):
            Fires when the user resets a form. @,param,ev, ,The event.

        - onresize (required)

        - onscroll (required):
            Fires when the user repositions the scroll box in the
            scroll bar on the object. @,param,ev, ,The event.

        - onsecuritypolicyviolation (required)

        - onseeked (required):
            Occurs when the seek operation ends. @,param,ev, ,The
            event.

        - onseeking (required):
            Occurs when the current playback position is moved.
            @,param,ev, ,The event.

        - onselect (required):
            Fires when the current selection changes. @,param,ev, ,The
            event.

        - onselectionchange (required)

        - onselectstart (required)

        - onslotchange (required)

        - onstalled (required):
            Occurs when the download has stopped. @,param,ev, ,The
            event.

        - onsubmit (required)

        - onsuspend (required):
            Occurs if the load operation has been intentionally
            halted. @,param,ev, ,The event.

        - ontimeupdate (required):
            Occurs to indicate the current playback position.
            @,param,ev, ,The event.

        - ontoggle (required)

        - ontouchcancel (optional)

        - ontouchend (optional)

        - ontouchmove (optional)

        - ontouchstart (optional)

        - ontransitioncancel (required)

        - ontransitionend (required)

        - ontransitionrun (required)

        - ontransitionstart (required)

        - onvolumechange (required):
            Occurs when the volume is changed, or playback is muted or
            unmuted. @,param,ev, ,The event.

        - onwaiting (required):
            Occurs when playback stops because the next frame of a
            video resource is not available. @,param,ev, ,The event.

        - onwebkitanimationend (required)

        - onwebkitanimationiteration (required)

        - onwebkitanimationstart (required)

        - onwebkittransitionend (required)

        - onwheel (required)

        - outerHTML (string; required)

        - outerText (string; required)

        - ownerDocument (boolean | number | string | dict | list; required)

        - parentElement (boolean | number | string | dict | list; required):
            Returns the parent element.

        - parentNode (boolean | number | string | dict | list; required):
            Returns the parent.

        - part (dict with strings as keys and values of type string; required)

        - prefix (string; required):
            Returns the namespace prefix.

        - prepend (required):
            Inserts nodes before the first child of node, while
            replacing strings in nodes with equivalent Text nodes.
            Throws a \"HierarchyRequestError\" DOMException if the
            constraints of the node tree are violated.

        - previousElementSibling (a list of or a singular dash component, string or number; required):
            Returns the first preceding sibling that is an element,
            and None otherwise.

        - previousSibling (boolean | number | string | dict | list; required):
            Returns the previous sibling.

        - querySelector (dict; required):
            Returns the first element that is a descendant of node
            that matches selectors.

            `querySelector` is a dict with keys:


        - querySelectorAll (dict; required):
            Returns all element descendants of node that match
            selectors.

            `querySelectorAll` is a dict with keys:


        - releasePointerCapture (required)

        - remove (required):
            Removes node.

        - removeAttribute (required):
            Removes element's first attribute whose qualified name is
            qualifiedName.

        - removeAttributeNS (required):
            Removes element's attribute whose namespace is namespace
            and local name is localName.

        - removeAttributeNode (required)

        - removeChild (required)

        - removeEventListener (required)

        - replaceChild (required)

        - replaceChildren (required):
            Replace all children of node with nodes, while replacing
            strings in nodes with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - replaceWith (required):
            Replaces node with nodes, while replacing strings in nodes
            with equivalent Text nodes.  Throws a
            \"HierarchyRequestError\" DOMException if the constraints
            of the node tree are violated.

        - requestFullscreen (required):
            Displays element fullscreen and resolves promise when
            done.  When supplied, options's navigationUI member
            indicates whether showing navigation UI while in
            fullscreen is preferred or not. If set to \"show\",
            navigation simplicity is preferred over screen space, and
            if set to \"hide\", more screen space is preferred. User
            agents are always free to honor user preference over the
            application's. The default value \"auto\" indicates no
            application preference.

        - requestPointerLock (required)

        - role (string; required)

        - scroll (dict; required)

            `scroll` is a dict with keys:


        - scrollBy (dict; required)

            `scrollBy` is a dict with keys:


        - scrollHeight (number; required)

        - scrollIntoView (required)

        - scrollLeft (number; required)

        - scrollTo (dict; required)

            `scrollTo` is a dict with keys:


        - scrollTop (number; required)

        - scrollWidth (number; required)

        - setAttribute (required):
            Sets the value of element's first attribute whose
            qualified name is qualifiedName to value.

        - setAttributeNS (required):
            Sets the value of element's attribute whose namespace is
            namespace and local name is localName to value.

        - setAttributeNode (required)

        - setAttributeNodeNS (required)

        - setPointerCapture (required)

        - shadowRoot (boolean | number | string | dict | list; required):
            Returns element's shadow root, if any, and if shadow
            root's mode is \"open\", and None otherwise.

        - slot (string; required):
            Returns the value of element's slot content attribute. Can
            be set to change it.

        - spellcheck (boolean; required)

        - style (dict with strings as keys and values of type string; required)

        - tabIndex (number; required)

        - tagName (string; required):
            Returns the HTML-uppercased qualified name.

        - textContent (string; required)

        - title (string; required)

        - toggleAttribute (required):
            If force is not given, \"toggles\" qualifiedName, removing
            it if it is present and adding it if it is not present. If
            force is True, adds qualifiedName. If force is False,
            removes qualifiedName.  Returns True if qualifiedName is
            now present, and False otherwise.

        - translate (boolean; required)

        - webkitMatchesSelector (required)

    - yearRange (number | list of numbers; optional):
        Number of years either side (e.g. 10) or array of upper/lower
        range (e.g. [1900, 2015]).

    - yearSuffix (string; optional):
        Additional text to append to the year in the title.

- defaultDate (string; optional)

- disableVisualSelection (boolean | number | string | dict | list; optional)

- dragToScroll (boolean; optional)

- dropdownMenu (boolean | number | string | dict | list; optional)

- editor (string; optional)

- enterBeginsEditing (boolean; optional)

- enterMoves (dict; optional)

    `enterMoves` is a dict with keys:

    - col (number; required)

    - row (number; required)

- exportData (boolean; default False)

- exportDataParams (dict; optional)

    `exportDataParams` is a dict with keys:

    - filename (string; optional)

- fillHandle (boolean | number | string | dict | list; optional)

- filter (boolean; optional)

- filteringCaseSensitive (boolean; optional)

- filters (boolean; optional)

- fixedColumnsLeft (number; optional)

- fixedColumnsStart (number; optional)

- fixedRowsBottom (number; optional)

- fixedRowsTop (number; optional)

- formulas (dict; optional)

    `formulas` is a dict with keys:

    - engine (boolean | number | string | dict | list; required)

    - sheetName (string; optional)

- fragmentSelection (boolean | number | string | dict | list; optional)

- height (string | number; optional)

- hiddenColumns (boolean | number | string | dict | list; optional)

- hiddenRows (boolean | number | string | dict | list; optional)

- imeFastEdit (boolean; optional)

- invalidCellClassName (string; optional)

- label (dict; optional)

    `label` is a dict with keys:

    - position (a value equal to: 'after', 'before'; optional)

    - property (string; optional)

    - value (string; optional)

- language (string; optional)

- layoutDirection (a value equal to: 'ltr', 'rtl', 'inherit'; optional)

- licenseKey (string; optional)

- locale (string; optional)

- manualColumnFreeze (boolean; optional)

- manualColumnMove (list of numbers; optional)

- manualColumnResize (list of numbers; optional)

- manualRowMove (list of numbers; optional)

- manualRowResize (list of numbers; optional)

- maxCols (number; optional)

- maxRows (number; optional)

- mergeCells (boolean | number | string | dict | list; optional)

- minCols (number; optional)

- minRows (number; optional)

- minSpareCols (number; optional)

- minSpareRows (number; optional)

- multiColumnSorting (boolean | number | string | dict | list; optional)

- navigableHeaders (boolean; optional)

- nestedHeaders (dict with strings as keys and values of type list of strings; optional)

- nestedRows (boolean; optional)

- noWordWrapClassName (string; optional)

- numericFormat (dict; optional)

    `numericFormat` is a dict with keys:

    - culture (string; optional)

    - pattern (string; required)

- observeDOMVisibility (boolean; optional)

- outsideClickDeselects (optional)

- persistentState (boolean; optional)

- placeholder (string; optional)

- placeholderCellClassName (string; optional)

- preventOverflow (boolean | number | string | dict | list; optional)

- preventWheel (boolean; optional)

- readOnly (boolean; optional)

- readOnlyCellClassName (string; optional)

- renderAllColumns (boolean; optional)

- renderAllRows (boolean; optional)

- renderer (string; optional)

- rowHeaderWidth (number | list of numbers; optional)

- rowHeaders (list of strings; optional)

- rowHeights (string | number | list of strings | list of numbers; optional)

- search (boolean | number | string | dict | list; optional)

- selectOptions (list of strings; optional)

- selectionMode (a value equal to: 'single', 'range', 'multiple'; optional)

- settings (dict; optional)

    `settings` is a dict with keys:

    - activeHeaderClassName (string; optional)

    - afterAddChild (optional)

    - afterAutofill (optional)

    - afterBeginEditing (optional)

    - afterCellMetaReset (optional)

    - afterChange (optional)

    - afterChangesObserved (optional)

    - afterColumnCollapse (optional)

    - afterColumnExpand (optional)

    - afterColumnFreeze (optional)

    - afterColumnMove (optional)

    - afterColumnResize (optional)

    - afterColumnSequenceChange (optional)

    - afterColumnSort (optional)

    - afterColumnUnfreeze (optional)

    - afterContextMenuDefaultOptions (optional)

    - afterContextMenuHide (optional)

    - afterContextMenuShow (optional)

    - afterCopy (optional)

    - afterCopyLimit (optional)

    - afterCreateCol (optional)

    - afterCreateRow (optional)

    - afterCut (optional)

    - afterDeselect (optional)

    - afterDestroy (optional)

    - afterDetachChild (optional)

    - afterDocumentKeyDown (optional)

    - afterDrawSelection (optional)

    - afterDropdownMenuDefaultOptions (optional)

    - afterDropdownMenuHide (optional)

    - afterDropdownMenuShow (optional)

    - afterFilter (optional)

    - afterFormulasValuesUpdate (optional)

    - afterGetCellMeta (optional)

    - afterGetColHeader (optional)

    - afterGetColumnHeaderRenderers (optional)

    - afterGetRowHeader (optional)

    - afterGetRowHeaderRenderers (optional)

    - afterHideColumns (optional)

    - afterHideRows (optional)

    - afterInit (optional)

    - afterLanguageChange (optional)

    - afterListen (optional)

    - afterLoadData (optional)

    - afterMergeCells (optional)

    - afterModifyTransformEnd (optional)

    - afterModifyTransformFocus (optional)

    - afterModifyTransformStart (optional)

    - afterMomentumScroll (optional)

    - afterNamedExpressionAdded (optional)

    - afterNamedExpressionRemoved (optional)

    - afterOnCellContextMenu (optional)

    - afterOnCellCornerDblClick (optional)

    - afterOnCellCornerMouseDown (optional)

    - afterOnCellMouseDown (optional)

    - afterOnCellMouseOut (optional)

    - afterOnCellMouseOver (optional)

    - afterOnCellMouseUp (optional)

    - afterPaste (optional)

    - afterPluginsInitialized (optional)

    - afterRedo (optional)

    - afterRedoStackChange (optional)

    - afterRefreshDimensions (optional)

    - afterRemoveCellMeta (optional)

    - afterRemoveCol (optional)

    - afterRemoveRow (optional)

    - afterRender (optional)

    - afterRenderer (optional)

    - afterRowMove (optional)

    - afterRowResize (optional)

    - afterRowSequenceChange (optional)

    - afterScroll (optional)

    - afterScrollHorizontally (optional)

    - afterScrollVertically (optional)

    - afterSelectColumns (optional)

    - afterSelectRows (optional)

    - afterSelection (optional)

    - afterSelectionByProp (optional)

    - afterSelectionEnd (optional)

    - afterSelectionEndByProp (optional)

    - afterSelectionFocusSet (optional)

    - afterSetCellMeta (optional)

    - afterSetDataAtCell (optional)

    - afterSetDataAtRowProp (optional)

    - afterSetSourceDataAtCell (optional)

    - afterSheetAdded (optional)

    - afterSheetRemoved (optional)

    - afterSheetRenamed (optional)

    - afterTrimRow (optional)

    - afterUndo (optional)

    - afterUndoStackChange (optional)

    - afterUnhideColumns (optional)

    - afterUnhideRows (optional)

    - afterUnlisten (optional)

    - afterUnmergeCells (optional)

    - afterUntrimRow (optional)

    - afterUpdateData (optional)

    - afterUpdateSettings (optional)

    - afterValidate (optional)

    - afterViewRender (optional)

    - afterViewportColumnCalculatorOverride (optional)

    - afterViewportRowCalculatorOverride (optional)

    - allowEmpty (boolean; optional)

    - allowHtml (boolean; optional)

    - allowInsertColumn (boolean; optional)

    - allowInsertRow (boolean; optional)

    - allowInvalid (boolean; optional)

    - allowRemoveColumn (boolean; optional)

    - allowRemoveRow (boolean; optional)

    - ariaTags (boolean; optional)

    - autoColumnSize (boolean | number | string | dict | list; optional)

    - autoRowSize (boolean | number | string | dict | list; optional)

    - autoWrapCol (boolean; optional)

    - autoWrapRow (boolean; optional)

    - beforeAddChild (optional)

    - beforeAutofill (optional)

    - beforeBeginEditing (optional)

    - beforeCellAlignment (optional)

    - beforeChange (optional)

    - beforeChangeRender (optional)

    - beforeColumnCollapse (optional)

    - beforeColumnExpand (optional)

    - beforeColumnFreeze (optional)

    - beforeColumnMove (optional)

    - beforeColumnResize (optional)

    - beforeColumnSort (optional)

    - beforeColumnUnfreeze (optional)

    - beforeColumnWrap (optional)

    - beforeContextMenuSetItems (optional)

    - beforeContextMenuShow (optional)

    - beforeCopy (optional)

    - beforeCreateCol (optional)

    - beforeCreateRow (optional)

    - beforeCut (optional)

    - beforeDetachChild (optional)

    - beforeDrawBorders (optional)

    - beforeDropdownMenuSetItems (optional)

    - beforeDropdownMenuShow (optional)

    - beforeFilter (optional)

    - beforeGetCellMeta (optional)

    - beforeHideColumns (optional)

    - beforeHideRows (optional)

    - beforeHighlightingColumnHeader (optional)

    - beforeHighlightingRowHeader (optional)

    - beforeInit (optional)

    - beforeInitWalkontable (optional)

    - beforeKeyDown (optional)

    - beforeLanguageChange (optional)

    - beforeLoadData (optional)

    - beforeMergeCells (optional)

    - beforeOnCellContextMenu (optional)

    - beforeOnCellMouseDown (optional)

    - beforeOnCellMouseOut (optional)

    - beforeOnCellMouseOver (optional)

    - beforeOnCellMouseUp (optional)

    - beforePaste (optional)

    - beforeRedo (optional)

    - beforeRedoStackChange (optional)

    - beforeRefreshDimensions (optional)

    - beforeRemoveCellClassNames (optional)

    - beforeRemoveCellMeta (optional)

    - beforeRemoveCol (optional)

    - beforeRemoveRow (optional)

    - beforeRender (optional)

    - beforeRenderer (optional)

    - beforeRowMove (optional)

    - beforeRowResize (optional)

    - beforeRowWrap (optional)

    - beforeSelectColumns (optional)

    - beforeSelectRows (optional)

    - beforeSelectionFocusSet (optional)

    - beforeSelectionHighlightSet (optional)

    - beforeSetCellMeta (optional)

    - beforeSetRangeEnd (optional)

    - beforeSetRangeStart (optional)

    - beforeSetRangeStartOnly (optional)

    - beforeStretchingColumnWidth (optional)

    - beforeTouchScroll (optional)

    - beforeTrimRow (optional)

    - beforeUndo (optional)

    - beforeUndoStackChange (optional)

    - beforeUnhideColumns (optional)

    - beforeUnhideRows (optional)

    - beforeUnmergeCells (optional)

    - beforeUntrimRow (optional)

    - beforeUpdateData (optional)

    - beforeValidate (optional)

    - beforeValueRender (optional)

    - beforeViewRender (optional)

    - beforeViewportScroll (optional)

    - beforeViewportScrollHorizontally (optional)

    - beforeViewportScrollVertically (optional)

    - bindRowsWithHeaders (boolean | number | string | dict | list; optional)

    - cell (list of dicts with strings as keys and values of type boolean | number | string | dict | list; optional)

    - cells (optional)

    - checkedTemplate (string | number; optional)

    - className (string | list of strings; optional)

    - colHeaders (list of strings; optional)

    - colWidths (string | number | list of strings | list of numbers; optional)

    - collapsibleColumns (boolean | number | string | dict | list; optional)

    - columnHeaderHeight (number | list of numbers; optional)

    - columnSorting (boolean | number | string | dict | list; optional)

    - columnSummary (optional)

    - columns (optional)

    - commentedCellClassName (string; optional)

    - comments (boolean | number | string | dict | list; optional)

    - construct (optional)

    - contextMenu (boolean | number | string | dict | list; optional)

    - copyPaste (boolean | number | string | dict | list; optional)

    - copyable (boolean; optional)

    - correctFormat (boolean; optional)

    - currentColClassName (string; optional)

    - currentHeaderClassName (string; optional)

    - currentRowClassName (string; optional)

    - customBorders (boolean | number | string | dict | list; optional)

    - data (list of list of boolean | number | string | dict | listss; optional)

    - dataSchema (list of boolean | number | string | dict | lists; optional)

    - dateFormat (string; optional)

    - datePickerConfig (dict; optional)

        `datePickerConfig` is a dict with keys:

        - ariaLabel (string; optional):
            Data-attribute on the input field with an aria assistance
            test (only applied when bound is set).

        - blurFieldOnSelect (boolean; optional):
            Defines if the field is blurred when a date is selected
            (default True).

        - bound (boolean; optional):
            Automatically show/hide the datepicker on field focus.
            Default: True if field is set.

        - container (dict; optional):
            DOM node to render calendar into, see container example.
            Default: undefined.

            `container` is a dict with keys:

            - ATTRIBUTE_NODE (number; required)

            - CDATA_SECTION_NODE (number; required):
                node is a CDATASection node.

            - COMMENT_NODE (number; required):
                node is a Comment node.

            - DOCUMENT_FRAGMENT_NODE (number; required):
                node is a DocumentFragment node.

            - DOCUMENT_NODE (number; required):
                node is a document.

            - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                Set when other is a descendant of node.

            - DOCUMENT_POSITION_CONTAINS (number; required):
                Set when other is an ancestor of node.

            - DOCUMENT_POSITION_DISCONNECTED (number; required):
                Set when node and other are not in the same tree.

            - DOCUMENT_POSITION_FOLLOWING (number; required):
                Set when other is following node.

            - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

            - DOCUMENT_POSITION_PRECEDING (number; required):
                Set when other is preceding node.

            - DOCUMENT_TYPE_NODE (number; required):
                node is a doctype.

            - ELEMENT_NODE (number; required):
                node is an element.

            - ENTITY_NODE (number; required)

            - ENTITY_REFERENCE_NODE (number; required)

            - NOTATION_NODE (number; required)

            - PROCESSING_INSTRUCTION_NODE (number; required):
                node is a ProcessingInstruction node.

            - TEXT_NODE (number; required):
                node is a Text node.

            - accessKey (string; required)

            - accessKeyLabel (string; required)

            - addEventListener (required)

            - after (required):
                Inserts nodes just after node, while replacing strings
                in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - animate (required)

            - append (required):
                Inserts nodes after the last child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - appendChild (required)

            - ariaAtomic (string; required)

            - ariaAutoComplete (string; required)

            - ariaBusy (string; required)

            - ariaChecked (string; required)

            - ariaColCount (string; required)

            - ariaColIndex (string; required)

            - ariaColIndexText (string; required)

            - ariaColSpan (string; required)

            - ariaCurrent (string; required)

            - ariaDisabled (string; required)

            - ariaExpanded (string; required)

            - ariaHasPopup (string; required)

            - ariaHidden (string; required)

            - ariaInvalid (string; required)

            - ariaKeyShortcuts (string; required)

            - ariaLabel (string; required)

            - ariaLevel (string; required)

            - ariaLive (string; required)

            - ariaModal (string; required)

            - ariaMultiLine (string; required)

            - ariaMultiSelectable (string; required)

            - ariaOrientation (string; required)

            - ariaPlaceholder (string; required)

            - ariaPosInSet (string; required)

            - ariaPressed (string; required)

            - ariaReadOnly (string; required)

            - ariaRequired (string; required)

            - ariaRoleDescription (string; required)

            - ariaRowCount (string; required)

            - ariaRowIndex (string; required)

            - ariaRowIndexText (string; required)

            - ariaRowSpan (string; required)

            - ariaSelected (string; required)

            - ariaSetSize (string; required)

            - ariaSort (string; required)

            - ariaValueMax (string; required)

            - ariaValueMin (string; required)

            - ariaValueNow (string; required)

            - ariaValueText (string; required)

            - assignedSlot (dict; required)

                `assignedSlot` is a dict with keys:

                - ATTRIBUTE_NODE (number; required)

                - CDATA_SECTION_NODE (number; required):
                    node is a CDATASection node.

                - COMMENT_NODE (number; required):
                    node is a Comment node.

                - DOCUMENT_FRAGMENT_NODE (number; required):
                    node is a DocumentFragment node.

                - DOCUMENT_NODE (number; required):
                    node is a document.

                - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                    Set when other is a descendant of node.

                - DOCUMENT_POSITION_CONTAINS (number; required):
                    Set when other is an ancestor of node.

                - DOCUMENT_POSITION_DISCONNECTED (number; required):
                    Set when node and other are not in the same tree.

                - DOCUMENT_POSITION_FOLLOWING (number; required):
                    Set when other is following node.

                - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

                - DOCUMENT_POSITION_PRECEDING (number; required):
                    Set when other is preceding node.

                - DOCUMENT_TYPE_NODE (number; required):
                    node is a doctype.

                - ELEMENT_NODE (number; required):
                    node is an element.

                - ENTITY_NODE (number; required)

                - ENTITY_REFERENCE_NODE (number; required)

                - NOTATION_NODE (number; required)

                - PROCESSING_INSTRUCTION_NODE (number; required):
                    node is a ProcessingInstruction node.

                - TEXT_NODE (number; required):
                    node is a Text node.

                - accessKey (string; required)

                - accessKeyLabel (string; required)

                - addEventListener (required)

                - after (required):
                    Inserts nodes just after node, while replacing
                    strings in nodes with equivalent Text nodes.
                    Throws a \"HierarchyRequestError\" DOMException if
                    the constraints of the node tree are violated.

                - animate (required)

                - append (required):
                    Inserts nodes after the last child of node, while
                    replacing strings in nodes with equivalent Text
                    nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - appendChild (required)

                - ariaAtomic (string; required)

                - ariaAutoComplete (string; required)

                - ariaBusy (string; required)

                - ariaChecked (string; required)

                - ariaColCount (string; required)

                - ariaColIndex (string; required)

                - ariaColIndexText (string; required)

                - ariaColSpan (string; required)

                - ariaCurrent (string; required)

                - ariaDisabled (string; required)

                - ariaExpanded (string; required)

                - ariaHasPopup (string; required)

                - ariaHidden (string; required)

                - ariaInvalid (string; required)

                - ariaKeyShortcuts (string; required)

                - ariaLabel (string; required)

                - ariaLevel (string; required)

                - ariaLive (string; required)

                - ariaModal (string; required)

                - ariaMultiLine (string; required)

                - ariaMultiSelectable (string; required)

                - ariaOrientation (string; required)

                - ariaPlaceholder (string; required)

                - ariaPosInSet (string; required)

                - ariaPressed (string; required)

                - ariaReadOnly (string; required)

                - ariaRequired (string; required)

                - ariaRoleDescription (string; required)

                - ariaRowCount (string; required)

                - ariaRowIndex (string; required)

                - ariaRowIndexText (string; required)

                - ariaRowSpan (string; required)

                - ariaSelected (string; required)

                - ariaSetSize (string; required)

                - ariaSort (string; required)

                - ariaValueMax (string; required)

                - ariaValueMin (string; required)

                - ariaValueNow (string; required)

                - ariaValueText (string; required)

                - assign (required)

                - assignedElements (required)

                - assignedNodes (required)

                - assignedSlot (boolean | number | string | dict | list; required)

                - attachInternals (required)

                - attachShadow (required):
                    Creates a shadow root for element and returns it.

                - attributes (dict; required)

                    `attributes` is a dict with strings as keys and
                    values of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

                - autocapitalize (string; required)

                - autofocus (boolean; required)

                - baseURI (string; required):
                    Returns node's node document's document base URL.

                - before (required):
                    Inserts nodes just before node, while replacing
                    strings in nodes with equivalent Text nodes.
                    Throws a \"HierarchyRequestError\" DOMException if
                    the constraints of the node tree are violated.

                - blur (required)

                - childElementCount (number; required)

                - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                    Returns the children.

                - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                    Returns the child elements.

                - classList (dict with strings as keys and values of type string; required):
                    Allows for manipulation of element's class content
                    attribute as a set of whitespace-separated tokens
                    through a DOMTokenList object.

                - className (string; required):
                    Returns the value of element's class content
                    attribute. Can be set to change it.

                - click (required)

                - clientHeight (number; required)

                - clientLeft (number; required)

                - clientTop (number; required)

                - clientWidth (number; required)

                - cloneNode (required):
                    Returns a copy of node. If deep is True, the copy
                    also includes the node's descendants.

                - closest (dict; required):
                    Returns the first (starting at element) inclusive
                    ancestor that matches selectors, and None
                    otherwise.

                    `closest` is a dict with keys:


                - compareDocumentPosition (required):
                    Returns a bitmask indicating the position of other
                    relative to node.

                - contains (required):
                    Returns True if other is an inclusive descendant
                    of node, and False otherwise.

                - contentEditable (string; required)

                - dataset (dict with strings as keys and values of type string; required)

                - dir (string; required)

                - dispatchEvent (required):
                    Dispatches a synthetic event event to target and
                    returns True if either event's cancelable
                    attribute value is False or its preventDefault()
                    method was not invoked, and False otherwise.

                - draggable (boolean; required)

                - enterKeyHint (string; required)

                - firstChild (boolean | number | string | dict | list; required):
                    Returns the first child.

                - firstElementChild (a list of or a singular dash component, string or number; required):
                    Returns the first child that is an element, and
                    None otherwise.

                - focus (required)

                - getAnimations (required)

                - getAttribute (required):
                    Returns element's first attribute whose qualified
                    name is qualifiedName, and None if there is no
                    such attribute otherwise.

                - getAttributeNS (required):
                    Returns element's attribute whose namespace is
                    namespace and local name is localName, and None if
                    there is no such attribute otherwise.

                - getAttributeNames (required):
                    Returns the qualified names of all element's
                    attributes. Can contain duplicates.

                - getAttributeNode (required)

                - getAttributeNodeNS (required)

                - getBoundingClientRect (required)

                - getClientRects (required)

                - getElementsByClassName (required):
                    Returns a HTMLCollection of the elements in the
                    object on which the method was invoked (a document
                    or an element) that have all the classes given by
                    classNames. The classNames argument is interpreted
                    as a space-separated list of classes.

                - getElementsByTagName (dict; required)

                    `getElementsByTagName` is a dict with keys:


                - getElementsByTagNameNS (dict; required)

                    `getElementsByTagNameNS` is a dict with keys:


                - getRootNode (required):
                    Returns node's root.

                - hasAttribute (required):
                    Returns True if element has an attribute whose
                    qualified name is qualifiedName, and False
                    otherwise.

                - hasAttributeNS (required):
                    Returns True if element has an attribute whose
                    namespace is namespace and local name is
                    localName.

                - hasAttributes (required):
                    Returns True if element has attributes, and False
                    otherwise.

                - hasChildNodes (required):
                    Returns whether node has children.

                - hasPointerCapture (required)

                - hidden (boolean; required)

                - id (string; required):
                    Returns the value of element's id content
                    attribute. Can be set to change it.

                - inert (boolean; required)

                - innerHTML (string; required)

                - innerText (string; required)

                - inputMode (string; required)

                - insertAdjacentElement (required)

                - insertAdjacentHTML (required)

                - insertAdjacentText (required)

                - insertBefore (required)

                - isConnected (boolean; required):
                    Returns True if node is connected and False
                    otherwise.

                - isContentEditable (boolean; required)

                - isDefaultNamespace (required)

                - isEqualNode (required):
                    Returns whether node and otherNode have the same
                    properties.

                - isSameNode (required)

                - lang (string; required)

                - lastChild (boolean | number | string | dict | list; required):
                    Returns the last child.

                - lastElementChild (a list of or a singular dash component, string or number; required):
                    Returns the last child that is an element, and
                    None otherwise.

                - localName (string; required):
                    Returns the local name.

                - lookupNamespaceURI (required)

                - lookupPrefix (required)

                - matches (required):
                    Returns True if matching selectors against
                    element's root yields element, and False
                    otherwise.

                - name (string; required)

                - namespaceURI (string; required):
                    Returns the namespace.

                - nextElementSibling (a list of or a singular dash component, string or number; required):
                    Returns the first following sibling that is an
                    element, and None otherwise.

                - nextSibling (boolean | number | string | dict | list; required):
                    Returns the next sibling.

                - nodeName (string; required):
                    Returns a string appropriate for the type of node.

                - nodeType (number; required):
                    Returns the type of node.

                - nodeValue (string; required)

                - nonce (string; optional)

                - normalize (required):
                    Removes empty exclusive Text nodes and
                    concatenates the data of remaining contiguous
                    exclusive Text nodes into the first of their
                    nodes.

                - offsetHeight (number; required)

                - offsetLeft (number; required)

                - offsetParent (a list of or a singular dash component, string or number; required)

                - offsetTop (number; required)

                - offsetWidth (number; required)

                - onabort (required):
                    Fires when the user aborts the download.
                    @,param,ev, ,The event.

                - onanimationcancel (required)

                - onanimationend (required)

                - onanimationiteration (required)

                - onanimationstart (required)

                - onauxclick (required)

                - onbeforeinput (required)

                - onblur (required):
                    Fires when the object loses the input focus.
                    @,param,ev, ,The focus event.

                - oncancel (required)

                - oncanplay (required):
                    Occurs when playback is possible, but would
                    require further buffering. @,param,ev, ,The event.

                - oncanplaythrough (required)

                - onchange (required):
                    Fires when the contents of the object or selection
                    have changed. @,param,ev, ,The event.

                - onclick (required):
                    Fires when the user clicks the left mouse button
                    on the object @,param,ev, ,The mouse event.

                - onclose (required)

                - oncontextmenu (required):
                    Fires when the user clicks the right mouse button
                    in the client area, opening the context menu.
                    @,param,ev, ,The mouse event.

                - oncopy (required)

                - oncuechange (required)

                - oncut (required)

                - ondblclick (required):
                    Fires when the user double-clicks the object.
                    @,param,ev, ,The mouse event.

                - ondrag (required):
                    Fires on the source object continuously during a
                    drag operation. @,param,ev, ,The event.

                - ondragend (required):
                    Fires on the source object when the user releases
                    the mouse at the close of a drag operation.
                    @,param,ev, ,The event.

                - ondragenter (required):
                    Fires on the target element when the user drags
                    the object to a valid drop target. @,param,ev,
                    ,The drag event.

                - ondragleave (required):
                    Fires on the target object when the user moves the
                    mouse out of a valid drop target during a drag
                    operation. @,param,ev, ,The drag event.

                - ondragover (required):
                    Fires on the target element continuously while the
                    user drags the object over a valid drop target.
                    @,param,ev, ,The event.

                - ondragstart (required):
                    Fires on the source object when the user starts to
                    drag a text selection or selected object.
                    @,param,ev, ,The event.

                - ondrop (required)

                - ondurationchange (required):
                    Occurs when the duration attribute is updated.
                    @,param,ev, ,The event.

                - onemptied (required):
                    Occurs when the media element is reset to its
                    initial state. @,param,ev, ,The event.

                - onended (required):
                    Occurs when the end of playback is reached.
                    @,param,ev, ,The event.

                - onerror (dict; required):
                    Fires when an error occurs during object loading.
                    @,param,ev, ,The event.

                    `onerror` is a dict with keys:


                - onfocus (required):
                    Fires when the object receives focus. @,param,ev,
                    ,The event.

                - onformdata (required)

                - onfullscreenchange (required)

                - onfullscreenerror (required)

                - ongotpointercapture (required)

                - oninput (required)

                - oninvalid (required)

                - onkeydown (required):
                    Fires when the user presses a key. @,param,ev,
                    ,The keyboard event.

                - onkeypress (required):
                    Fires when the user presses an alphanumeric key.
                    @,param,ev, ,The event. @,deprecated.

                - onkeyup (required):
                    Fires when the user releases a key. @,param,ev,
                    ,The keyboard event.

                - onload (required):
                    Fires immediately after the browser loads the
                    object. @,param,ev, ,The event.

                - onloadeddata (required):
                    Occurs when media data is loaded at the current
                    playback position. @,param,ev, ,The event.

                - onloadedmetadata (required):
                    Occurs when the duration and dimensions of the
                    media have been determined. @,param,ev, ,The
                    event.

                - onloadstart (required):
                    Occurs when Internet Explorer begins looking for
                    media data. @,param,ev, ,The event.

                - onlostpointercapture (required)

                - onmousedown (required):
                    Fires when the user clicks the object with either
                    mouse button. @,param,ev, ,The mouse event.

                - onmouseenter (required)

                - onmouseleave (required)

                - onmousemove (required):
                    Fires when the user moves the mouse over the
                    object. @,param,ev, ,The mouse event.

                - onmouseout (required):
                    Fires when the user moves the mouse pointer
                    outside the boundaries of the object. @,param,ev,
                    ,The mouse event.

                - onmouseover (required):
                    Fires when the user moves the mouse pointer into
                    the object. @,param,ev, ,The mouse event.

                - onmouseup (required):
                    Fires when the user releases a mouse button while
                    the mouse is over the object. @,param,ev, ,The
                    mouse event.

                - onpaste (required)

                - onpause (required):
                    Occurs when playback is paused. @,param,ev, ,The
                    event.

                - onplay (required):
                    Occurs when the play method is requested.
                    @,param,ev, ,The event.

                - onplaying (required):
                    Occurs when the audio or video has started
                    playing. @,param,ev, ,The event.

                - onpointercancel (required)

                - onpointerdown (required)

                - onpointerenter (required)

                - onpointerleave (required)

                - onpointermove (required)

                - onpointerout (required)

                - onpointerover (required)

                - onpointerup (required)

                - onprogress (required):
                    Occurs to indicate progress while downloading
                    media data. @,param,ev, ,The event.

                - onratechange (required):
                    Occurs when the playback rate is increased or
                    decreased. @,param,ev, ,The event.

                - onreset (required):
                    Fires when the user resets a form. @,param,ev,
                    ,The event.

                - onresize (required)

                - onscroll (required):
                    Fires when the user repositions the scroll box in
                    the scroll bar on the object. @,param,ev, ,The
                    event.

                - onsecuritypolicyviolation (required)

                - onseeked (required):
                    Occurs when the seek operation ends. @,param,ev,
                    ,The event.

                - onseeking (required):
                    Occurs when the current playback position is
                    moved. @,param,ev, ,The event.

                - onselect (required):
                    Fires when the current selection changes.
                    @,param,ev, ,The event.

                - onselectionchange (required)

                - onselectstart (required)

                - onslotchange (required)

                - onstalled (required):
                    Occurs when the download has stopped. @,param,ev,
                    ,The event.

                - onsubmit (required)

                - onsuspend (required):
                    Occurs if the load operation has been
                    intentionally halted. @,param,ev, ,The event.

                - ontimeupdate (required):
                    Occurs to indicate the current playback position.
                    @,param,ev, ,The event.

                - ontoggle (required)

                - ontouchcancel (optional)

                - ontouchend (optional)

                - ontouchmove (optional)

                - ontouchstart (optional)

                - ontransitioncancel (required)

                - ontransitionend (required)

                - ontransitionrun (required)

                - ontransitionstart (required)

                - onvolumechange (required):
                    Occurs when the volume is changed, or playback is
                    muted or unmuted. @,param,ev, ,The event.

                - onwaiting (required):
                    Occurs when playback stops because the next frame
                    of a video resource is not available. @,param,ev,
                    ,The event.

                - onwebkitanimationend (required)

                - onwebkitanimationiteration (required)

                - onwebkitanimationstart (required)

                - onwebkittransitionend (required)

                - onwheel (required)

                - outerHTML (string; required)

                - outerText (string; required)

                - ownerDocument (boolean | number | string | dict | list; required)

                - parentElement (boolean | number | string | dict | list; required):
                    Returns the parent element.

                - parentNode (boolean | number | string | dict | list; required):
                    Returns the parent.

                - part (dict with strings as keys and values of type string; required)

                - prefix (string; required):
                    Returns the namespace prefix.

                - prepend (required):
                    Inserts nodes before the first child of node,
                    while replacing strings in nodes with equivalent
                    Text nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - previousElementSibling (a list of or a singular dash component, string or number; required):
                    Returns the first preceding sibling that is an
                    element, and None otherwise.

                - previousSibling (boolean | number | string | dict | list; required):
                    Returns the previous sibling.

                - querySelector (dict; required):
                    Returns the first element that is a descendant of
                    node that matches selectors.

                    `querySelector` is a dict with keys:


                - querySelectorAll (dict; required):
                    Returns all element descendants of node that match
                    selectors.

                    `querySelectorAll` is a dict with keys:


                - releasePointerCapture (required)

                - remove (required):
                    Removes node.

                - removeAttribute (required):
                    Removes element's first attribute whose qualified
                    name is qualifiedName.

                - removeAttributeNS (required):
                    Removes element's attribute whose namespace is
                    namespace and local name is localName.

                - removeAttributeNode (required)

                - removeChild (required)

                - removeEventListener (required)

                - replaceChild (required)

                - replaceChildren (required):
                    Replace all children of node with nodes, while
                    replacing strings in nodes with equivalent Text
                    nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - replaceWith (required):
                    Replaces node with nodes, while replacing strings
                    in nodes with equivalent Text nodes.  Throws a
                    \"HierarchyRequestError\" DOMException if the
                    constraints of the node tree are violated.

                - requestFullscreen (required):
                    Displays element fullscreen and resolves promise
                    when done.  When supplied, options's navigationUI
                    member indicates whether showing navigation UI
                    while in fullscreen is preferred or not. If set to
                    \"show\", navigation simplicity is preferred over
                    screen space, and if set to \"hide\", more screen
                    space is preferred. User agents are always free to
                    honor user preference over the application's. The
                    default value \"auto\" indicates no application
                    preference.

                - requestPointerLock (required)

                - role (string; required)

                - scroll (dict; required)

                    `scroll` is a dict with keys:


                - scrollBy (dict; required)

                    `scrollBy` is a dict with keys:


                - scrollHeight (number; required)

                - scrollIntoView (required)

                - scrollLeft (number; required)

                - scrollTo (dict; required)

                    `scrollTo` is a dict with keys:


                - scrollTop (number; required)

                - scrollWidth (number; required)

                - setAttribute (required):
                    Sets the value of element's first attribute whose
                    qualified name is qualifiedName to value.

                - setAttributeNS (required):
                    Sets the value of element's attribute whose
                    namespace is namespace and local name is localName
                    to value.

                - setAttributeNode (required)

                - setAttributeNodeNS (required)

                - setPointerCapture (required)

                - shadowRoot (boolean | number | string | dict | list; required):
                    Returns element's shadow root, if any, and if
                    shadow root's mode is \"open\", and None
                    otherwise.

                - slot (string; required):
                    Returns the value of element's slot content
                    attribute. Can be set to change it.

                - spellcheck (boolean; required)

                - style (dict with strings as keys and values of type string; required)

                - tabIndex (number; required)

                - tagName (string; required):
                    Returns the HTML-uppercased qualified name.

                - textContent (string; required)

                - title (string; required)

                - toggleAttribute (required):
                    If force is not given, \"toggles\" qualifiedName,
                    removing it if it is present and adding it if it
                    is not present. If force is True, adds
                    qualifiedName. If force is False, removes
                    qualifiedName.  Returns True if qualifiedName is
                    now present, and False otherwise.

                - translate (boolean; required)

                - webkitMatchesSelector (required)

            - attachInternals (required)

            - attachShadow (required):
                Creates a shadow root for element and returns it.

            - attributes (dict; required)

                `attributes` is a dict with strings as keys and values
                of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

            - autocapitalize (string; required)

            - autofocus (boolean; required)

            - baseURI (string; required):
                Returns node's node document's document base URL.

            - before (required):
                Inserts nodes just before node, while replacing
                strings in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - blur (required)

            - childElementCount (number; required)

            - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                Returns the children.

            - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                Returns the child elements.

            - classList (dict with strings as keys and values of type string; required):
                Allows for manipulation of element's class content
                attribute as a set of whitespace-separated tokens
                through a DOMTokenList object.

            - className (string; required):
                Returns the value of element's class content
                attribute. Can be set to change it.

            - click (required)

            - clientHeight (number; required)

            - clientLeft (number; required)

            - clientTop (number; required)

            - clientWidth (number; required)

            - cloneNode (required):
                Returns a copy of node. If deep is True, the copy also
                includes the node's descendants.

            - closest (dict; required):
                Returns the first (starting at element) inclusive
                ancestor that matches selectors, and None otherwise.

                `closest` is a dict with keys:


            - compareDocumentPosition (required):
                Returns a bitmask indicating the position of other
                relative to node.

            - contains (required):
                Returns True if other is an inclusive descendant of
                node, and False otherwise.

            - contentEditable (string; required)

            - dataset (dict with strings as keys and values of type string; required)

            - dir (string; required)

            - dispatchEvent (required):
                Dispatches a synthetic event event to target and
                returns True if either event's cancelable attribute
                value is False or its preventDefault() method was not
                invoked, and False otherwise.

            - draggable (boolean; required)

            - enterKeyHint (string; required)

            - firstChild (boolean | number | string | dict | list; required):
                Returns the first child.

            - firstElementChild (a list of or a singular dash component, string or number; required):
                Returns the first child that is an element, and None
                otherwise.

            - focus (required)

            - getAnimations (required)

            - getAttribute (required):
                Returns element's first attribute whose qualified name
                is qualifiedName, and None if there is no such
                attribute otherwise.

            - getAttributeNS (required):
                Returns element's attribute whose namespace is
                namespace and local name is localName, and None if
                there is no such attribute otherwise.

            - getAttributeNames (required):
                Returns the qualified names of all element's
                attributes. Can contain duplicates.

            - getAttributeNode (required)

            - getAttributeNodeNS (required)

            - getBoundingClientRect (required)

            - getClientRects (required)

            - getElementsByClassName (required):
                Returns a HTMLCollection of the elements in the object
                on which the method was invoked (a document or an
                element) that have all the classes given by
                classNames. The classNames argument is interpreted as
                a space-separated list of classes.

            - getElementsByTagName (dict; required)

                `getElementsByTagName` is a dict with keys:


            - getElementsByTagNameNS (dict; required)

                `getElementsByTagNameNS` is a dict with keys:


            - getRootNode (required):
                Returns node's root.

            - hasAttribute (required):
                Returns True if element has an attribute whose
                qualified name is qualifiedName, and False otherwise.

            - hasAttributeNS (required):
                Returns True if element has an attribute whose
                namespace is namespace and local name is localName.

            - hasAttributes (required):
                Returns True if element has attributes, and False
                otherwise.

            - hasChildNodes (required):
                Returns whether node has children.

            - hasPointerCapture (required)

            - hidden (boolean; required)

            - id (string; required):
                Returns the value of element's id content attribute.
                Can be set to change it.

            - inert (boolean; required)

            - innerHTML (string; required)

            - innerText (string; required)

            - inputMode (string; required)

            - insertAdjacentElement (required)

            - insertAdjacentHTML (required)

            - insertAdjacentText (required)

            - insertBefore (required)

            - isConnected (boolean; required):
                Returns True if node is connected and False otherwise.

            - isContentEditable (boolean; required)

            - isDefaultNamespace (required)

            - isEqualNode (required):
                Returns whether node and otherNode have the same
                properties.

            - isSameNode (required)

            - lang (string; required)

            - lastChild (boolean | number | string | dict | list; required):
                Returns the last child.

            - lastElementChild (a list of or a singular dash component, string or number; required):
                Returns the last child that is an element, and None
                otherwise.

            - localName (string; required):
                Returns the local name.

            - lookupNamespaceURI (required)

            - lookupPrefix (required)

            - matches (required):
                Returns True if matching selectors against element's
                root yields element, and False otherwise.

            - namespaceURI (string; required):
                Returns the namespace.

            - nextElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first following sibling that is an
                element, and None otherwise.

            - nextSibling (boolean | number | string | dict | list; required):
                Returns the next sibling.

            - nodeName (string; required):
                Returns a string appropriate for the type of node.

            - nodeType (number; required):
                Returns the type of node.

            - nodeValue (string; required)

            - nonce (string; optional)

            - normalize (required):
                Removes empty exclusive Text nodes and concatenates
                the data of remaining contiguous exclusive Text nodes
                into the first of their nodes.

            - offsetHeight (number; required)

            - offsetLeft (number; required)

            - offsetParent (a list of or a singular dash component, string or number; required)

            - offsetTop (number; required)

            - offsetWidth (number; required)

            - onabort (required):
                Fires when the user aborts the download. @,param,ev,
                ,The event.

            - onanimationcancel (required)

            - onanimationend (required)

            - onanimationiteration (required)

            - onanimationstart (required)

            - onauxclick (required)

            - onbeforeinput (required)

            - onblur (required):
                Fires when the object loses the input focus.
                @,param,ev, ,The focus event.

            - oncancel (required)

            - oncanplay (required):
                Occurs when playback is possible, but would require
                further buffering. @,param,ev, ,The event.

            - oncanplaythrough (required)

            - onchange (required):
                Fires when the contents of the object or selection
                have changed. @,param,ev, ,The event.

            - onclick (required):
                Fires when the user clicks the left mouse button on
                the object @,param,ev, ,The mouse event.

            - onclose (required)

            - oncontextmenu (required):
                Fires when the user clicks the right mouse button in
                the client area, opening the context menu. @,param,ev,
                ,The mouse event.

            - oncopy (required)

            - oncuechange (required)

            - oncut (required)

            - ondblclick (required):
                Fires when the user double-clicks the object.
                @,param,ev, ,The mouse event.

            - ondrag (required):
                Fires on the source object continuously during a drag
                operation. @,param,ev, ,The event.

            - ondragend (required):
                Fires on the source object when the user releases the
                mouse at the close of a drag operation. @,param,ev,
                ,The event.

            - ondragenter (required):
                Fires on the target element when the user drags the
                object to a valid drop target. @,param,ev, ,The drag
                event.

            - ondragleave (required):
                Fires on the target object when the user moves the
                mouse out of a valid drop target during a drag
                operation. @,param,ev, ,The drag event.

            - ondragover (required):
                Fires on the target element continuously while the
                user drags the object over a valid drop target.
                @,param,ev, ,The event.

            - ondragstart (required):
                Fires on the source object when the user starts to
                drag a text selection or selected object. @,param,ev,
                ,The event.

            - ondrop (required)

            - ondurationchange (required):
                Occurs when the duration attribute is updated.
                @,param,ev, ,The event.

            - onemptied (required):
                Occurs when the media element is reset to its initial
                state. @,param,ev, ,The event.

            - onended (required):
                Occurs when the end of playback is reached.
                @,param,ev, ,The event.

            - onerror (dict; required):
                Fires when an error occurs during object loading.
                @,param,ev, ,The event.

                `onerror` is a dict with keys:


            - onfocus (required):
                Fires when the object receives focus. @,param,ev, ,The
                event.

            - onformdata (required)

            - onfullscreenchange (required)

            - onfullscreenerror (required)

            - ongotpointercapture (required)

            - oninput (required)

            - oninvalid (required)

            - onkeydown (required):
                Fires when the user presses a key. @,param,ev, ,The
                keyboard event.

            - onkeypress (required):
                Fires when the user presses an alphanumeric key.
                @,param,ev, ,The event. @,deprecated.

            - onkeyup (required):
                Fires when the user releases a key. @,param,ev, ,The
                keyboard event.

            - onload (required):
                Fires immediately after the browser loads the object.
                @,param,ev, ,The event.

            - onloadeddata (required):
                Occurs when media data is loaded at the current
                playback position. @,param,ev, ,The event.

            - onloadedmetadata (required):
                Occurs when the duration and dimensions of the media
                have been determined. @,param,ev, ,The event.

            - onloadstart (required):
                Occurs when Internet Explorer begins looking for media
                data. @,param,ev, ,The event.

            - onlostpointercapture (required)

            - onmousedown (required):
                Fires when the user clicks the object with either
                mouse button. @,param,ev, ,The mouse event.

            - onmouseenter (required)

            - onmouseleave (required)

            - onmousemove (required):
                Fires when the user moves the mouse over the object.
                @,param,ev, ,The mouse event.

            - onmouseout (required):
                Fires when the user moves the mouse pointer outside
                the boundaries of the object. @,param,ev, ,The mouse
                event.

            - onmouseover (required):
                Fires when the user moves the mouse pointer into the
                object. @,param,ev, ,The mouse event.

            - onmouseup (required):
                Fires when the user releases a mouse button while the
                mouse is over the object. @,param,ev, ,The mouse
                event.

            - onpaste (required)

            - onpause (required):
                Occurs when playback is paused. @,param,ev, ,The
                event.

            - onplay (required):
                Occurs when the play method is requested. @,param,ev,
                ,The event.

            - onplaying (required):
                Occurs when the audio or video has started playing.
                @,param,ev, ,The event.

            - onpointercancel (required)

            - onpointerdown (required)

            - onpointerenter (required)

            - onpointerleave (required)

            - onpointermove (required)

            - onpointerout (required)

            - onpointerover (required)

            - onpointerup (required)

            - onprogress (required):
                Occurs to indicate progress while downloading media
                data. @,param,ev, ,The event.

            - onratechange (required):
                Occurs when the playback rate is increased or
                decreased. @,param,ev, ,The event.

            - onreset (required):
                Fires when the user resets a form. @,param,ev, ,The
                event.

            - onresize (required)

            - onscroll (required):
                Fires when the user repositions the scroll box in the
                scroll bar on the object. @,param,ev, ,The event.

            - onsecuritypolicyviolation (required)

            - onseeked (required):
                Occurs when the seek operation ends. @,param,ev, ,The
                event.

            - onseeking (required):
                Occurs when the current playback position is moved.
                @,param,ev, ,The event.

            - onselect (required):
                Fires when the current selection changes. @,param,ev,
                ,The event.

            - onselectionchange (required)

            - onselectstart (required)

            - onslotchange (required)

            - onstalled (required):
                Occurs when the download has stopped. @,param,ev, ,The
                event.

            - onsubmit (required)

            - onsuspend (required):
                Occurs if the load operation has been intentionally
                halted. @,param,ev, ,The event.

            - ontimeupdate (required):
                Occurs to indicate the current playback position.
                @,param,ev, ,The event.

            - ontoggle (required)

            - ontouchcancel (optional)

            - ontouchend (optional)

            - ontouchmove (optional)

            - ontouchstart (optional)

            - ontransitioncancel (required)

            - ontransitionend (required)

            - ontransitionrun (required)

            - ontransitionstart (required)

            - onvolumechange (required):
                Occurs when the volume is changed, or playback is
                muted or unmuted. @,param,ev, ,The event.

            - onwaiting (required):
                Occurs when playback stops because the next frame of a
                video resource is not available. @,param,ev, ,The
                event.

            - onwebkitanimationend (required)

            - onwebkitanimationiteration (required)

            - onwebkitanimationstart (required)

            - onwebkittransitionend (required)

            - onwheel (required)

            - outerHTML (string; required)

            - outerText (string; required)

            - ownerDocument (boolean | number | string | dict | list; required)

            - parentElement (boolean | number | string | dict | list; required):
                Returns the parent element.

            - parentNode (boolean | number | string | dict | list; required):
                Returns the parent.

            - part (dict with strings as keys and values of type string; required)

            - prefix (string; required):
                Returns the namespace prefix.

            - prepend (required):
                Inserts nodes before the first child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - previousElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first preceding sibling that is an
                element, and None otherwise.

            - previousSibling (boolean | number | string | dict | list; required):
                Returns the previous sibling.

            - querySelector (dict; required):
                Returns the first element that is a descendant of node
                that matches selectors.

                `querySelector` is a dict with keys:


            - querySelectorAll (dict; required):
                Returns all element descendants of node that match
                selectors.

                `querySelectorAll` is a dict with keys:


            - releasePointerCapture (required)

            - remove (required):
                Removes node.

            - removeAttribute (required):
                Removes element's first attribute whose qualified name
                is qualifiedName.

            - removeAttributeNS (required):
                Removes element's attribute whose namespace is
                namespace and local name is localName.

            - removeAttributeNode (required)

            - removeChild (required)

            - removeEventListener (required)

            - replaceChild (required)

            - replaceChildren (required):
                Replace all children of node with nodes, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - replaceWith (required):
                Replaces node with nodes, while replacing strings in
                nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - requestFullscreen (required):
                Displays element fullscreen and resolves promise when
                done.  When supplied, options's navigationUI member
                indicates whether showing navigation UI while in
                fullscreen is preferred or not. If set to \"show\",
                navigation simplicity is preferred over screen space,
                and if set to \"hide\", more screen space is
                preferred. User agents are always free to honor user
                preference over the application's. The default value
                \"auto\" indicates no application preference.

            - requestPointerLock (required)

            - role (string; required)

            - scroll (dict; required)

                `scroll` is a dict with keys:


            - scrollBy (dict; required)

                `scrollBy` is a dict with keys:


            - scrollHeight (number; required)

            - scrollIntoView (required)

            - scrollLeft (number; required)

            - scrollTo (dict; required)

                `scrollTo` is a dict with keys:


            - scrollTop (number; required)

            - scrollWidth (number; required)

            - setAttribute (required):
                Sets the value of element's first attribute whose
                qualified name is qualifiedName to value.

            - setAttributeNS (required):
                Sets the value of element's attribute whose namespace
                is namespace and local name is localName to value.

            - setAttributeNode (required)

            - setAttributeNodeNS (required)

            - setPointerCapture (required)

            - shadowRoot (boolean | number | string | dict | list; required):
                Returns element's shadow root, if any, and if shadow
                root's mode is \"open\", and None otherwise.

            - slot (string; required):
                Returns the value of element's slot content attribute.
                Can be set to change it.

            - spellcheck (boolean; required)

            - style (dict with strings as keys and values of type string; required)

            - tabIndex (number; required)

            - tagName (string; required):
                Returns the HTML-uppercased qualified name.

            - textContent (string; required)

            - title (string; required)

            - toggleAttribute (required):
                If force is not given, \"toggles\" qualifiedName,
                removing it if it is present and adding it if it is
                not present. If force is True, adds qualifiedName. If
                force is False, removes qualifiedName.  Returns True
                if qualifiedName is now present, and False otherwise.

            - translate (boolean; required)

            - webkitMatchesSelector (required)

        - defaultDate (dict; optional):
            The initial date to view when first opened.

            `defaultDate` is a dict with keys:

            - __@toPrimitive@4735 (dict; required):
                Converts a Date object to a string.   Converts a Date
                object to a number.   Converts a Date object to a
                string or number. @,param,hint, ,The strings
                \"number\", \"string\", or \"default\" to specify what
                primitive to return. @,throws,{TypeError} If 'hint'
                was given something other than \"number\", \"string\",
                or \"default\". @,returns,A number if 'hint' was
                \"number\", a string if 'hint' was \"string\" or
                \"default\".

                `__@toPrimitive@4735` is a dict with keys:


            - getDate (required):
                Gets the day-of-the-month, using local time.

            - getDay (required):
                Gets the day of the week, using local time.

            - getFullYear (required):
                Gets the year, using local time.

            - getHours (required):
                Gets the hours in a date, using local time.

            - getMilliseconds (required):
                Gets the milliseconds of a Date, using local time.

            - getMinutes (required):
                Gets the minutes of a Date object, using local time.

            - getMonth (required):
                Gets the month, using local time.

            - getSeconds (required):
                Gets the seconds of a Date object, using local time.

            - getTime (required):
                Gets the time value in milliseconds.

            - getTimezoneOffset (required):
                Gets the difference in minutes between the time on the
                local computer and Universal Coordinated Time (UTC).

            - getUTCDate (required):
                Gets the day-of-the-month, using Universal Coordinated
                Time (UTC).

            - getUTCDay (required):
                Gets the day of the week using Universal Coordinated
                Time (UTC).

            - getUTCFullYear (required):
                Gets the year using Universal Coordinated Time (UTC).

            - getUTCHours (required):
                Gets the hours value in a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMilliseconds (required):
                Gets the milliseconds of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMinutes (required):
                Gets the minutes of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMonth (required):
                Gets the month of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCSeconds (required):
                Gets the seconds of a Date object using Universal
                Coordinated Time (UTC).

            - getVarDate (required)

            - setDate (required):
                Sets the numeric day-of-the-month value of the Date
                object using local time. @,param,date, ,A numeric
                value equal to the day of the month.

            - setFullYear (required):
                Sets the year of the Date object using local time.
                @,param,year, ,A numeric value for the year.
                @,param,month, ,A zero-based numeric value for the
                month (0 for January, 11 for December). Must be
                specified if numDate is specified. @,param,date, ,A
                numeric value equal for the day of the month.

            - setHours (required):
                Sets the hour value in the Date object using local
                time. @,param,hours, ,A numeric value equal to the
                hours value. @,param,min, ,A numeric value equal to
                the minutes value. @,param,sec, ,A numeric value equal
                to the seconds value. @,param,ms, ,A numeric value
                equal to the milliseconds value.

            - setMilliseconds (required):
                Sets the milliseconds value in the Date object using
                local time. @,param,ms, ,A numeric value equal to the
                millisecond value.

            - setMinutes (required):
                Sets the minutes value in the Date object using local
                time. @,param,min, ,A numeric value equal to the
                minutes value. @,param,sec, ,A numeric value equal to
                the seconds value. @,param,ms, ,A numeric value equal
                to the milliseconds value.

            - setMonth (required):
                Sets the month value in the Date object using local
                time. @,param,month, ,A numeric value equal to the
                month. The value for January is 0, and other month
                values follow consecutively. @,param,date, ,A numeric
                value representing the day of the month. If this value
                is not supplied, the value from a call to the getDate
                method is used.

            - setSeconds (required):
                Sets the seconds value in the Date object using local
                time. @,param,sec, ,A numeric value equal to the
                seconds value. @,param,ms, ,A numeric value equal to
                the milliseconds value.

            - setTime (required):
                Sets the date and time value in the Date object.
                @,param,time, ,A numeric value representing the number
                of elapsed milliseconds since midnight, January 1,
                1970 GMT.

            - setUTCDate (required):
                Sets the numeric day of the month in the Date object
                using Universal Coordinated Time (UTC). @,param,date,
                ,A numeric value equal to the day of the month.

            - setUTCFullYear (required):
                Sets the year value in the Date object using Universal
                Coordinated Time (UTC). @,param,year, ,A numeric value
                equal to the year. @,param,month, ,A numeric value
                equal to the month. The value for January is 0, and
                other month values follow consecutively. Must be
                supplied if numDate is supplied. @,param,date, ,A
                numeric value equal to the day of the month.

            - setUTCHours (required):
                Sets the hours value in the Date object using
                Universal Coordinated Time (UTC). @,param,hours, ,A
                numeric value equal to the hours value. @,param,min,
                ,A numeric value equal to the minutes value.
                @,param,sec, ,A numeric value equal to the seconds
                value. @,param,ms, ,A numeric value equal to the
                milliseconds value.

            - setUTCMilliseconds (required):
                Sets the milliseconds value in the Date object using
                Universal Coordinated Time (UTC). @,param,ms, ,A
                numeric value equal to the millisecond value.

            - setUTCMinutes (required):
                Sets the minutes value in the Date object using
                Universal Coordinated Time (UTC). @,param,min, ,A
                numeric value equal to the minutes value. @,param,sec,
                ,A numeric value equal to the seconds value.
                @,param,ms, ,A numeric value equal to the milliseconds
                value.

            - setUTCMonth (required):
                Sets the month value in the Date object using
                Universal Coordinated Time (UTC). @,param,month, ,A
                numeric value equal to the month. The value for
                January is 0, and other month values follow
                consecutively. @,param,date, ,A numeric value
                representing the day of the month. If it is not
                supplied, the value from a call to the getUTCDate
                method is used.

            - setUTCSeconds (required):
                Sets the seconds value in the Date object using
                Universal Coordinated Time (UTC). @,param,sec, ,A
                numeric value equal to the seconds value. @,param,ms,
                ,A numeric value equal to the milliseconds value.

            - toDateString (required):
                Returns a date as a string value.

            - toISOString (required):
                Returns a date as a string value in ISO format.

            - toJSON (required):
                Used by the JSON.stringify method to enable the
                transformation of an object's data for JavaScript
                Object Notation (JSON) serialization.

            - toLocaleDateString (dict; required):
                Returns a date as a string value appropriate to the
                host environment's current locale.   Converts a date
                to a string by using the current or specified locale.
                @,param,locales, ,A locale string or array of locale
                strings that contain one or more language or locale
                tags. If you include more than one locale string, list
                them in descending order of priority so that the first
                entry is the preferred locale. If you omit this
                parameter, the default locale of the JavaScript
                runtime is used. @,param,options, ,An object that
                contains one or more properties that specify
                comparison options. @,param,locales, ,A locale string,
                array of locale strings, Intl.Locale object, or array
                of Intl.Locale objects that contain one or more
                language or locale tags. If you include more than one
                locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleDateString` is a dict with keys:


            - toLocaleString (dict; optional):
                Returns a value as a string value appropriate to the
                host environment's current locale.   Converts a date
                and time to a string by using the current or specified
                locale. @,param,locales, ,A locale string or array of
                locale strings that contain one or more language or
                locale tags. If you include more than one locale
                string, list them in descending order of priority so
                that the first entry is the preferred locale. If you
                omit this parameter, the default locale of the
                JavaScript runtime is used. @,param,options, ,An
                object that contains one or more properties that
                specify comparison options. @,param,locales, ,A locale
                string, array of locale strings, Intl.Locale object,
                or array of Intl.Locale objects that contain one or
                more language or locale tags. If you include more than
                one locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleString` is a dict with keys:


            - toLocaleTimeString (dict; required):
                Returns a time as a string value appropriate to the
                host environment's current locale.   Converts a time
                to a string by using the current or specified locale.
                @,param,locales, ,A locale string or array of locale
                strings that contain one or more language or locale
                tags. If you include more than one locale string, list
                them in descending order of priority so that the first
                entry is the preferred locale. If you omit this
                parameter, the default locale of the JavaScript
                runtime is used. @,param,options, ,An object that
                contains one or more properties that specify
                comparison options. @,param,locales, ,A locale string,
                array of locale strings, Intl.Locale object, or array
                of Intl.Locale objects that contain one or more
                language or locale tags. If you include more than one
                locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleTimeString` is a dict with keys:


            - toString (optional):
                Returns a string representation of a date. The format
                of the string depends on the locale.

            - toTimeString (required):
                Returns a time as a string value.

            - toUTCString (required):
                Returns a date converted to a string using Universal
                Coordinated Time (UTC).

            - valueOf (optional):
                Returns the stored time value in milliseconds since
                midnight, January 1, 1970 UTC.

        - disableDayFn (optional):
            Callback function that gets passed a Date object for each
            day in view. Should return True to disable selection of
            that day.

        - disableWeekends (boolean; optional):
            Disallow selection of Saturdays and Sundays.

        - enableSelectionDaysInNextAndPreviousMonths (boolean; optional):
            Allows user to select date that is in the next or previous
            months (default: False).

        - events (list of strings; optional):
            Array of dates that you would like to differentiate from
            regular days (e.g. ['Sat Jun 28 2017', 'Sun Jun 29 2017',
            'Tue Jul 01 2017',]).

        - field (dict; optional):
            Bind the datepicker to a form field.

            `field` is a dict with keys:

            - ATTRIBUTE_NODE (number; required)

            - CDATA_SECTION_NODE (number; required):
                node is a CDATASection node.

            - COMMENT_NODE (number; required):
                node is a Comment node.

            - DOCUMENT_FRAGMENT_NODE (number; required):
                node is a DocumentFragment node.

            - DOCUMENT_NODE (number; required):
                node is a document.

            - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                Set when other is a descendant of node.

            - DOCUMENT_POSITION_CONTAINS (number; required):
                Set when other is an ancestor of node.

            - DOCUMENT_POSITION_DISCONNECTED (number; required):
                Set when node and other are not in the same tree.

            - DOCUMENT_POSITION_FOLLOWING (number; required):
                Set when other is following node.

            - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

            - DOCUMENT_POSITION_PRECEDING (number; required):
                Set when other is preceding node.

            - DOCUMENT_TYPE_NODE (number; required):
                node is a doctype.

            - ELEMENT_NODE (number; required):
                node is an element.

            - ENTITY_NODE (number; required)

            - ENTITY_REFERENCE_NODE (number; required)

            - NOTATION_NODE (number; required)

            - PROCESSING_INSTRUCTION_NODE (number; required):
                node is a ProcessingInstruction node.

            - TEXT_NODE (number; required):
                node is a Text node.

            - accessKey (string; required)

            - accessKeyLabel (string; required)

            - addEventListener (required)

            - after (required):
                Inserts nodes just after node, while replacing strings
                in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - animate (required)

            - append (required):
                Inserts nodes after the last child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - appendChild (required)

            - ariaAtomic (string; required)

            - ariaAutoComplete (string; required)

            - ariaBusy (string; required)

            - ariaChecked (string; required)

            - ariaColCount (string; required)

            - ariaColIndex (string; required)

            - ariaColIndexText (string; required)

            - ariaColSpan (string; required)

            - ariaCurrent (string; required)

            - ariaDisabled (string; required)

            - ariaExpanded (string; required)

            - ariaHasPopup (string; required)

            - ariaHidden (string; required)

            - ariaInvalid (string; required)

            - ariaKeyShortcuts (string; required)

            - ariaLabel (string; required)

            - ariaLevel (string; required)

            - ariaLive (string; required)

            - ariaModal (string; required)

            - ariaMultiLine (string; required)

            - ariaMultiSelectable (string; required)

            - ariaOrientation (string; required)

            - ariaPlaceholder (string; required)

            - ariaPosInSet (string; required)

            - ariaPressed (string; required)

            - ariaReadOnly (string; required)

            - ariaRequired (string; required)

            - ariaRoleDescription (string; required)

            - ariaRowCount (string; required)

            - ariaRowIndex (string; required)

            - ariaRowIndexText (string; required)

            - ariaRowSpan (string; required)

            - ariaSelected (string; required)

            - ariaSetSize (string; required)

            - ariaSort (string; required)

            - ariaValueMax (string; required)

            - ariaValueMin (string; required)

            - ariaValueNow (string; required)

            - ariaValueText (string; required)

            - assignedSlot (dict; required)

                `assignedSlot` is a dict with keys:

                - ATTRIBUTE_NODE (number; required)

                - CDATA_SECTION_NODE (number; required):
                    node is a CDATASection node.

                - COMMENT_NODE (number; required):
                    node is a Comment node.

                - DOCUMENT_FRAGMENT_NODE (number; required):
                    node is a DocumentFragment node.

                - DOCUMENT_NODE (number; required):
                    node is a document.

                - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                    Set when other is a descendant of node.

                - DOCUMENT_POSITION_CONTAINS (number; required):
                    Set when other is an ancestor of node.

                - DOCUMENT_POSITION_DISCONNECTED (number; required):
                    Set when node and other are not in the same tree.

                - DOCUMENT_POSITION_FOLLOWING (number; required):
                    Set when other is following node.

                - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

                - DOCUMENT_POSITION_PRECEDING (number; required):
                    Set when other is preceding node.

                - DOCUMENT_TYPE_NODE (number; required):
                    node is a doctype.

                - ELEMENT_NODE (number; required):
                    node is an element.

                - ENTITY_NODE (number; required)

                - ENTITY_REFERENCE_NODE (number; required)

                - NOTATION_NODE (number; required)

                - PROCESSING_INSTRUCTION_NODE (number; required):
                    node is a ProcessingInstruction node.

                - TEXT_NODE (number; required):
                    node is a Text node.

                - accessKey (string; required)

                - accessKeyLabel (string; required)

                - addEventListener (required)

                - after (required):
                    Inserts nodes just after node, while replacing
                    strings in nodes with equivalent Text nodes.
                    Throws a \"HierarchyRequestError\" DOMException if
                    the constraints of the node tree are violated.

                - animate (required)

                - append (required):
                    Inserts nodes after the last child of node, while
                    replacing strings in nodes with equivalent Text
                    nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - appendChild (required)

                - ariaAtomic (string; required)

                - ariaAutoComplete (string; required)

                - ariaBusy (string; required)

                - ariaChecked (string; required)

                - ariaColCount (string; required)

                - ariaColIndex (string; required)

                - ariaColIndexText (string; required)

                - ariaColSpan (string; required)

                - ariaCurrent (string; required)

                - ariaDisabled (string; required)

                - ariaExpanded (string; required)

                - ariaHasPopup (string; required)

                - ariaHidden (string; required)

                - ariaInvalid (string; required)

                - ariaKeyShortcuts (string; required)

                - ariaLabel (string; required)

                - ariaLevel (string; required)

                - ariaLive (string; required)

                - ariaModal (string; required)

                - ariaMultiLine (string; required)

                - ariaMultiSelectable (string; required)

                - ariaOrientation (string; required)

                - ariaPlaceholder (string; required)

                - ariaPosInSet (string; required)

                - ariaPressed (string; required)

                - ariaReadOnly (string; required)

                - ariaRequired (string; required)

                - ariaRoleDescription (string; required)

                - ariaRowCount (string; required)

                - ariaRowIndex (string; required)

                - ariaRowIndexText (string; required)

                - ariaRowSpan (string; required)

                - ariaSelected (string; required)

                - ariaSetSize (string; required)

                - ariaSort (string; required)

                - ariaValueMax (string; required)

                - ariaValueMin (string; required)

                - ariaValueNow (string; required)

                - ariaValueText (string; required)

                - assign (required)

                - assignedElements (required)

                - assignedNodes (required)

                - assignedSlot (boolean | number | string | dict | list; required)

                - attachInternals (required)

                - attachShadow (required):
                    Creates a shadow root for element and returns it.

                - attributes (dict; required)

                    `attributes` is a dict with strings as keys and
                    values of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

                - autocapitalize (string; required)

                - autofocus (boolean; required)

                - baseURI (string; required):
                    Returns node's node document's document base URL.

                - before (required):
                    Inserts nodes just before node, while replacing
                    strings in nodes with equivalent Text nodes.
                    Throws a \"HierarchyRequestError\" DOMException if
                    the constraints of the node tree are violated.

                - blur (required)

                - childElementCount (number; required)

                - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                    Returns the children.

                - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                    Returns the child elements.

                - classList (dict with strings as keys and values of type string; required):
                    Allows for manipulation of element's class content
                    attribute as a set of whitespace-separated tokens
                    through a DOMTokenList object.

                - className (string; required):
                    Returns the value of element's class content
                    attribute. Can be set to change it.

                - click (required)

                - clientHeight (number; required)

                - clientLeft (number; required)

                - clientTop (number; required)

                - clientWidth (number; required)

                - cloneNode (required):
                    Returns a copy of node. If deep is True, the copy
                    also includes the node's descendants.

                - closest (dict; required):
                    Returns the first (starting at element) inclusive
                    ancestor that matches selectors, and None
                    otherwise.

                    `closest` is a dict with keys:


                - compareDocumentPosition (required):
                    Returns a bitmask indicating the position of other
                    relative to node.

                - contains (required):
                    Returns True if other is an inclusive descendant
                    of node, and False otherwise.

                - contentEditable (string; required)

                - dataset (dict with strings as keys and values of type string; required)

                - dir (string; required)

                - dispatchEvent (required):
                    Dispatches a synthetic event event to target and
                    returns True if either event's cancelable
                    attribute value is False or its preventDefault()
                    method was not invoked, and False otherwise.

                - draggable (boolean; required)

                - enterKeyHint (string; required)

                - firstChild (boolean | number | string | dict | list; required):
                    Returns the first child.

                - firstElementChild (a list of or a singular dash component, string or number; required):
                    Returns the first child that is an element, and
                    None otherwise.

                - focus (required)

                - getAnimations (required)

                - getAttribute (required):
                    Returns element's first attribute whose qualified
                    name is qualifiedName, and None if there is no
                    such attribute otherwise.

                - getAttributeNS (required):
                    Returns element's attribute whose namespace is
                    namespace and local name is localName, and None if
                    there is no such attribute otherwise.

                - getAttributeNames (required):
                    Returns the qualified names of all element's
                    attributes. Can contain duplicates.

                - getAttributeNode (required)

                - getAttributeNodeNS (required)

                - getBoundingClientRect (required)

                - getClientRects (required)

                - getElementsByClassName (required):
                    Returns a HTMLCollection of the elements in the
                    object on which the method was invoked (a document
                    or an element) that have all the classes given by
                    classNames. The classNames argument is interpreted
                    as a space-separated list of classes.

                - getElementsByTagName (dict; required)

                    `getElementsByTagName` is a dict with keys:


                - getElementsByTagNameNS (dict; required)

                    `getElementsByTagNameNS` is a dict with keys:


                - getRootNode (required):
                    Returns node's root.

                - hasAttribute (required):
                    Returns True if element has an attribute whose
                    qualified name is qualifiedName, and False
                    otherwise.

                - hasAttributeNS (required):
                    Returns True if element has an attribute whose
                    namespace is namespace and local name is
                    localName.

                - hasAttributes (required):
                    Returns True if element has attributes, and False
                    otherwise.

                - hasChildNodes (required):
                    Returns whether node has children.

                - hasPointerCapture (required)

                - hidden (boolean; required)

                - id (string; required):
                    Returns the value of element's id content
                    attribute. Can be set to change it.

                - inert (boolean; required)

                - innerHTML (string; required)

                - innerText (string; required)

                - inputMode (string; required)

                - insertAdjacentElement (required)

                - insertAdjacentHTML (required)

                - insertAdjacentText (required)

                - insertBefore (required)

                - isConnected (boolean; required):
                    Returns True if node is connected and False
                    otherwise.

                - isContentEditable (boolean; required)

                - isDefaultNamespace (required)

                - isEqualNode (required):
                    Returns whether node and otherNode have the same
                    properties.

                - isSameNode (required)

                - lang (string; required)

                - lastChild (boolean | number | string | dict | list; required):
                    Returns the last child.

                - lastElementChild (a list of or a singular dash component, string or number; required):
                    Returns the last child that is an element, and
                    None otherwise.

                - localName (string; required):
                    Returns the local name.

                - lookupNamespaceURI (required)

                - lookupPrefix (required)

                - matches (required):
                    Returns True if matching selectors against
                    element's root yields element, and False
                    otherwise.

                - name (string; required)

                - namespaceURI (string; required):
                    Returns the namespace.

                - nextElementSibling (a list of or a singular dash component, string or number; required):
                    Returns the first following sibling that is an
                    element, and None otherwise.

                - nextSibling (boolean | number | string | dict | list; required):
                    Returns the next sibling.

                - nodeName (string; required):
                    Returns a string appropriate for the type of node.

                - nodeType (number; required):
                    Returns the type of node.

                - nodeValue (string; required)

                - nonce (string; optional)

                - normalize (required):
                    Removes empty exclusive Text nodes and
                    concatenates the data of remaining contiguous
                    exclusive Text nodes into the first of their
                    nodes.

                - offsetHeight (number; required)

                - offsetLeft (number; required)

                - offsetParent (a list of or a singular dash component, string or number; required)

                - offsetTop (number; required)

                - offsetWidth (number; required)

                - onabort (required):
                    Fires when the user aborts the download.
                    @,param,ev, ,The event.

                - onanimationcancel (required)

                - onanimationend (required)

                - onanimationiteration (required)

                - onanimationstart (required)

                - onauxclick (required)

                - onbeforeinput (required)

                - onblur (required):
                    Fires when the object loses the input focus.
                    @,param,ev, ,The focus event.

                - oncancel (required)

                - oncanplay (required):
                    Occurs when playback is possible, but would
                    require further buffering. @,param,ev, ,The event.

                - oncanplaythrough (required)

                - onchange (required):
                    Fires when the contents of the object or selection
                    have changed. @,param,ev, ,The event.

                - onclick (required):
                    Fires when the user clicks the left mouse button
                    on the object @,param,ev, ,The mouse event.

                - onclose (required)

                - oncontextmenu (required):
                    Fires when the user clicks the right mouse button
                    in the client area, opening the context menu.
                    @,param,ev, ,The mouse event.

                - oncopy (required)

                - oncuechange (required)

                - oncut (required)

                - ondblclick (required):
                    Fires when the user double-clicks the object.
                    @,param,ev, ,The mouse event.

                - ondrag (required):
                    Fires on the source object continuously during a
                    drag operation. @,param,ev, ,The event.

                - ondragend (required):
                    Fires on the source object when the user releases
                    the mouse at the close of a drag operation.
                    @,param,ev, ,The event.

                - ondragenter (required):
                    Fires on the target element when the user drags
                    the object to a valid drop target. @,param,ev,
                    ,The drag event.

                - ondragleave (required):
                    Fires on the target object when the user moves the
                    mouse out of a valid drop target during a drag
                    operation. @,param,ev, ,The drag event.

                - ondragover (required):
                    Fires on the target element continuously while the
                    user drags the object over a valid drop target.
                    @,param,ev, ,The event.

                - ondragstart (required):
                    Fires on the source object when the user starts to
                    drag a text selection or selected object.
                    @,param,ev, ,The event.

                - ondrop (required)

                - ondurationchange (required):
                    Occurs when the duration attribute is updated.
                    @,param,ev, ,The event.

                - onemptied (required):
                    Occurs when the media element is reset to its
                    initial state. @,param,ev, ,The event.

                - onended (required):
                    Occurs when the end of playback is reached.
                    @,param,ev, ,The event.

                - onerror (dict; required):
                    Fires when an error occurs during object loading.
                    @,param,ev, ,The event.

                    `onerror` is a dict with keys:


                - onfocus (required):
                    Fires when the object receives focus. @,param,ev,
                    ,The event.

                - onformdata (required)

                - onfullscreenchange (required)

                - onfullscreenerror (required)

                - ongotpointercapture (required)

                - oninput (required)

                - oninvalid (required)

                - onkeydown (required):
                    Fires when the user presses a key. @,param,ev,
                    ,The keyboard event.

                - onkeypress (required):
                    Fires when the user presses an alphanumeric key.
                    @,param,ev, ,The event. @,deprecated.

                - onkeyup (required):
                    Fires when the user releases a key. @,param,ev,
                    ,The keyboard event.

                - onload (required):
                    Fires immediately after the browser loads the
                    object. @,param,ev, ,The event.

                - onloadeddata (required):
                    Occurs when media data is loaded at the current
                    playback position. @,param,ev, ,The event.

                - onloadedmetadata (required):
                    Occurs when the duration and dimensions of the
                    media have been determined. @,param,ev, ,The
                    event.

                - onloadstart (required):
                    Occurs when Internet Explorer begins looking for
                    media data. @,param,ev, ,The event.

                - onlostpointercapture (required)

                - onmousedown (required):
                    Fires when the user clicks the object with either
                    mouse button. @,param,ev, ,The mouse event.

                - onmouseenter (required)

                - onmouseleave (required)

                - onmousemove (required):
                    Fires when the user moves the mouse over the
                    object. @,param,ev, ,The mouse event.

                - onmouseout (required):
                    Fires when the user moves the mouse pointer
                    outside the boundaries of the object. @,param,ev,
                    ,The mouse event.

                - onmouseover (required):
                    Fires when the user moves the mouse pointer into
                    the object. @,param,ev, ,The mouse event.

                - onmouseup (required):
                    Fires when the user releases a mouse button while
                    the mouse is over the object. @,param,ev, ,The
                    mouse event.

                - onpaste (required)

                - onpause (required):
                    Occurs when playback is paused. @,param,ev, ,The
                    event.

                - onplay (required):
                    Occurs when the play method is requested.
                    @,param,ev, ,The event.

                - onplaying (required):
                    Occurs when the audio or video has started
                    playing. @,param,ev, ,The event.

                - onpointercancel (required)

                - onpointerdown (required)

                - onpointerenter (required)

                - onpointerleave (required)

                - onpointermove (required)

                - onpointerout (required)

                - onpointerover (required)

                - onpointerup (required)

                - onprogress (required):
                    Occurs to indicate progress while downloading
                    media data. @,param,ev, ,The event.

                - onratechange (required):
                    Occurs when the playback rate is increased or
                    decreased. @,param,ev, ,The event.

                - onreset (required):
                    Fires when the user resets a form. @,param,ev,
                    ,The event.

                - onresize (required)

                - onscroll (required):
                    Fires when the user repositions the scroll box in
                    the scroll bar on the object. @,param,ev, ,The
                    event.

                - onsecuritypolicyviolation (required)

                - onseeked (required):
                    Occurs when the seek operation ends. @,param,ev,
                    ,The event.

                - onseeking (required):
                    Occurs when the current playback position is
                    moved. @,param,ev, ,The event.

                - onselect (required):
                    Fires when the current selection changes.
                    @,param,ev, ,The event.

                - onselectionchange (required)

                - onselectstart (required)

                - onslotchange (required)

                - onstalled (required):
                    Occurs when the download has stopped. @,param,ev,
                    ,The event.

                - onsubmit (required)

                - onsuspend (required):
                    Occurs if the load operation has been
                    intentionally halted. @,param,ev, ,The event.

                - ontimeupdate (required):
                    Occurs to indicate the current playback position.
                    @,param,ev, ,The event.

                - ontoggle (required)

                - ontouchcancel (optional)

                - ontouchend (optional)

                - ontouchmove (optional)

                - ontouchstart (optional)

                - ontransitioncancel (required)

                - ontransitionend (required)

                - ontransitionrun (required)

                - ontransitionstart (required)

                - onvolumechange (required):
                    Occurs when the volume is changed, or playback is
                    muted or unmuted. @,param,ev, ,The event.

                - onwaiting (required):
                    Occurs when playback stops because the next frame
                    of a video resource is not available. @,param,ev,
                    ,The event.

                - onwebkitanimationend (required)

                - onwebkitanimationiteration (required)

                - onwebkitanimationstart (required)

                - onwebkittransitionend (required)

                - onwheel (required)

                - outerHTML (string; required)

                - outerText (string; required)

                - ownerDocument (boolean | number | string | dict | list; required)

                - parentElement (boolean | number | string | dict | list; required):
                    Returns the parent element.

                - parentNode (boolean | number | string | dict | list; required):
                    Returns the parent.

                - part (dict with strings as keys and values of type string; required)

                - prefix (string; required):
                    Returns the namespace prefix.

                - prepend (required):
                    Inserts nodes before the first child of node,
                    while replacing strings in nodes with equivalent
                    Text nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - previousElementSibling (a list of or a singular dash component, string or number; required):
                    Returns the first preceding sibling that is an
                    element, and None otherwise.

                - previousSibling (boolean | number | string | dict | list; required):
                    Returns the previous sibling.

                - querySelector (dict; required):
                    Returns the first element that is a descendant of
                    node that matches selectors.

                    `querySelector` is a dict with keys:


                - querySelectorAll (dict; required):
                    Returns all element descendants of node that match
                    selectors.

                    `querySelectorAll` is a dict with keys:


                - releasePointerCapture (required)

                - remove (required):
                    Removes node.

                - removeAttribute (required):
                    Removes element's first attribute whose qualified
                    name is qualifiedName.

                - removeAttributeNS (required):
                    Removes element's attribute whose namespace is
                    namespace and local name is localName.

                - removeAttributeNode (required)

                - removeChild (required)

                - removeEventListener (required)

                - replaceChild (required)

                - replaceChildren (required):
                    Replace all children of node with nodes, while
                    replacing strings in nodes with equivalent Text
                    nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - replaceWith (required):
                    Replaces node with nodes, while replacing strings
                    in nodes with equivalent Text nodes.  Throws a
                    \"HierarchyRequestError\" DOMException if the
                    constraints of the node tree are violated.

                - requestFullscreen (required):
                    Displays element fullscreen and resolves promise
                    when done.  When supplied, options's navigationUI
                    member indicates whether showing navigation UI
                    while in fullscreen is preferred or not. If set to
                    \"show\", navigation simplicity is preferred over
                    screen space, and if set to \"hide\", more screen
                    space is preferred. User agents are always free to
                    honor user preference over the application's. The
                    default value \"auto\" indicates no application
                    preference.

                - requestPointerLock (required)

                - role (string; required)

                - scroll (dict; required)

                    `scroll` is a dict with keys:


                - scrollBy (dict; required)

                    `scrollBy` is a dict with keys:


                - scrollHeight (number; required)

                - scrollIntoView (required)

                - scrollLeft (number; required)

                - scrollTo (dict; required)

                    `scrollTo` is a dict with keys:


                - scrollTop (number; required)

                - scrollWidth (number; required)

                - setAttribute (required):
                    Sets the value of element's first attribute whose
                    qualified name is qualifiedName to value.

                - setAttributeNS (required):
                    Sets the value of element's attribute whose
                    namespace is namespace and local name is localName
                    to value.

                - setAttributeNode (required)

                - setAttributeNodeNS (required)

                - setPointerCapture (required)

                - shadowRoot (boolean | number | string | dict | list; required):
                    Returns element's shadow root, if any, and if
                    shadow root's mode is \"open\", and None
                    otherwise.

                - slot (string; required):
                    Returns the value of element's slot content
                    attribute. Can be set to change it.

                - spellcheck (boolean; required)

                - style (dict with strings as keys and values of type string; required)

                - tabIndex (number; required)

                - tagName (string; required):
                    Returns the HTML-uppercased qualified name.

                - textContent (string; required)

                - title (string; required)

                - toggleAttribute (required):
                    If force is not given, \"toggles\" qualifiedName,
                    removing it if it is present and adding it if it
                    is not present. If force is True, adds
                    qualifiedName. If force is False, removes
                    qualifiedName.  Returns True if qualifiedName is
                    now present, and False otherwise.

                - translate (boolean; required)

                - webkitMatchesSelector (required)

            - attachInternals (required)

            - attachShadow (required):
                Creates a shadow root for element and returns it.

            - attributes (dict; required)

                `attributes` is a dict with strings as keys and values
                of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

            - autocapitalize (string; required)

            - autofocus (boolean; required)

            - baseURI (string; required):
                Returns node's node document's document base URL.

            - before (required):
                Inserts nodes just before node, while replacing
                strings in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - blur (required)

            - childElementCount (number; required)

            - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                Returns the children.

            - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                Returns the child elements.

            - classList (dict with strings as keys and values of type string; required):
                Allows for manipulation of element's class content
                attribute as a set of whitespace-separated tokens
                through a DOMTokenList object.

            - className (string; required):
                Returns the value of element's class content
                attribute. Can be set to change it.

            - click (required)

            - clientHeight (number; required)

            - clientLeft (number; required)

            - clientTop (number; required)

            - clientWidth (number; required)

            - cloneNode (required):
                Returns a copy of node. If deep is True, the copy also
                includes the node's descendants.

            - closest (dict; required):
                Returns the first (starting at element) inclusive
                ancestor that matches selectors, and None otherwise.

                `closest` is a dict with keys:


            - compareDocumentPosition (required):
                Returns a bitmask indicating the position of other
                relative to node.

            - contains (required):
                Returns True if other is an inclusive descendant of
                node, and False otherwise.

            - contentEditable (string; required)

            - dataset (dict with strings as keys and values of type string; required)

            - dir (string; required)

            - dispatchEvent (required):
                Dispatches a synthetic event event to target and
                returns True if either event's cancelable attribute
                value is False or its preventDefault() method was not
                invoked, and False otherwise.

            - draggable (boolean; required)

            - enterKeyHint (string; required)

            - firstChild (boolean | number | string | dict | list; required):
                Returns the first child.

            - firstElementChild (a list of or a singular dash component, string or number; required):
                Returns the first child that is an element, and None
                otherwise.

            - focus (required)

            - getAnimations (required)

            - getAttribute (required):
                Returns element's first attribute whose qualified name
                is qualifiedName, and None if there is no such
                attribute otherwise.

            - getAttributeNS (required):
                Returns element's attribute whose namespace is
                namespace and local name is localName, and None if
                there is no such attribute otherwise.

            - getAttributeNames (required):
                Returns the qualified names of all element's
                attributes. Can contain duplicates.

            - getAttributeNode (required)

            - getAttributeNodeNS (required)

            - getBoundingClientRect (required)

            - getClientRects (required)

            - getElementsByClassName (required):
                Returns a HTMLCollection of the elements in the object
                on which the method was invoked (a document or an
                element) that have all the classes given by
                classNames. The classNames argument is interpreted as
                a space-separated list of classes.

            - getElementsByTagName (dict; required)

                `getElementsByTagName` is a dict with keys:


            - getElementsByTagNameNS (dict; required)

                `getElementsByTagNameNS` is a dict with keys:


            - getRootNode (required):
                Returns node's root.

            - hasAttribute (required):
                Returns True if element has an attribute whose
                qualified name is qualifiedName, and False otherwise.

            - hasAttributeNS (required):
                Returns True if element has an attribute whose
                namespace is namespace and local name is localName.

            - hasAttributes (required):
                Returns True if element has attributes, and False
                otherwise.

            - hasChildNodes (required):
                Returns whether node has children.

            - hasPointerCapture (required)

            - hidden (boolean; required)

            - id (string; required):
                Returns the value of element's id content attribute.
                Can be set to change it.

            - inert (boolean; required)

            - innerHTML (string; required)

            - innerText (string; required)

            - inputMode (string; required)

            - insertAdjacentElement (required)

            - insertAdjacentHTML (required)

            - insertAdjacentText (required)

            - insertBefore (required)

            - isConnected (boolean; required):
                Returns True if node is connected and False otherwise.

            - isContentEditable (boolean; required)

            - isDefaultNamespace (required)

            - isEqualNode (required):
                Returns whether node and otherNode have the same
                properties.

            - isSameNode (required)

            - lang (string; required)

            - lastChild (boolean | number | string | dict | list; required):
                Returns the last child.

            - lastElementChild (a list of or a singular dash component, string or number; required):
                Returns the last child that is an element, and None
                otherwise.

            - localName (string; required):
                Returns the local name.

            - lookupNamespaceURI (required)

            - lookupPrefix (required)

            - matches (required):
                Returns True if matching selectors against element's
                root yields element, and False otherwise.

            - namespaceURI (string; required):
                Returns the namespace.

            - nextElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first following sibling that is an
                element, and None otherwise.

            - nextSibling (boolean | number | string | dict | list; required):
                Returns the next sibling.

            - nodeName (string; required):
                Returns a string appropriate for the type of node.

            - nodeType (number; required):
                Returns the type of node.

            - nodeValue (string; required)

            - nonce (string; optional)

            - normalize (required):
                Removes empty exclusive Text nodes and concatenates
                the data of remaining contiguous exclusive Text nodes
                into the first of their nodes.

            - offsetHeight (number; required)

            - offsetLeft (number; required)

            - offsetParent (a list of or a singular dash component, string or number; required)

            - offsetTop (number; required)

            - offsetWidth (number; required)

            - onabort (required):
                Fires when the user aborts the download. @,param,ev,
                ,The event.

            - onanimationcancel (required)

            - onanimationend (required)

            - onanimationiteration (required)

            - onanimationstart (required)

            - onauxclick (required)

            - onbeforeinput (required)

            - onblur (required):
                Fires when the object loses the input focus.
                @,param,ev, ,The focus event.

            - oncancel (required)

            - oncanplay (required):
                Occurs when playback is possible, but would require
                further buffering. @,param,ev, ,The event.

            - oncanplaythrough (required)

            - onchange (required):
                Fires when the contents of the object or selection
                have changed. @,param,ev, ,The event.

            - onclick (required):
                Fires when the user clicks the left mouse button on
                the object @,param,ev, ,The mouse event.

            - onclose (required)

            - oncontextmenu (required):
                Fires when the user clicks the right mouse button in
                the client area, opening the context menu. @,param,ev,
                ,The mouse event.

            - oncopy (required)

            - oncuechange (required)

            - oncut (required)

            - ondblclick (required):
                Fires when the user double-clicks the object.
                @,param,ev, ,The mouse event.

            - ondrag (required):
                Fires on the source object continuously during a drag
                operation. @,param,ev, ,The event.

            - ondragend (required):
                Fires on the source object when the user releases the
                mouse at the close of a drag operation. @,param,ev,
                ,The event.

            - ondragenter (required):
                Fires on the target element when the user drags the
                object to a valid drop target. @,param,ev, ,The drag
                event.

            - ondragleave (required):
                Fires on the target object when the user moves the
                mouse out of a valid drop target during a drag
                operation. @,param,ev, ,The drag event.

            - ondragover (required):
                Fires on the target element continuously while the
                user drags the object over a valid drop target.
                @,param,ev, ,The event.

            - ondragstart (required):
                Fires on the source object when the user starts to
                drag a text selection or selected object. @,param,ev,
                ,The event.

            - ondrop (required)

            - ondurationchange (required):
                Occurs when the duration attribute is updated.
                @,param,ev, ,The event.

            - onemptied (required):
                Occurs when the media element is reset to its initial
                state. @,param,ev, ,The event.

            - onended (required):
                Occurs when the end of playback is reached.
                @,param,ev, ,The event.

            - onerror (dict; required):
                Fires when an error occurs during object loading.
                @,param,ev, ,The event.

                `onerror` is a dict with keys:


            - onfocus (required):
                Fires when the object receives focus. @,param,ev, ,The
                event.

            - onformdata (required)

            - onfullscreenchange (required)

            - onfullscreenerror (required)

            - ongotpointercapture (required)

            - oninput (required)

            - oninvalid (required)

            - onkeydown (required):
                Fires when the user presses a key. @,param,ev, ,The
                keyboard event.

            - onkeypress (required):
                Fires when the user presses an alphanumeric key.
                @,param,ev, ,The event. @,deprecated.

            - onkeyup (required):
                Fires when the user releases a key. @,param,ev, ,The
                keyboard event.

            - onload (required):
                Fires immediately after the browser loads the object.
                @,param,ev, ,The event.

            - onloadeddata (required):
                Occurs when media data is loaded at the current
                playback position. @,param,ev, ,The event.

            - onloadedmetadata (required):
                Occurs when the duration and dimensions of the media
                have been determined. @,param,ev, ,The event.

            - onloadstart (required):
                Occurs when Internet Explorer begins looking for media
                data. @,param,ev, ,The event.

            - onlostpointercapture (required)

            - onmousedown (required):
                Fires when the user clicks the object with either
                mouse button. @,param,ev, ,The mouse event.

            - onmouseenter (required)

            - onmouseleave (required)

            - onmousemove (required):
                Fires when the user moves the mouse over the object.
                @,param,ev, ,The mouse event.

            - onmouseout (required):
                Fires when the user moves the mouse pointer outside
                the boundaries of the object. @,param,ev, ,The mouse
                event.

            - onmouseover (required):
                Fires when the user moves the mouse pointer into the
                object. @,param,ev, ,The mouse event.

            - onmouseup (required):
                Fires when the user releases a mouse button while the
                mouse is over the object. @,param,ev, ,The mouse
                event.

            - onpaste (required)

            - onpause (required):
                Occurs when playback is paused. @,param,ev, ,The
                event.

            - onplay (required):
                Occurs when the play method is requested. @,param,ev,
                ,The event.

            - onplaying (required):
                Occurs when the audio or video has started playing.
                @,param,ev, ,The event.

            - onpointercancel (required)

            - onpointerdown (required)

            - onpointerenter (required)

            - onpointerleave (required)

            - onpointermove (required)

            - onpointerout (required)

            - onpointerover (required)

            - onpointerup (required)

            - onprogress (required):
                Occurs to indicate progress while downloading media
                data. @,param,ev, ,The event.

            - onratechange (required):
                Occurs when the playback rate is increased or
                decreased. @,param,ev, ,The event.

            - onreset (required):
                Fires when the user resets a form. @,param,ev, ,The
                event.

            - onresize (required)

            - onscroll (required):
                Fires when the user repositions the scroll box in the
                scroll bar on the object. @,param,ev, ,The event.

            - onsecuritypolicyviolation (required)

            - onseeked (required):
                Occurs when the seek operation ends. @,param,ev, ,The
                event.

            - onseeking (required):
                Occurs when the current playback position is moved.
                @,param,ev, ,The event.

            - onselect (required):
                Fires when the current selection changes. @,param,ev,
                ,The event.

            - onselectionchange (required)

            - onselectstart (required)

            - onslotchange (required)

            - onstalled (required):
                Occurs when the download has stopped. @,param,ev, ,The
                event.

            - onsubmit (required)

            - onsuspend (required):
                Occurs if the load operation has been intentionally
                halted. @,param,ev, ,The event.

            - ontimeupdate (required):
                Occurs to indicate the current playback position.
                @,param,ev, ,The event.

            - ontoggle (required)

            - ontouchcancel (optional)

            - ontouchend (optional)

            - ontouchmove (optional)

            - ontouchstart (optional)

            - ontransitioncancel (required)

            - ontransitionend (required)

            - ontransitionrun (required)

            - ontransitionstart (required)

            - onvolumechange (required):
                Occurs when the volume is changed, or playback is
                muted or unmuted. @,param,ev, ,The event.

            - onwaiting (required):
                Occurs when playback stops because the next frame of a
                video resource is not available. @,param,ev, ,The
                event.

            - onwebkitanimationend (required)

            - onwebkitanimationiteration (required)

            - onwebkitanimationstart (required)

            - onwebkittransitionend (required)

            - onwheel (required)

            - outerHTML (string; required)

            - outerText (string; required)

            - ownerDocument (boolean | number | string | dict | list; required)

            - parentElement (boolean | number | string | dict | list; required):
                Returns the parent element.

            - parentNode (boolean | number | string | dict | list; required):
                Returns the parent.

            - part (dict with strings as keys and values of type string; required)

            - prefix (string; required):
                Returns the namespace prefix.

            - prepend (required):
                Inserts nodes before the first child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - previousElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first preceding sibling that is an
                element, and None otherwise.

            - previousSibling (boolean | number | string | dict | list; required):
                Returns the previous sibling.

            - querySelector (dict; required):
                Returns the first element that is a descendant of node
                that matches selectors.

                `querySelector` is a dict with keys:


            - querySelectorAll (dict; required):
                Returns all element descendants of node that match
                selectors.

                `querySelectorAll` is a dict with keys:


            - releasePointerCapture (required)

            - remove (required):
                Removes node.

            - removeAttribute (required):
                Removes element's first attribute whose qualified name
                is qualifiedName.

            - removeAttributeNS (required):
                Removes element's attribute whose namespace is
                namespace and local name is localName.

            - removeAttributeNode (required)

            - removeChild (required)

            - removeEventListener (required)

            - replaceChild (required)

            - replaceChildren (required):
                Replace all children of node with nodes, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - replaceWith (required):
                Replaces node with nodes, while replacing strings in
                nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - requestFullscreen (required):
                Displays element fullscreen and resolves promise when
                done.  When supplied, options's navigationUI member
                indicates whether showing navigation UI while in
                fullscreen is preferred or not. If set to \"show\",
                navigation simplicity is preferred over screen space,
                and if set to \"hide\", more screen space is
                preferred. User agents are always free to honor user
                preference over the application's. The default value
                \"auto\" indicates no application preference.

            - requestPointerLock (required)

            - role (string; required)

            - scroll (dict; required)

                `scroll` is a dict with keys:


            - scrollBy (dict; required)

                `scrollBy` is a dict with keys:


            - scrollHeight (number; required)

            - scrollIntoView (required)

            - scrollLeft (number; required)

            - scrollTo (dict; required)

                `scrollTo` is a dict with keys:


            - scrollTop (number; required)

            - scrollWidth (number; required)

            - setAttribute (required):
                Sets the value of element's first attribute whose
                qualified name is qualifiedName to value.

            - setAttributeNS (required):
                Sets the value of element's attribute whose namespace
                is namespace and local name is localName to value.

            - setAttributeNode (required)

            - setAttributeNodeNS (required)

            - setPointerCapture (required)

            - shadowRoot (boolean | number | string | dict | list; required):
                Returns element's shadow root, if any, and if shadow
                root's mode is \"open\", and None otherwise.

            - slot (string; required):
                Returns the value of element's slot content attribute.
                Can be set to change it.

            - spellcheck (boolean; required)

            - style (dict with strings as keys and values of type string; required)

            - tabIndex (number; required)

            - tagName (string; required):
                Returns the HTML-uppercased qualified name.

            - textContent (string; required)

            - title (string; required)

            - toggleAttribute (required):
                If force is not given, \"toggles\" qualifiedName,
                removing it if it is present and adding it if it is
                not present. If force is True, adds qualifiedName. If
                force is False, removes qualifiedName.  Returns True
                if qualifiedName is now present, and False otherwise.

            - translate (boolean; required)

            - webkitMatchesSelector (required)

        - firstDay (number; optional):
            First day of the week (0: Sunday, 1: Monday, etc).

        - format (string; optional):
            The default output format for toString() and field value.
            Requires Moment.js for custom formatting.

        - formatStrict (boolean; optional):
            The default flag for moment's strict date parsing
            (requires Moment.js for custom formatting). Default:
            False.

        - i18n (dict; optional):
            Language defaults for month and weekday names.

            `i18n` is a dict with keys:

            - months (list of strings; required)

            - nextMonth (string; required)

            - previousMonth (string; required)

            - weekdays (list of strings; required)

            - weekdaysShort (list of strings; required)

        - isRTL (boolean; optional):
            Reverse the calendar for right-to-left languages. Default:
            False.

        - keyboardInput (boolean; optional):
            Enable keyboard input support. Default: True.

        - mainCalendar (string; optional):
            When numberOfMonths is used, this will help you to choose
            where the main calendar will be (default left, can be set
            to right). Only used for the first display or when a
            selected date is not already visible.

        - maxDate (dict; optional):
            The latest date that can be selected (this should be a
            native Date object - e.g. new Date() or
            moment().toDate()).

            `maxDate` is a dict with keys:

            - __@toPrimitive@4735 (dict; required):
                Converts a Date object to a string.   Converts a Date
                object to a number.   Converts a Date object to a
                string or number. @,param,hint, ,The strings
                \"number\", \"string\", or \"default\" to specify what
                primitive to return. @,throws,{TypeError} If 'hint'
                was given something other than \"number\", \"string\",
                or \"default\". @,returns,A number if 'hint' was
                \"number\", a string if 'hint' was \"string\" or
                \"default\".

                `__@toPrimitive@4735` is a dict with keys:


            - getDate (required):
                Gets the day-of-the-month, using local time.

            - getDay (required):
                Gets the day of the week, using local time.

            - getFullYear (required):
                Gets the year, using local time.

            - getHours (required):
                Gets the hours in a date, using local time.

            - getMilliseconds (required):
                Gets the milliseconds of a Date, using local time.

            - getMinutes (required):
                Gets the minutes of a Date object, using local time.

            - getMonth (required):
                Gets the month, using local time.

            - getSeconds (required):
                Gets the seconds of a Date object, using local time.

            - getTime (required):
                Gets the time value in milliseconds.

            - getTimezoneOffset (required):
                Gets the difference in minutes between the time on the
                local computer and Universal Coordinated Time (UTC).

            - getUTCDate (required):
                Gets the day-of-the-month, using Universal Coordinated
                Time (UTC).

            - getUTCDay (required):
                Gets the day of the week using Universal Coordinated
                Time (UTC).

            - getUTCFullYear (required):
                Gets the year using Universal Coordinated Time (UTC).

            - getUTCHours (required):
                Gets the hours value in a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMilliseconds (required):
                Gets the milliseconds of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMinutes (required):
                Gets the minutes of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMonth (required):
                Gets the month of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCSeconds (required):
                Gets the seconds of a Date object using Universal
                Coordinated Time (UTC).

            - getVarDate (required)

            - setDate (required):
                Sets the numeric day-of-the-month value of the Date
                object using local time. @,param,date, ,A numeric
                value equal to the day of the month.

            - setFullYear (required):
                Sets the year of the Date object using local time.
                @,param,year, ,A numeric value for the year.
                @,param,month, ,A zero-based numeric value for the
                month (0 for January, 11 for December). Must be
                specified if numDate is specified. @,param,date, ,A
                numeric value equal for the day of the month.

            - setHours (required):
                Sets the hour value in the Date object using local
                time. @,param,hours, ,A numeric value equal to the
                hours value. @,param,min, ,A numeric value equal to
                the minutes value. @,param,sec, ,A numeric value equal
                to the seconds value. @,param,ms, ,A numeric value
                equal to the milliseconds value.

            - setMilliseconds (required):
                Sets the milliseconds value in the Date object using
                local time. @,param,ms, ,A numeric value equal to the
                millisecond value.

            - setMinutes (required):
                Sets the minutes value in the Date object using local
                time. @,param,min, ,A numeric value equal to the
                minutes value. @,param,sec, ,A numeric value equal to
                the seconds value. @,param,ms, ,A numeric value equal
                to the milliseconds value.

            - setMonth (required):
                Sets the month value in the Date object using local
                time. @,param,month, ,A numeric value equal to the
                month. The value for January is 0, and other month
                values follow consecutively. @,param,date, ,A numeric
                value representing the day of the month. If this value
                is not supplied, the value from a call to the getDate
                method is used.

            - setSeconds (required):
                Sets the seconds value in the Date object using local
                time. @,param,sec, ,A numeric value equal to the
                seconds value. @,param,ms, ,A numeric value equal to
                the milliseconds value.

            - setTime (required):
                Sets the date and time value in the Date object.
                @,param,time, ,A numeric value representing the number
                of elapsed milliseconds since midnight, January 1,
                1970 GMT.

            - setUTCDate (required):
                Sets the numeric day of the month in the Date object
                using Universal Coordinated Time (UTC). @,param,date,
                ,A numeric value equal to the day of the month.

            - setUTCFullYear (required):
                Sets the year value in the Date object using Universal
                Coordinated Time (UTC). @,param,year, ,A numeric value
                equal to the year. @,param,month, ,A numeric value
                equal to the month. The value for January is 0, and
                other month values follow consecutively. Must be
                supplied if numDate is supplied. @,param,date, ,A
                numeric value equal to the day of the month.

            - setUTCHours (required):
                Sets the hours value in the Date object using
                Universal Coordinated Time (UTC). @,param,hours, ,A
                numeric value equal to the hours value. @,param,min,
                ,A numeric value equal to the minutes value.
                @,param,sec, ,A numeric value equal to the seconds
                value. @,param,ms, ,A numeric value equal to the
                milliseconds value.

            - setUTCMilliseconds (required):
                Sets the milliseconds value in the Date object using
                Universal Coordinated Time (UTC). @,param,ms, ,A
                numeric value equal to the millisecond value.

            - setUTCMinutes (required):
                Sets the minutes value in the Date object using
                Universal Coordinated Time (UTC). @,param,min, ,A
                numeric value equal to the minutes value. @,param,sec,
                ,A numeric value equal to the seconds value.
                @,param,ms, ,A numeric value equal to the milliseconds
                value.

            - setUTCMonth (required):
                Sets the month value in the Date object using
                Universal Coordinated Time (UTC). @,param,month, ,A
                numeric value equal to the month. The value for
                January is 0, and other month values follow
                consecutively. @,param,date, ,A numeric value
                representing the day of the month. If it is not
                supplied, the value from a call to the getUTCDate
                method is used.

            - setUTCSeconds (required):
                Sets the seconds value in the Date object using
                Universal Coordinated Time (UTC). @,param,sec, ,A
                numeric value equal to the seconds value. @,param,ms,
                ,A numeric value equal to the milliseconds value.

            - toDateString (required):
                Returns a date as a string value.

            - toISOString (required):
                Returns a date as a string value in ISO format.

            - toJSON (required):
                Used by the JSON.stringify method to enable the
                transformation of an object's data for JavaScript
                Object Notation (JSON) serialization.

            - toLocaleDateString (dict; required):
                Returns a date as a string value appropriate to the
                host environment's current locale.   Converts a date
                to a string by using the current or specified locale.
                @,param,locales, ,A locale string or array of locale
                strings that contain one or more language or locale
                tags. If you include more than one locale string, list
                them in descending order of priority so that the first
                entry is the preferred locale. If you omit this
                parameter, the default locale of the JavaScript
                runtime is used. @,param,options, ,An object that
                contains one or more properties that specify
                comparison options. @,param,locales, ,A locale string,
                array of locale strings, Intl.Locale object, or array
                of Intl.Locale objects that contain one or more
                language or locale tags. If you include more than one
                locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleDateString` is a dict with keys:


            - toLocaleString (dict; optional):
                Returns a value as a string value appropriate to the
                host environment's current locale.   Converts a date
                and time to a string by using the current or specified
                locale. @,param,locales, ,A locale string or array of
                locale strings that contain one or more language or
                locale tags. If you include more than one locale
                string, list them in descending order of priority so
                that the first entry is the preferred locale. If you
                omit this parameter, the default locale of the
                JavaScript runtime is used. @,param,options, ,An
                object that contains one or more properties that
                specify comparison options. @,param,locales, ,A locale
                string, array of locale strings, Intl.Locale object,
                or array of Intl.Locale objects that contain one or
                more language or locale tags. If you include more than
                one locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleString` is a dict with keys:


            - toLocaleTimeString (dict; required):
                Returns a time as a string value appropriate to the
                host environment's current locale.   Converts a time
                to a string by using the current or specified locale.
                @,param,locales, ,A locale string or array of locale
                strings that contain one or more language or locale
                tags. If you include more than one locale string, list
                them in descending order of priority so that the first
                entry is the preferred locale. If you omit this
                parameter, the default locale of the JavaScript
                runtime is used. @,param,options, ,An object that
                contains one or more properties that specify
                comparison options. @,param,locales, ,A locale string,
                array of locale strings, Intl.Locale object, or array
                of Intl.Locale objects that contain one or more
                language or locale tags. If you include more than one
                locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleTimeString` is a dict with keys:


            - toString (optional):
                Returns a string representation of a date. The format
                of the string depends on the locale.

            - toTimeString (required):
                Returns a time as a string value.

            - toUTCString (required):
                Returns a date converted to a string using Universal
                Coordinated Time (UTC).

            - valueOf (optional):
                Returns the stored time value in milliseconds since
                midnight, January 1, 1970 UTC.

        - minDate (dict; optional):
            The earliest date that can be selected (this should be a
            native Date object - e.g. new Date() or
            moment().toDate()).

            `minDate` is a dict with keys:

            - __@toPrimitive@4735 (dict; required):
                Converts a Date object to a string.   Converts a Date
                object to a number.   Converts a Date object to a
                string or number. @,param,hint, ,The strings
                \"number\", \"string\", or \"default\" to specify what
                primitive to return. @,throws,{TypeError} If 'hint'
                was given something other than \"number\", \"string\",
                or \"default\". @,returns,A number if 'hint' was
                \"number\", a string if 'hint' was \"string\" or
                \"default\".

                `__@toPrimitive@4735` is a dict with keys:


            - getDate (required):
                Gets the day-of-the-month, using local time.

            - getDay (required):
                Gets the day of the week, using local time.

            - getFullYear (required):
                Gets the year, using local time.

            - getHours (required):
                Gets the hours in a date, using local time.

            - getMilliseconds (required):
                Gets the milliseconds of a Date, using local time.

            - getMinutes (required):
                Gets the minutes of a Date object, using local time.

            - getMonth (required):
                Gets the month, using local time.

            - getSeconds (required):
                Gets the seconds of a Date object, using local time.

            - getTime (required):
                Gets the time value in milliseconds.

            - getTimezoneOffset (required):
                Gets the difference in minutes between the time on the
                local computer and Universal Coordinated Time (UTC).

            - getUTCDate (required):
                Gets the day-of-the-month, using Universal Coordinated
                Time (UTC).

            - getUTCDay (required):
                Gets the day of the week using Universal Coordinated
                Time (UTC).

            - getUTCFullYear (required):
                Gets the year using Universal Coordinated Time (UTC).

            - getUTCHours (required):
                Gets the hours value in a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMilliseconds (required):
                Gets the milliseconds of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMinutes (required):
                Gets the minutes of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCMonth (required):
                Gets the month of a Date object using Universal
                Coordinated Time (UTC).

            - getUTCSeconds (required):
                Gets the seconds of a Date object using Universal
                Coordinated Time (UTC).

            - getVarDate (required)

            - setDate (required):
                Sets the numeric day-of-the-month value of the Date
                object using local time. @,param,date, ,A numeric
                value equal to the day of the month.

            - setFullYear (required):
                Sets the year of the Date object using local time.
                @,param,year, ,A numeric value for the year.
                @,param,month, ,A zero-based numeric value for the
                month (0 for January, 11 for December). Must be
                specified if numDate is specified. @,param,date, ,A
                numeric value equal for the day of the month.

            - setHours (required):
                Sets the hour value in the Date object using local
                time. @,param,hours, ,A numeric value equal to the
                hours value. @,param,min, ,A numeric value equal to
                the minutes value. @,param,sec, ,A numeric value equal
                to the seconds value. @,param,ms, ,A numeric value
                equal to the milliseconds value.

            - setMilliseconds (required):
                Sets the milliseconds value in the Date object using
                local time. @,param,ms, ,A numeric value equal to the
                millisecond value.

            - setMinutes (required):
                Sets the minutes value in the Date object using local
                time. @,param,min, ,A numeric value equal to the
                minutes value. @,param,sec, ,A numeric value equal to
                the seconds value. @,param,ms, ,A numeric value equal
                to the milliseconds value.

            - setMonth (required):
                Sets the month value in the Date object using local
                time. @,param,month, ,A numeric value equal to the
                month. The value for January is 0, and other month
                values follow consecutively. @,param,date, ,A numeric
                value representing the day of the month. If this value
                is not supplied, the value from a call to the getDate
                method is used.

            - setSeconds (required):
                Sets the seconds value in the Date object using local
                time. @,param,sec, ,A numeric value equal to the
                seconds value. @,param,ms, ,A numeric value equal to
                the milliseconds value.

            - setTime (required):
                Sets the date and time value in the Date object.
                @,param,time, ,A numeric value representing the number
                of elapsed milliseconds since midnight, January 1,
                1970 GMT.

            - setUTCDate (required):
                Sets the numeric day of the month in the Date object
                using Universal Coordinated Time (UTC). @,param,date,
                ,A numeric value equal to the day of the month.

            - setUTCFullYear (required):
                Sets the year value in the Date object using Universal
                Coordinated Time (UTC). @,param,year, ,A numeric value
                equal to the year. @,param,month, ,A numeric value
                equal to the month. The value for January is 0, and
                other month values follow consecutively. Must be
                supplied if numDate is supplied. @,param,date, ,A
                numeric value equal to the day of the month.

            - setUTCHours (required):
                Sets the hours value in the Date object using
                Universal Coordinated Time (UTC). @,param,hours, ,A
                numeric value equal to the hours value. @,param,min,
                ,A numeric value equal to the minutes value.
                @,param,sec, ,A numeric value equal to the seconds
                value. @,param,ms, ,A numeric value equal to the
                milliseconds value.

            - setUTCMilliseconds (required):
                Sets the milliseconds value in the Date object using
                Universal Coordinated Time (UTC). @,param,ms, ,A
                numeric value equal to the millisecond value.

            - setUTCMinutes (required):
                Sets the minutes value in the Date object using
                Universal Coordinated Time (UTC). @,param,min, ,A
                numeric value equal to the minutes value. @,param,sec,
                ,A numeric value equal to the seconds value.
                @,param,ms, ,A numeric value equal to the milliseconds
                value.

            - setUTCMonth (required):
                Sets the month value in the Date object using
                Universal Coordinated Time (UTC). @,param,month, ,A
                numeric value equal to the month. The value for
                January is 0, and other month values follow
                consecutively. @,param,date, ,A numeric value
                representing the day of the month. If it is not
                supplied, the value from a call to the getUTCDate
                method is used.

            - setUTCSeconds (required):
                Sets the seconds value in the Date object using
                Universal Coordinated Time (UTC). @,param,sec, ,A
                numeric value equal to the seconds value. @,param,ms,
                ,A numeric value equal to the milliseconds value.

            - toDateString (required):
                Returns a date as a string value.

            - toISOString (required):
                Returns a date as a string value in ISO format.

            - toJSON (required):
                Used by the JSON.stringify method to enable the
                transformation of an object's data for JavaScript
                Object Notation (JSON) serialization.

            - toLocaleDateString (dict; required):
                Returns a date as a string value appropriate to the
                host environment's current locale.   Converts a date
                to a string by using the current or specified locale.
                @,param,locales, ,A locale string or array of locale
                strings that contain one or more language or locale
                tags. If you include more than one locale string, list
                them in descending order of priority so that the first
                entry is the preferred locale. If you omit this
                parameter, the default locale of the JavaScript
                runtime is used. @,param,options, ,An object that
                contains one or more properties that specify
                comparison options. @,param,locales, ,A locale string,
                array of locale strings, Intl.Locale object, or array
                of Intl.Locale objects that contain one or more
                language or locale tags. If you include more than one
                locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleDateString` is a dict with keys:


            - toLocaleString (dict; optional):
                Returns a value as a string value appropriate to the
                host environment's current locale.   Converts a date
                and time to a string by using the current or specified
                locale. @,param,locales, ,A locale string or array of
                locale strings that contain one or more language or
                locale tags. If you include more than one locale
                string, list them in descending order of priority so
                that the first entry is the preferred locale. If you
                omit this parameter, the default locale of the
                JavaScript runtime is used. @,param,options, ,An
                object that contains one or more properties that
                specify comparison options. @,param,locales, ,A locale
                string, array of locale strings, Intl.Locale object,
                or array of Intl.Locale objects that contain one or
                more language or locale tags. If you include more than
                one locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleString` is a dict with keys:


            - toLocaleTimeString (dict; required):
                Returns a time as a string value appropriate to the
                host environment's current locale.   Converts a time
                to a string by using the current or specified locale.
                @,param,locales, ,A locale string or array of locale
                strings that contain one or more language or locale
                tags. If you include more than one locale string, list
                them in descending order of priority so that the first
                entry is the preferred locale. If you omit this
                parameter, the default locale of the JavaScript
                runtime is used. @,param,options, ,An object that
                contains one or more properties that specify
                comparison options. @,param,locales, ,A locale string,
                array of locale strings, Intl.Locale object, or array
                of Intl.Locale objects that contain one or more
                language or locale tags. If you include more than one
                locale string, list them in descending order of
                priority so that the first entry is the preferred
                locale. If you omit this parameter, the default locale
                of the JavaScript runtime is used. @,param,options,
                ,An object that contains one or more properties that
                specify comparison options.

                `toLocaleTimeString` is a dict with keys:


            - toString (optional):
                Returns a string representation of a date. The format
                of the string depends on the locale.

            - toTimeString (required):
                Returns a time as a string value.

            - toUTCString (required):
                Returns a date converted to a string using Universal
                Coordinated Time (UTC).

            - valueOf (optional):
                Returns the stored time value in milliseconds since
                midnight, January 1, 1970 UTC.

        - numberOfMonths (number; optional):
            Number of visible calendars.

        - onClose (optional):
            Callback function for when the picker is hidden.

        - onDraw (optional):
            Callback function for when the picker draws a new month.

        - onOpen (optional):
            Callback function for when the picker becomes visible.

        - onSelect (optional):
            Callback function for when a date is selected.

        - parse (optional):
            Function which will be used for parsing input string and
            getting a date object from it. This function will take
            precedence over moment.

        - pickWholeWeek (boolean; optional):
            Select a whole week instead of a day (default False).

        - position (string; optional):
            Preferred position of the datepicker relative to the form
            field (e.g. 'top right'). Automatic adjustment may occur
            to avoid displaying outside the viewport. Default: 'bottom
            left'.

        - reposition (boolean; optional):
            Can be set to False to not reposition the datepicker
            within the viewport, forcing it to take the configured
            position. Default: True.

        - setDefaultDate (boolean; optional):
            Make the defaultDate the initial selected value.

        - showDaysInNextAndPreviousMonths (boolean; optional):
            Render days of the calendar grid that fall in the next or
            previous months to the current month instead of rendering
            an empty table cell. Default: False.

        - showMonthAfterYear (boolean; optional):
            Render the month after the year in the title. Default:
            False.

        - showWeekNumber (boolean; optional):
            Show the ISO week number at the head of the row. Default:
            False.

        - theme (string; optional):
            Define a class name that can be used as a hook for styling
            different themes. Default: None.

        - toString (optional):
            Function which will be used for formatting date object to
            string. This function will take precedence over moment.

        - trigger (dict; optional):
            Use a different element to trigger opening the datepicker.
            Default: field element.

            `trigger` is a dict with keys:

            - ATTRIBUTE_NODE (number; required)

            - CDATA_SECTION_NODE (number; required):
                node is a CDATASection node.

            - COMMENT_NODE (number; required):
                node is a Comment node.

            - DOCUMENT_FRAGMENT_NODE (number; required):
                node is a DocumentFragment node.

            - DOCUMENT_NODE (number; required):
                node is a document.

            - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                Set when other is a descendant of node.

            - DOCUMENT_POSITION_CONTAINS (number; required):
                Set when other is an ancestor of node.

            - DOCUMENT_POSITION_DISCONNECTED (number; required):
                Set when node and other are not in the same tree.

            - DOCUMENT_POSITION_FOLLOWING (number; required):
                Set when other is following node.

            - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

            - DOCUMENT_POSITION_PRECEDING (number; required):
                Set when other is preceding node.

            - DOCUMENT_TYPE_NODE (number; required):
                node is a doctype.

            - ELEMENT_NODE (number; required):
                node is an element.

            - ENTITY_NODE (number; required)

            - ENTITY_REFERENCE_NODE (number; required)

            - NOTATION_NODE (number; required)

            - PROCESSING_INSTRUCTION_NODE (number; required):
                node is a ProcessingInstruction node.

            - TEXT_NODE (number; required):
                node is a Text node.

            - accessKey (string; required)

            - accessKeyLabel (string; required)

            - addEventListener (required)

            - after (required):
                Inserts nodes just after node, while replacing strings
                in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - animate (required)

            - append (required):
                Inserts nodes after the last child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - appendChild (required)

            - ariaAtomic (string; required)

            - ariaAutoComplete (string; required)

            - ariaBusy (string; required)

            - ariaChecked (string; required)

            - ariaColCount (string; required)

            - ariaColIndex (string; required)

            - ariaColIndexText (string; required)

            - ariaColSpan (string; required)

            - ariaCurrent (string; required)

            - ariaDisabled (string; required)

            - ariaExpanded (string; required)

            - ariaHasPopup (string; required)

            - ariaHidden (string; required)

            - ariaInvalid (string; required)

            - ariaKeyShortcuts (string; required)

            - ariaLabel (string; required)

            - ariaLevel (string; required)

            - ariaLive (string; required)

            - ariaModal (string; required)

            - ariaMultiLine (string; required)

            - ariaMultiSelectable (string; required)

            - ariaOrientation (string; required)

            - ariaPlaceholder (string; required)

            - ariaPosInSet (string; required)

            - ariaPressed (string; required)

            - ariaReadOnly (string; required)

            - ariaRequired (string; required)

            - ariaRoleDescription (string; required)

            - ariaRowCount (string; required)

            - ariaRowIndex (string; required)

            - ariaRowIndexText (string; required)

            - ariaRowSpan (string; required)

            - ariaSelected (string; required)

            - ariaSetSize (string; required)

            - ariaSort (string; required)

            - ariaValueMax (string; required)

            - ariaValueMin (string; required)

            - ariaValueNow (string; required)

            - ariaValueText (string; required)

            - assignedSlot (dict; required)

                `assignedSlot` is a dict with keys:

                - ATTRIBUTE_NODE (number; required)

                - CDATA_SECTION_NODE (number; required):
                    node is a CDATASection node.

                - COMMENT_NODE (number; required):
                    node is a Comment node.

                - DOCUMENT_FRAGMENT_NODE (number; required):
                    node is a DocumentFragment node.

                - DOCUMENT_NODE (number; required):
                    node is a document.

                - DOCUMENT_POSITION_CONTAINED_BY (number; required):
                    Set when other is a descendant of node.

                - DOCUMENT_POSITION_CONTAINS (number; required):
                    Set when other is an ancestor of node.

                - DOCUMENT_POSITION_DISCONNECTED (number; required):
                    Set when node and other are not in the same tree.

                - DOCUMENT_POSITION_FOLLOWING (number; required):
                    Set when other is following node.

                - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

                - DOCUMENT_POSITION_PRECEDING (number; required):
                    Set when other is preceding node.

                - DOCUMENT_TYPE_NODE (number; required):
                    node is a doctype.

                - ELEMENT_NODE (number; required):
                    node is an element.

                - ENTITY_NODE (number; required)

                - ENTITY_REFERENCE_NODE (number; required)

                - NOTATION_NODE (number; required)

                - PROCESSING_INSTRUCTION_NODE (number; required):
                    node is a ProcessingInstruction node.

                - TEXT_NODE (number; required):
                    node is a Text node.

                - accessKey (string; required)

                - accessKeyLabel (string; required)

                - addEventListener (required)

                - after (required):
                    Inserts nodes just after node, while replacing
                    strings in nodes with equivalent Text nodes.
                    Throws a \"HierarchyRequestError\" DOMException if
                    the constraints of the node tree are violated.

                - animate (required)

                - append (required):
                    Inserts nodes after the last child of node, while
                    replacing strings in nodes with equivalent Text
                    nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - appendChild (required)

                - ariaAtomic (string; required)

                - ariaAutoComplete (string; required)

                - ariaBusy (string; required)

                - ariaChecked (string; required)

                - ariaColCount (string; required)

                - ariaColIndex (string; required)

                - ariaColIndexText (string; required)

                - ariaColSpan (string; required)

                - ariaCurrent (string; required)

                - ariaDisabled (string; required)

                - ariaExpanded (string; required)

                - ariaHasPopup (string; required)

                - ariaHidden (string; required)

                - ariaInvalid (string; required)

                - ariaKeyShortcuts (string; required)

                - ariaLabel (string; required)

                - ariaLevel (string; required)

                - ariaLive (string; required)

                - ariaModal (string; required)

                - ariaMultiLine (string; required)

                - ariaMultiSelectable (string; required)

                - ariaOrientation (string; required)

                - ariaPlaceholder (string; required)

                - ariaPosInSet (string; required)

                - ariaPressed (string; required)

                - ariaReadOnly (string; required)

                - ariaRequired (string; required)

                - ariaRoleDescription (string; required)

                - ariaRowCount (string; required)

                - ariaRowIndex (string; required)

                - ariaRowIndexText (string; required)

                - ariaRowSpan (string; required)

                - ariaSelected (string; required)

                - ariaSetSize (string; required)

                - ariaSort (string; required)

                - ariaValueMax (string; required)

                - ariaValueMin (string; required)

                - ariaValueNow (string; required)

                - ariaValueText (string; required)

                - assign (required)

                - assignedElements (required)

                - assignedNodes (required)

                - assignedSlot (boolean | number | string | dict | list; required)

                - attachInternals (required)

                - attachShadow (required):
                    Creates a shadow root for element and returns it.

                - attributes (dict; required)

                    `attributes` is a dict with strings as keys and
                    values of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

                - autocapitalize (string; required)

                - autofocus (boolean; required)

                - baseURI (string; required):
                    Returns node's node document's document base URL.

                - before (required):
                    Inserts nodes just before node, while replacing
                    strings in nodes with equivalent Text nodes.
                    Throws a \"HierarchyRequestError\" DOMException if
                    the constraints of the node tree are violated.

                - blur (required)

                - childElementCount (number; required)

                - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                    Returns the children.

                - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                    Returns the child elements.

                - classList (dict with strings as keys and values of type string; required):
                    Allows for manipulation of element's class content
                    attribute as a set of whitespace-separated tokens
                    through a DOMTokenList object.

                - className (string; required):
                    Returns the value of element's class content
                    attribute. Can be set to change it.

                - click (required)

                - clientHeight (number; required)

                - clientLeft (number; required)

                - clientTop (number; required)

                - clientWidth (number; required)

                - cloneNode (required):
                    Returns a copy of node. If deep is True, the copy
                    also includes the node's descendants.

                - closest (dict; required):
                    Returns the first (starting at element) inclusive
                    ancestor that matches selectors, and None
                    otherwise.

                    `closest` is a dict with keys:


                - compareDocumentPosition (required):
                    Returns a bitmask indicating the position of other
                    relative to node.

                - contains (required):
                    Returns True if other is an inclusive descendant
                    of node, and False otherwise.

                - contentEditable (string; required)

                - dataset (dict with strings as keys and values of type string; required)

                - dir (string; required)

                - dispatchEvent (required):
                    Dispatches a synthetic event event to target and
                    returns True if either event's cancelable
                    attribute value is False or its preventDefault()
                    method was not invoked, and False otherwise.

                - draggable (boolean; required)

                - enterKeyHint (string; required)

                - firstChild (boolean | number | string | dict | list; required):
                    Returns the first child.

                - firstElementChild (a list of or a singular dash component, string or number; required):
                    Returns the first child that is an element, and
                    None otherwise.

                - focus (required)

                - getAnimations (required)

                - getAttribute (required):
                    Returns element's first attribute whose qualified
                    name is qualifiedName, and None if there is no
                    such attribute otherwise.

                - getAttributeNS (required):
                    Returns element's attribute whose namespace is
                    namespace and local name is localName, and None if
                    there is no such attribute otherwise.

                - getAttributeNames (required):
                    Returns the qualified names of all element's
                    attributes. Can contain duplicates.

                - getAttributeNode (required)

                - getAttributeNodeNS (required)

                - getBoundingClientRect (required)

                - getClientRects (required)

                - getElementsByClassName (required):
                    Returns a HTMLCollection of the elements in the
                    object on which the method was invoked (a document
                    or an element) that have all the classes given by
                    classNames. The classNames argument is interpreted
                    as a space-separated list of classes.

                - getElementsByTagName (dict; required)

                    `getElementsByTagName` is a dict with keys:


                - getElementsByTagNameNS (dict; required)

                    `getElementsByTagNameNS` is a dict with keys:


                - getRootNode (required):
                    Returns node's root.

                - hasAttribute (required):
                    Returns True if element has an attribute whose
                    qualified name is qualifiedName, and False
                    otherwise.

                - hasAttributeNS (required):
                    Returns True if element has an attribute whose
                    namespace is namespace and local name is
                    localName.

                - hasAttributes (required):
                    Returns True if element has attributes, and False
                    otherwise.

                - hasChildNodes (required):
                    Returns whether node has children.

                - hasPointerCapture (required)

                - hidden (boolean; required)

                - id (string; required):
                    Returns the value of element's id content
                    attribute. Can be set to change it.

                - inert (boolean; required)

                - innerHTML (string; required)

                - innerText (string; required)

                - inputMode (string; required)

                - insertAdjacentElement (required)

                - insertAdjacentHTML (required)

                - insertAdjacentText (required)

                - insertBefore (required)

                - isConnected (boolean; required):
                    Returns True if node is connected and False
                    otherwise.

                - isContentEditable (boolean; required)

                - isDefaultNamespace (required)

                - isEqualNode (required):
                    Returns whether node and otherNode have the same
                    properties.

                - isSameNode (required)

                - lang (string; required)

                - lastChild (boolean | number | string | dict | list; required):
                    Returns the last child.

                - lastElementChild (a list of or a singular dash component, string or number; required):
                    Returns the last child that is an element, and
                    None otherwise.

                - localName (string; required):
                    Returns the local name.

                - lookupNamespaceURI (required)

                - lookupPrefix (required)

                - matches (required):
                    Returns True if matching selectors against
                    element's root yields element, and False
                    otherwise.

                - name (string; required)

                - namespaceURI (string; required):
                    Returns the namespace.

                - nextElementSibling (a list of or a singular dash component, string or number; required):
                    Returns the first following sibling that is an
                    element, and None otherwise.

                - nextSibling (boolean | number | string | dict | list; required):
                    Returns the next sibling.

                - nodeName (string; required):
                    Returns a string appropriate for the type of node.

                - nodeType (number; required):
                    Returns the type of node.

                - nodeValue (string; required)

                - nonce (string; optional)

                - normalize (required):
                    Removes empty exclusive Text nodes and
                    concatenates the data of remaining contiguous
                    exclusive Text nodes into the first of their
                    nodes.

                - offsetHeight (number; required)

                - offsetLeft (number; required)

                - offsetParent (a list of or a singular dash component, string or number; required)

                - offsetTop (number; required)

                - offsetWidth (number; required)

                - onabort (required):
                    Fires when the user aborts the download.
                    @,param,ev, ,The event.

                - onanimationcancel (required)

                - onanimationend (required)

                - onanimationiteration (required)

                - onanimationstart (required)

                - onauxclick (required)

                - onbeforeinput (required)

                - onblur (required):
                    Fires when the object loses the input focus.
                    @,param,ev, ,The focus event.

                - oncancel (required)

                - oncanplay (required):
                    Occurs when playback is possible, but would
                    require further buffering. @,param,ev, ,The event.

                - oncanplaythrough (required)

                - onchange (required):
                    Fires when the contents of the object or selection
                    have changed. @,param,ev, ,The event.

                - onclick (required):
                    Fires when the user clicks the left mouse button
                    on the object @,param,ev, ,The mouse event.

                - onclose (required)

                - oncontextmenu (required):
                    Fires when the user clicks the right mouse button
                    in the client area, opening the context menu.
                    @,param,ev, ,The mouse event.

                - oncopy (required)

                - oncuechange (required)

                - oncut (required)

                - ondblclick (required):
                    Fires when the user double-clicks the object.
                    @,param,ev, ,The mouse event.

                - ondrag (required):
                    Fires on the source object continuously during a
                    drag operation. @,param,ev, ,The event.

                - ondragend (required):
                    Fires on the source object when the user releases
                    the mouse at the close of a drag operation.
                    @,param,ev, ,The event.

                - ondragenter (required):
                    Fires on the target element when the user drags
                    the object to a valid drop target. @,param,ev,
                    ,The drag event.

                - ondragleave (required):
                    Fires on the target object when the user moves the
                    mouse out of a valid drop target during a drag
                    operation. @,param,ev, ,The drag event.

                - ondragover (required):
                    Fires on the target element continuously while the
                    user drags the object over a valid drop target.
                    @,param,ev, ,The event.

                - ondragstart (required):
                    Fires on the source object when the user starts to
                    drag a text selection or selected object.
                    @,param,ev, ,The event.

                - ondrop (required)

                - ondurationchange (required):
                    Occurs when the duration attribute is updated.
                    @,param,ev, ,The event.

                - onemptied (required):
                    Occurs when the media element is reset to its
                    initial state. @,param,ev, ,The event.

                - onended (required):
                    Occurs when the end of playback is reached.
                    @,param,ev, ,The event.

                - onerror (dict; required):
                    Fires when an error occurs during object loading.
                    @,param,ev, ,The event.

                    `onerror` is a dict with keys:


                - onfocus (required):
                    Fires when the object receives focus. @,param,ev,
                    ,The event.

                - onformdata (required)

                - onfullscreenchange (required)

                - onfullscreenerror (required)

                - ongotpointercapture (required)

                - oninput (required)

                - oninvalid (required)

                - onkeydown (required):
                    Fires when the user presses a key. @,param,ev,
                    ,The keyboard event.

                - onkeypress (required):
                    Fires when the user presses an alphanumeric key.
                    @,param,ev, ,The event. @,deprecated.

                - onkeyup (required):
                    Fires when the user releases a key. @,param,ev,
                    ,The keyboard event.

                - onload (required):
                    Fires immediately after the browser loads the
                    object. @,param,ev, ,The event.

                - onloadeddata (required):
                    Occurs when media data is loaded at the current
                    playback position. @,param,ev, ,The event.

                - onloadedmetadata (required):
                    Occurs when the duration and dimensions of the
                    media have been determined. @,param,ev, ,The
                    event.

                - onloadstart (required):
                    Occurs when Internet Explorer begins looking for
                    media data. @,param,ev, ,The event.

                - onlostpointercapture (required)

                - onmousedown (required):
                    Fires when the user clicks the object with either
                    mouse button. @,param,ev, ,The mouse event.

                - onmouseenter (required)

                - onmouseleave (required)

                - onmousemove (required):
                    Fires when the user moves the mouse over the
                    object. @,param,ev, ,The mouse event.

                - onmouseout (required):
                    Fires when the user moves the mouse pointer
                    outside the boundaries of the object. @,param,ev,
                    ,The mouse event.

                - onmouseover (required):
                    Fires when the user moves the mouse pointer into
                    the object. @,param,ev, ,The mouse event.

                - onmouseup (required):
                    Fires when the user releases a mouse button while
                    the mouse is over the object. @,param,ev, ,The
                    mouse event.

                - onpaste (required)

                - onpause (required):
                    Occurs when playback is paused. @,param,ev, ,The
                    event.

                - onplay (required):
                    Occurs when the play method is requested.
                    @,param,ev, ,The event.

                - onplaying (required):
                    Occurs when the audio or video has started
                    playing. @,param,ev, ,The event.

                - onpointercancel (required)

                - onpointerdown (required)

                - onpointerenter (required)

                - onpointerleave (required)

                - onpointermove (required)

                - onpointerout (required)

                - onpointerover (required)

                - onpointerup (required)

                - onprogress (required):
                    Occurs to indicate progress while downloading
                    media data. @,param,ev, ,The event.

                - onratechange (required):
                    Occurs when the playback rate is increased or
                    decreased. @,param,ev, ,The event.

                - onreset (required):
                    Fires when the user resets a form. @,param,ev,
                    ,The event.

                - onresize (required)

                - onscroll (required):
                    Fires when the user repositions the scroll box in
                    the scroll bar on the object. @,param,ev, ,The
                    event.

                - onsecuritypolicyviolation (required)

                - onseeked (required):
                    Occurs when the seek operation ends. @,param,ev,
                    ,The event.

                - onseeking (required):
                    Occurs when the current playback position is
                    moved. @,param,ev, ,The event.

                - onselect (required):
                    Fires when the current selection changes.
                    @,param,ev, ,The event.

                - onselectionchange (required)

                - onselectstart (required)

                - onslotchange (required)

                - onstalled (required):
                    Occurs when the download has stopped. @,param,ev,
                    ,The event.

                - onsubmit (required)

                - onsuspend (required):
                    Occurs if the load operation has been
                    intentionally halted. @,param,ev, ,The event.

                - ontimeupdate (required):
                    Occurs to indicate the current playback position.
                    @,param,ev, ,The event.

                - ontoggle (required)

                - ontouchcancel (optional)

                - ontouchend (optional)

                - ontouchmove (optional)

                - ontouchstart (optional)

                - ontransitioncancel (required)

                - ontransitionend (required)

                - ontransitionrun (required)

                - ontransitionstart (required)

                - onvolumechange (required):
                    Occurs when the volume is changed, or playback is
                    muted or unmuted. @,param,ev, ,The event.

                - onwaiting (required):
                    Occurs when playback stops because the next frame
                    of a video resource is not available. @,param,ev,
                    ,The event.

                - onwebkitanimationend (required)

                - onwebkitanimationiteration (required)

                - onwebkitanimationstart (required)

                - onwebkittransitionend (required)

                - onwheel (required)

                - outerHTML (string; required)

                - outerText (string; required)

                - ownerDocument (boolean | number | string | dict | list; required)

                - parentElement (boolean | number | string | dict | list; required):
                    Returns the parent element.

                - parentNode (boolean | number | string | dict | list; required):
                    Returns the parent.

                - part (dict with strings as keys and values of type string; required)

                - prefix (string; required):
                    Returns the namespace prefix.

                - prepend (required):
                    Inserts nodes before the first child of node,
                    while replacing strings in nodes with equivalent
                    Text nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - previousElementSibling (a list of or a singular dash component, string or number; required):
                    Returns the first preceding sibling that is an
                    element, and None otherwise.

                - previousSibling (boolean | number | string | dict | list; required):
                    Returns the previous sibling.

                - querySelector (dict; required):
                    Returns the first element that is a descendant of
                    node that matches selectors.

                    `querySelector` is a dict with keys:


                - querySelectorAll (dict; required):
                    Returns all element descendants of node that match
                    selectors.

                    `querySelectorAll` is a dict with keys:


                - releasePointerCapture (required)

                - remove (required):
                    Removes node.

                - removeAttribute (required):
                    Removes element's first attribute whose qualified
                    name is qualifiedName.

                - removeAttributeNS (required):
                    Removes element's attribute whose namespace is
                    namespace and local name is localName.

                - removeAttributeNode (required)

                - removeChild (required)

                - removeEventListener (required)

                - replaceChild (required)

                - replaceChildren (required):
                    Replace all children of node with nodes, while
                    replacing strings in nodes with equivalent Text
                    nodes.  Throws a \"HierarchyRequestError\"
                    DOMException if the constraints of the node tree
                    are violated.

                - replaceWith (required):
                    Replaces node with nodes, while replacing strings
                    in nodes with equivalent Text nodes.  Throws a
                    \"HierarchyRequestError\" DOMException if the
                    constraints of the node tree are violated.

                - requestFullscreen (required):
                    Displays element fullscreen and resolves promise
                    when done.  When supplied, options's navigationUI
                    member indicates whether showing navigation UI
                    while in fullscreen is preferred or not. If set to
                    \"show\", navigation simplicity is preferred over
                    screen space, and if set to \"hide\", more screen
                    space is preferred. User agents are always free to
                    honor user preference over the application's. The
                    default value \"auto\" indicates no application
                    preference.

                - requestPointerLock (required)

                - role (string; required)

                - scroll (dict; required)

                    `scroll` is a dict with keys:


                - scrollBy (dict; required)

                    `scrollBy` is a dict with keys:


                - scrollHeight (number; required)

                - scrollIntoView (required)

                - scrollLeft (number; required)

                - scrollTo (dict; required)

                    `scrollTo` is a dict with keys:


                - scrollTop (number; required)

                - scrollWidth (number; required)

                - setAttribute (required):
                    Sets the value of element's first attribute whose
                    qualified name is qualifiedName to value.

                - setAttributeNS (required):
                    Sets the value of element's attribute whose
                    namespace is namespace and local name is localName
                    to value.

                - setAttributeNode (required)

                - setAttributeNodeNS (required)

                - setPointerCapture (required)

                - shadowRoot (boolean | number | string | dict | list; required):
                    Returns element's shadow root, if any, and if
                    shadow root's mode is \"open\", and None
                    otherwise.

                - slot (string; required):
                    Returns the value of element's slot content
                    attribute. Can be set to change it.

                - spellcheck (boolean; required)

                - style (dict with strings as keys and values of type string; required)

                - tabIndex (number; required)

                - tagName (string; required):
                    Returns the HTML-uppercased qualified name.

                - textContent (string; required)

                - title (string; required)

                - toggleAttribute (required):
                    If force is not given, \"toggles\" qualifiedName,
                    removing it if it is present and adding it if it
                    is not present. If force is True, adds
                    qualifiedName. If force is False, removes
                    qualifiedName.  Returns True if qualifiedName is
                    now present, and False otherwise.

                - translate (boolean; required)

                - webkitMatchesSelector (required)

            - attachInternals (required)

            - attachShadow (required):
                Creates a shadow root for element and returns it.

            - attributes (dict; required)

                `attributes` is a dict with strings as keys and values
                of type dict with keys:

    - ATTRIBUTE_NODE (number; required)

    - CDATA_SECTION_NODE (number; required):
        node is a CDATASection node.

    - COMMENT_NODE (number; required):
        node is a Comment node.

    - DOCUMENT_FRAGMENT_NODE (number; required):
        node is a DocumentFragment node.

    - DOCUMENT_NODE (number; required):
        node is a document.

    - DOCUMENT_POSITION_CONTAINED_BY (number; required):
        Set when other is a descendant of node.

    - DOCUMENT_POSITION_CONTAINS (number; required):
        Set when other is an ancestor of node.

    - DOCUMENT_POSITION_DISCONNECTED (number; required):
        Set when node and other are not in the same tree.

    - DOCUMENT_POSITION_FOLLOWING (number; required):
        Set when other is following node.

    - DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC (number; required)

    - DOCUMENT_POSITION_PRECEDING (number; required):
        Set when other is preceding node.

    - DOCUMENT_TYPE_NODE (number; required):
        node is a doctype.

    - ELEMENT_NODE (number; required):
        node is an element.

    - ENTITY_NODE (number; required)

    - ENTITY_REFERENCE_NODE (number; required)

    - NOTATION_NODE (number; required)

    - PROCESSING_INSTRUCTION_NODE (number; required):
        node is a ProcessingInstruction node.

    - TEXT_NODE (number; required):
        node is a Text node.

    - addEventListener (required):
        Appends an event listener for events whose type attribute
        value is type. The callback argument sets the callback that
        will be invoked when the event is dispatched.  The options
        argument sets listener-specific options. For compatibility
        this can be a boolean, in which case the method behaves
        exactly as if the value was specified as options's capture.
        When set to True, options's capture prevents callback from
        being invoked when the event's eventPhase attribute value is
        BUBBLING_PHASE. When False (or not present), callback will not
        be invoked when event's eventPhase attribute value is
        CAPTURING_PHASE. Either way, callback will be invoked if
        event's eventPhase attribute value is AT_TARGET.  When set to
        True, options's passive indicates that the callback will not
        cancel the event by invoking preventDefault(). This is used to
        enable performance optimizations described in § 2.8 Observing
        event listeners.  When set to True, options's once indicates
        that the callback will only be invoked once after which the
        event listener will be removed.  If an AbortSignal is passed
        for options's signal, then the event listener will be removed
        when signal is aborted.  The event listener is appended to
        target's event listener list and is not appended if it has the
        same type, callback, and capture.

    - appendChild (required)

    - baseURI (string; required):
        Returns node's node document's document base URL.

    - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
        Returns the children.

    - cloneNode (required):
        Returns a copy of node. If deep is True, the copy also
        includes the node's descendants.

    - compareDocumentPosition (required):
        Returns a bitmask indicating the position of other relative to
        node.

    - contains (required):
        Returns True if other is an inclusive descendant of node, and
        False otherwise.

    - dispatchEvent (required):
        Dispatches a synthetic event event to target and returns True
        if either event's cancelable attribute value is False or its
        preventDefault() method was not invoked, and False otherwise.

    - firstChild (boolean | number | string | dict | list; required):
        Returns the first child.

    - getRootNode (required):
        Returns node's root.

    - hasChildNodes (required):
        Returns whether node has children.

    - insertBefore (required)

    - isConnected (boolean; required):
        Returns True if node is connected and False otherwise.

    - isDefaultNamespace (required)

    - isEqualNode (required):
        Returns whether node and otherNode have the same properties.

    - isSameNode (required)

    - lastChild (boolean | number | string | dict | list; required):
        Returns the last child.

    - localName (string; required)

    - lookupNamespaceURI (required)

    - lookupPrefix (required)

    - name (string; required)

    - namespaceURI (string; required)

    - nextSibling (boolean | number | string | dict | list; required):
        Returns the next sibling.

    - nodeName (string; required):
        Returns a string appropriate for the type of node.

    - nodeType (number; required):
        Returns the type of node.

    - nodeValue (string; required)

    - normalize (required):
        Removes empty exclusive Text nodes and concatenates the data
        of remaining contiguous exclusive Text nodes into the first of
        their nodes.

    - ownerDocument (boolean | number | string | dict | list; required)

    - ownerElement (a list of or a singular dash component, string or number; required)

    - parentElement (boolean | number | string | dict | list; required):
        Returns the parent element.

    - parentNode (boolean | number | string | dict | list; required):
        Returns the parent.

    - prefix (string; required)

    - previousSibling (boolean | number | string | dict | list; required):
        Returns the previous sibling.

    - removeChild (required)

    - removeEventListener (required):
        Removes the event listener in target's event listener list
        with the same type, callback, and options.

    - replaceChild (required)

    - specified (boolean; required)

    - textContent (string; required)

    - value (string; required)

            - autocapitalize (string; required)

            - autofocus (boolean; required)

            - baseURI (string; required):
                Returns node's node document's document base URL.

            - before (required):
                Inserts nodes just before node, while replacing
                strings in nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - blur (required)

            - childElementCount (number; required)

            - childNodes (dict with strings as keys and values of type boolean | number | string | dict | list; required):
                Returns the children.

            - children (dict with strings as keys and values of type a list of or a singular dash component, string or number; required):
                Returns the child elements.

            - classList (dict with strings as keys and values of type string; required):
                Allows for manipulation of element's class content
                attribute as a set of whitespace-separated tokens
                through a DOMTokenList object.

            - className (string; required):
                Returns the value of element's class content
                attribute. Can be set to change it.

            - click (required)

            - clientHeight (number; required)

            - clientLeft (number; required)

            - clientTop (number; required)

            - clientWidth (number; required)

            - cloneNode (required):
                Returns a copy of node. If deep is True, the copy also
                includes the node's descendants.

            - closest (dict; required):
                Returns the first (starting at element) inclusive
                ancestor that matches selectors, and None otherwise.

                `closest` is a dict with keys:


            - compareDocumentPosition (required):
                Returns a bitmask indicating the position of other
                relative to node.

            - contains (required):
                Returns True if other is an inclusive descendant of
                node, and False otherwise.

            - contentEditable (string; required)

            - dataset (dict with strings as keys and values of type string; required)

            - dir (string; required)

            - dispatchEvent (required):
                Dispatches a synthetic event event to target and
                returns True if either event's cancelable attribute
                value is False or its preventDefault() method was not
                invoked, and False otherwise.

            - draggable (boolean; required)

            - enterKeyHint (string; required)

            - firstChild (boolean | number | string | dict | list; required):
                Returns the first child.

            - firstElementChild (a list of or a singular dash component, string or number; required):
                Returns the first child that is an element, and None
                otherwise.

            - focus (required)

            - getAnimations (required)

            - getAttribute (required):
                Returns element's first attribute whose qualified name
                is qualifiedName, and None if there is no such
                attribute otherwise.

            - getAttributeNS (required):
                Returns element's attribute whose namespace is
                namespace and local name is localName, and None if
                there is no such attribute otherwise.

            - getAttributeNames (required):
                Returns the qualified names of all element's
                attributes. Can contain duplicates.

            - getAttributeNode (required)

            - getAttributeNodeNS (required)

            - getBoundingClientRect (required)

            - getClientRects (required)

            - getElementsByClassName (required):
                Returns a HTMLCollection of the elements in the object
                on which the method was invoked (a document or an
                element) that have all the classes given by
                classNames. The classNames argument is interpreted as
                a space-separated list of classes.

            - getElementsByTagName (dict; required)

                `getElementsByTagName` is a dict with keys:


            - getElementsByTagNameNS (dict; required)

                `getElementsByTagNameNS` is a dict with keys:


            - getRootNode (required):
                Returns node's root.

            - hasAttribute (required):
                Returns True if element has an attribute whose
                qualified name is qualifiedName, and False otherwise.

            - hasAttributeNS (required):
                Returns True if element has an attribute whose
                namespace is namespace and local name is localName.

            - hasAttributes (required):
                Returns True if element has attributes, and False
                otherwise.

            - hasChildNodes (required):
                Returns whether node has children.

            - hasPointerCapture (required)

            - hidden (boolean; required)

            - id (string; required):
                Returns the value of element's id content attribute.
                Can be set to change it.

            - inert (boolean; required)

            - innerHTML (string; required)

            - innerText (string; required)

            - inputMode (string; required)

            - insertAdjacentElement (required)

            - insertAdjacentHTML (required)

            - insertAdjacentText (required)

            - insertBefore (required)

            - isConnected (boolean; required):
                Returns True if node is connected and False otherwise.

            - isContentEditable (boolean; required)

            - isDefaultNamespace (required)

            - isEqualNode (required):
                Returns whether node and otherNode have the same
                properties.

            - isSameNode (required)

            - lang (string; required)

            - lastChild (boolean | number | string | dict | list; required):
                Returns the last child.

            - lastElementChild (a list of or a singular dash component, string or number; required):
                Returns the last child that is an element, and None
                otherwise.

            - localName (string; required):
                Returns the local name.

            - lookupNamespaceURI (required)

            - lookupPrefix (required)

            - matches (required):
                Returns True if matching selectors against element's
                root yields element, and False otherwise.

            - namespaceURI (string; required):
                Returns the namespace.

            - nextElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first following sibling that is an
                element, and None otherwise.

            - nextSibling (boolean | number | string | dict | list; required):
                Returns the next sibling.

            - nodeName (string; required):
                Returns a string appropriate for the type of node.

            - nodeType (number; required):
                Returns the type of node.

            - nodeValue (string; required)

            - nonce (string; optional)

            - normalize (required):
                Removes empty exclusive Text nodes and concatenates
                the data of remaining contiguous exclusive Text nodes
                into the first of their nodes.

            - offsetHeight (number; required)

            - offsetLeft (number; required)

            - offsetParent (a list of or a singular dash component, string or number; required)

            - offsetTop (number; required)

            - offsetWidth (number; required)

            - onabort (required):
                Fires when the user aborts the download. @,param,ev,
                ,The event.

            - onanimationcancel (required)

            - onanimationend (required)

            - onanimationiteration (required)

            - onanimationstart (required)

            - onauxclick (required)

            - onbeforeinput (required)

            - onblur (required):
                Fires when the object loses the input focus.
                @,param,ev, ,The focus event.

            - oncancel (required)

            - oncanplay (required):
                Occurs when playback is possible, but would require
                further buffering. @,param,ev, ,The event.

            - oncanplaythrough (required)

            - onchange (required):
                Fires when the contents of the object or selection
                have changed. @,param,ev, ,The event.

            - onclick (required):
                Fires when the user clicks the left mouse button on
                the object @,param,ev, ,The mouse event.

            - onclose (required)

            - oncontextmenu (required):
                Fires when the user clicks the right mouse button in
                the client area, opening the context menu. @,param,ev,
                ,The mouse event.

            - oncopy (required)

            - oncuechange (required)

            - oncut (required)

            - ondblclick (required):
                Fires when the user double-clicks the object.
                @,param,ev, ,The mouse event.

            - ondrag (required):
                Fires on the source object continuously during a drag
                operation. @,param,ev, ,The event.

            - ondragend (required):
                Fires on the source object when the user releases the
                mouse at the close of a drag operation. @,param,ev,
                ,The event.

            - ondragenter (required):
                Fires on the target element when the user drags the
                object to a valid drop target. @,param,ev, ,The drag
                event.

            - ondragleave (required):
                Fires on the target object when the user moves the
                mouse out of a valid drop target during a drag
                operation. @,param,ev, ,The drag event.

            - ondragover (required):
                Fires on the target element continuously while the
                user drags the object over a valid drop target.
                @,param,ev, ,The event.

            - ondragstart (required):
                Fires on the source object when the user starts to
                drag a text selection or selected object. @,param,ev,
                ,The event.

            - ondrop (required)

            - ondurationchange (required):
                Occurs when the duration attribute is updated.
                @,param,ev, ,The event.

            - onemptied (required):
                Occurs when the media element is reset to its initial
                state. @,param,ev, ,The event.

            - onended (required):
                Occurs when the end of playback is reached.
                @,param,ev, ,The event.

            - onerror (dict; required):
                Fires when an error occurs during object loading.
                @,param,ev, ,The event.

                `onerror` is a dict with keys:


            - onfocus (required):
                Fires when the object receives focus. @,param,ev, ,The
                event.

            - onformdata (required)

            - onfullscreenchange (required)

            - onfullscreenerror (required)

            - ongotpointercapture (required)

            - oninput (required)

            - oninvalid (required)

            - onkeydown (required):
                Fires when the user presses a key. @,param,ev, ,The
                keyboard event.

            - onkeypress (required):
                Fires when the user presses an alphanumeric key.
                @,param,ev, ,The event. @,deprecated.

            - onkeyup (required):
                Fires when the user releases a key. @,param,ev, ,The
                keyboard event.

            - onload (required):
                Fires immediately after the browser loads the object.
                @,param,ev, ,The event.

            - onloadeddata (required):
                Occurs when media data is loaded at the current
                playback position. @,param,ev, ,The event.

            - onloadedmetadata (required):
                Occurs when the duration and dimensions of the media
                have been determined. @,param,ev, ,The event.

            - onloadstart (required):
                Occurs when Internet Explorer begins looking for media
                data. @,param,ev, ,The event.

            - onlostpointercapture (required)

            - onmousedown (required):
                Fires when the user clicks the object with either
                mouse button. @,param,ev, ,The mouse event.

            - onmouseenter (required)

            - onmouseleave (required)

            - onmousemove (required):
                Fires when the user moves the mouse over the object.
                @,param,ev, ,The mouse event.

            - onmouseout (required):
                Fires when the user moves the mouse pointer outside
                the boundaries of the object. @,param,ev, ,The mouse
                event.

            - onmouseover (required):
                Fires when the user moves the mouse pointer into the
                object. @,param,ev, ,The mouse event.

            - onmouseup (required):
                Fires when the user releases a mouse button while the
                mouse is over the object. @,param,ev, ,The mouse
                event.

            - onpaste (required)

            - onpause (required):
                Occurs when playback is paused. @,param,ev, ,The
                event.

            - onplay (required):
                Occurs when the play method is requested. @,param,ev,
                ,The event.

            - onplaying (required):
                Occurs when the audio or video has started playing.
                @,param,ev, ,The event.

            - onpointercancel (required)

            - onpointerdown (required)

            - onpointerenter (required)

            - onpointerleave (required)

            - onpointermove (required)

            - onpointerout (required)

            - onpointerover (required)

            - onpointerup (required)

            - onprogress (required):
                Occurs to indicate progress while downloading media
                data. @,param,ev, ,The event.

            - onratechange (required):
                Occurs when the playback rate is increased or
                decreased. @,param,ev, ,The event.

            - onreset (required):
                Fires when the user resets a form. @,param,ev, ,The
                event.

            - onresize (required)

            - onscroll (required):
                Fires when the user repositions the scroll box in the
                scroll bar on the object. @,param,ev, ,The event.

            - onsecuritypolicyviolation (required)

            - onseeked (required):
                Occurs when the seek operation ends. @,param,ev, ,The
                event.

            - onseeking (required):
                Occurs when the current playback position is moved.
                @,param,ev, ,The event.

            - onselect (required):
                Fires when the current selection changes. @,param,ev,
                ,The event.

            - onselectionchange (required)

            - onselectstart (required)

            - onslotchange (required)

            - onstalled (required):
                Occurs when the download has stopped. @,param,ev, ,The
                event.

            - onsubmit (required)

            - onsuspend (required):
                Occurs if the load operation has been intentionally
                halted. @,param,ev, ,The event.

            - ontimeupdate (required):
                Occurs to indicate the current playback position.
                @,param,ev, ,The event.

            - ontoggle (required)

            - ontouchcancel (optional)

            - ontouchend (optional)

            - ontouchmove (optional)

            - ontouchstart (optional)

            - ontransitioncancel (required)

            - ontransitionend (required)

            - ontransitionrun (required)

            - ontransitionstart (required)

            - onvolumechange (required):
                Occurs when the volume is changed, or playback is
                muted or unmuted. @,param,ev, ,The event.

            - onwaiting (required):
                Occurs when playback stops because the next frame of a
                video resource is not available. @,param,ev, ,The
                event.

            - onwebkitanimationend (required)

            - onwebkitanimationiteration (required)

            - onwebkitanimationstart (required)

            - onwebkittransitionend (required)

            - onwheel (required)

            - outerHTML (string; required)

            - outerText (string; required)

            - ownerDocument (boolean | number | string | dict | list; required)

            - parentElement (boolean | number | string | dict | list; required):
                Returns the parent element.

            - parentNode (boolean | number | string | dict | list; required):
                Returns the parent.

            - part (dict with strings as keys and values of type string; required)

            - prefix (string; required):
                Returns the namespace prefix.

            - prepend (required):
                Inserts nodes before the first child of node, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - previousElementSibling (a list of or a singular dash component, string or number; required):
                Returns the first preceding sibling that is an
                element, and None otherwise.

            - previousSibling (boolean | number | string | dict | list; required):
                Returns the previous sibling.

            - querySelector (dict; required):
                Returns the first element that is a descendant of node
                that matches selectors.

                `querySelector` is a dict with keys:


            - querySelectorAll (dict; required):
                Returns all element descendants of node that match
                selectors.

                `querySelectorAll` is a dict with keys:


            - releasePointerCapture (required)

            - remove (required):
                Removes node.

            - removeAttribute (required):
                Removes element's first attribute whose qualified name
                is qualifiedName.

            - removeAttributeNS (required):
                Removes element's attribute whose namespace is
                namespace and local name is localName.

            - removeAttributeNode (required)

            - removeChild (required)

            - removeEventListener (required)

            - replaceChild (required)

            - replaceChildren (required):
                Replace all children of node with nodes, while
                replacing strings in nodes with equivalent Text nodes.
                Throws a \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - replaceWith (required):
                Replaces node with nodes, while replacing strings in
                nodes with equivalent Text nodes.  Throws a
                \"HierarchyRequestError\" DOMException if the
                constraints of the node tree are violated.

            - requestFullscreen (required):
                Displays element fullscreen and resolves promise when
                done.  When supplied, options's navigationUI member
                indicates whether showing navigation UI while in
                fullscreen is preferred or not. If set to \"show\",
                navigation simplicity is preferred over screen space,
                and if set to \"hide\", more screen space is
                preferred. User agents are always free to honor user
                preference over the application's. The default value
                \"auto\" indicates no application preference.

            - requestPointerLock (required)

            - role (string; required)

            - scroll (dict; required)

                `scroll` is a dict with keys:


            - scrollBy (dict; required)

                `scrollBy` is a dict with keys:


            - scrollHeight (number; required)

            - scrollIntoView (required)

            - scrollLeft (number; required)

            - scrollTo (dict; required)

                `scrollTo` is a dict with keys:


            - scrollTop (number; required)

            - scrollWidth (number; required)

            - setAttribute (required):
                Sets the value of element's first attribute whose
                qualified name is qualifiedName to value.

            - setAttributeNS (required):
                Sets the value of element's attribute whose namespace
                is namespace and local name is localName to value.

            - setAttributeNode (required)

            - setAttributeNodeNS (required)

            - setPointerCapture (required)

            - shadowRoot (boolean | number | string | dict | list; required):
                Returns element's shadow root, if any, and if shadow
                root's mode is \"open\", and None otherwise.

            - slot (string; required):
                Returns the value of element's slot content attribute.
                Can be set to change it.

            - spellcheck (boolean; required)

            - style (dict with strings as keys and values of type string; required)

            - tabIndex (number; required)

            - tagName (string; required):
                Returns the HTML-uppercased qualified name.

            - textContent (string; required)

            - title (string; required)

            - toggleAttribute (required):
                If force is not given, \"toggles\" qualifiedName,
                removing it if it is present and adding it if it is
                not present. If force is True, adds qualifiedName. If
                force is False, removes qualifiedName.  Returns True
                if qualifiedName is now present, and False otherwise.

            - translate (boolean; required)

            - webkitMatchesSelector (required)

        - yearRange (number | list of numbers; optional):
            Number of years either side (e.g. 10) or array of
            upper/lower range (e.g. [1900, 2015]).

        - yearSuffix (string; optional):
            Additional text to append to the year in the title.

    - defaultDate (string; optional)

    - disableVisualSelection (boolean | number | string | dict | list; optional)

    - dragToScroll (boolean; optional)

    - dropdownMenu (boolean | number | string | dict | list; optional)

    - editor (string; optional)

    - enterBeginsEditing (boolean; optional)

    - enterMoves (dict; optional)

        `enterMoves` is a dict with keys:

        - col (number; required)

        - row (number; required)

    - fillHandle (boolean | number | string | dict | list; optional)

    - filter (boolean; optional)

    - filteringCaseSensitive (boolean; optional)

    - filters (boolean; optional)

    - fixedColumnsLeft (number; optional)

    - fixedColumnsStart (number; optional)

    - fixedRowsBottom (number; optional)

    - fixedRowsTop (number; optional)

    - formulas (dict; optional)

        `formulas` is a dict with keys:

        - engine (boolean | number | string | dict | list; required)

        - sheetName (string; optional)

    - fragmentSelection (boolean | number | string | dict | list; optional)

    - height (string | number; optional)

    - hiddenColumns (boolean | number | string | dict | list; optional)

    - hiddenRows (boolean | number | string | dict | list; optional)

    - imeFastEdit (boolean; optional)

    - init (optional)

    - invalidCellClassName (string; optional)

    - isEmptyCol (optional)

    - isEmptyRow (optional)

    - label (dict; optional)

        `label` is a dict with keys:

        - position (a value equal to: 'after', 'before'; optional)

        - property (string; optional)

        - value (string; optional)

    - language (string; optional)

    - layoutDirection (a value equal to: 'ltr', 'rtl', 'inherit'; optional)

    - licenseKey (string; optional)

    - locale (string; optional)

    - manualColumnFreeze (boolean; optional)

    - manualColumnMove (list of numbers; optional)

    - manualColumnResize (list of numbers; optional)

    - manualRowMove (list of numbers; optional)

    - manualRowResize (list of numbers; optional)

    - maxCols (number; optional)

    - maxRows (number; optional)

    - mergeCells (boolean | number | string | dict | list; optional)

    - minCols (number; optional)

    - minRows (number; optional)

    - minSpareCols (number; optional)

    - minSpareRows (number; optional)

    - modifyAutoColumnSizeSeed (optional)

    - modifyAutofillRange (optional)

    - modifyColHeader (optional)

    - modifyColWidth (optional)

    - modifyColumnHeaderHeight (optional)

    - modifyColumnHeaderValue (optional)

    - modifyCopyableRange (optional)

    - modifyData (optional)

    - modifyFiltersMultiSelectValue (optional)

    - modifyFocusOnTabNavigation (optional)

    - modifyFocusedElement (optional)

    - modifyGetCellCoords (optional)

    - modifyRowData (optional)

    - modifyRowHeader (optional)

    - modifyRowHeaderWidth (optional)

    - modifyRowHeight (optional)

    - modifySourceData (optional)

    - modifyTransformEnd (optional)

    - modifyTransformFocus (optional)

    - modifyTransformStart (optional)

    - multiColumnSorting (boolean | number | string | dict | list; optional)

    - navigableHeaders (boolean; optional)

    - nestedHeaders (dict with strings as keys and values of type list of strings; optional)

    - nestedRows (boolean; optional)

    - noWordWrapClassName (string; optional)

    - numericFormat (dict; optional)

        `numericFormat` is a dict with keys:

        - culture (string; optional)

        - pattern (string; required)

    - observeDOMVisibility (boolean; optional)

    - outsideClickDeselects (optional)

    - persistentState (boolean; optional)

    - persistentStateLoad (optional)

    - persistentStateReset (optional)

    - persistentStateSave (optional)

    - placeholder (string; optional)

    - placeholderCellClassName (string; optional)

    - preventOverflow (boolean | number | string | dict | list; optional)

    - preventWheel (boolean; optional)

    - readOnly (boolean; optional)

    - readOnlyCellClassName (string; optional)

    - renderAllColumns (boolean; optional)

    - renderAllRows (boolean; optional)

    - renderer (string; optional)

    - rowHeaderWidth (number | list of numbers; optional)

    - rowHeaders (list of strings; optional)

    - rowHeights (string | number | list of strings | list of numbers; optional)

    - search (boolean | number | string | dict | list; optional)

    - selectOptions (list of strings; optional)

    - selectionMode (a value equal to: 'single', 'range', 'multiple'; optional)

    - skipColumnOnPaste (boolean; optional)

    - skipRowOnPaste (boolean; optional)

    - sortByRelevance (boolean; optional)

    - source (list of strings | list of numbers; optional)

    - startCols (number; optional)

    - startRows (number; optional)

    - stretchH (a value equal to: 'none', 'all', 'last'; optional)

    - strict (boolean; optional)

    - tabMoves (dict; optional)

        `tabMoves` is a dict with keys:

        - col (number; required)

        - row (number; required)

    - tabNavigation (boolean; optional)

    - tableClassName (string | list of strings; optional)

    - title (string; optional)

    - trimDropdown (boolean; optional)

    - trimRows (list of numbers; optional)

    - trimWhitespace (boolean; optional)

    - type (string; optional)

    - uncheckedTemplate (string | number; optional)

    - undo (boolean; optional)

    - validator (string; optional)

    - viewportColumnRenderingOffset (number; optional)

    - viewportRowRenderingOffset (number; optional)

    - visibleRows (number; optional)

    - width (string | number; optional)

    - wordWrap (boolean; optional)

- skipColumnOnPaste (boolean; optional)

- skipRowOnPaste (boolean; optional)

- sortByRelevance (boolean; optional)

- source (list of strings | list of numbers; optional)

- startCols (number; optional)

- startRows (number; optional)

- stretchH (a value equal to: 'none', 'all', 'last'; optional)

- strict (boolean; optional)

- style (dict; optional)

    `style` is a dict with keys:

    - KhtmlBoxAlign (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'stretch', 'center', 'end', 'start', 'baseline'; optional):
        The **`box-align`** CSS property specifies how an element
        aligns its contents across its layout in a perpendicular
        direction. The effect of the property is only visible if there
        is extra space in the box.  **Syntax**: `start | center | end
        | baseline | stretch`  **Initial value**: `stretch`
        @,deprecated.

    - KhtmlBoxDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'reverse'; optional):
        The **`box-direction`** CSS property specifies whether a box
        lays out its contents normally (from the top or left edge), or
        in reverse (from the bottom or right edge).  **Syntax**:
        `normal | reverse | inherit`  **Initial value**: `normal`
        @,deprecated.

    - KhtmlBoxFlex (boolean | number | string | dict | list; optional):
        The **`-moz-box-flex`** and **`-webkit-box-flex`** CSS
        properties specify how a `-moz-box` or `-webkit-box` grows to
        fill the box that contains it, in the direction of the
        containing box's layout.  **Syntax**: `<number>`  **Initial
        value**: `0` @,deprecated.

    - KhtmlBoxFlexGroup (boolean | number | string | dict | list; optional):
        The **`box-flex-group`** CSS property assigns the flexbox's
        child elements to a flex group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - KhtmlBoxLines (a value equal to: 'inherit', 'single', 'multiple', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`box-lines`** CSS property determines whether the box
        may have a single or multiple lines (rows for horizontally
        oriented boxes, columns for vertically oriented boxes).
        **Syntax**: `single | multiple`  **Initial value**: `single`
        @,deprecated.

    - KhtmlBoxOrdinalGroup (boolean | number | string | dict | list; optional):
        The **`box-ordinal-group`** CSS property assigns the flexbox's
        child elements to an ordinal group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - KhtmlBoxOrient (a value equal to: 'vertical', 'horizontal', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'block-axis', 'inline-axis'; optional):
        The **`box-orient`** CSS property sets whether an element lays
        out its contents horizontally or vertically.  **Syntax**:
        `horizontal | vertical | inline-axis | block-axis | inherit`
        **Initial value**: `inline-axis` (`horizontal` in XUL)
        @,deprecated.

    - KhtmlBoxPack (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'justify'; optional):
        The **`-moz-box-pack`** and **`-webkit-box-pack`** CSS
        properties specify how a `-moz-box` or `-webkit-box` packs its
        contents in the direction of its layout. The effect of this is
        only visible if there is extra space in the box.  **Syntax**:
        `start | center | end | justify`  **Initial value**: `start`
        @,deprecated.

    - KhtmlLineBreak (a value equal to: 'loose', 'strict', 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'anywhere'; optional):
        The **`line-break`** CSS property sets how to break lines of
        Chinese, Japanese, or Korean (CJK) text when working with
        punctuation and symbols.  **Syntax**: `auto | loose | normal |
        strict | anywhere`  **Initial value**: `auto` @,deprecated.

    - KhtmlOpacity (boolean | number | string | dict | list; optional):
        The **`opacity`** CSS property sets the opacity of an element.
        Opacity is the degree to which content behind an element is
        hidden, and is the opposite of transparency.  **Syntax**:
        `<alpha-value>`  **Initial value**: `1` @,deprecated.

    - KhtmlUserSelect (a value equal to: 'text', 'inherit', 'none', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain', '-moz-none', 'element'; optional):
        The **`user-select`** CSS property controls whether the user
        can select text. This doesn't have any effect on content
        loaded as part of a browser's user interface (its chrome),
        except in textboxes.  **Syntax**: `auto | text | none |
        contain | all`  **Initial value**: `auto` @,deprecated.

    - MozAnimation (boolean | number | string | dict | list; optional):
        The **`animation`** shorthand CSS property applies an
        animation between styles. It is a shorthand for
        `animation-name`, `animation-duration`,
        `animation-timing-function`, `animation-delay`,
        `animation-iteration-count`, `animation-direction`,
        `animation-fill-mode`, and `animation-play-state`.
        **Syntax**: `<single-animation>#`.

    - MozAnimationDelay (boolean | number | string | dict | list; optional):
        The **`animation-delay`** CSS property specifies the amount of
        time to wait from applying the animation to an element before
        beginning to perform the animation. The animation can start
        later, immediately from its beginning, or immediately and
        partway through the animation.  **Syntax**: `<time>#`
        **Initial value**: `0s`.

    - MozAnimationDirection (boolean | number | string | dict | list; optional):
        The **`animation-direction`** CSS property sets whether an
        animation should play forward, backward, or alternate back and
        forth between playing the sequence forward and backward.
        **Syntax**: `<single-animation-direction>#`  **Initial
        value**: `normal`.

    - MozAnimationDuration (boolean | number | string | dict | list; optional):
        The **`animation-duration`** CSS property sets the length of
        time that an animation takes to complete one cycle.
        **Syntax**: `<time>#`  **Initial value**: `0s`.

    - MozAnimationFillMode (boolean | number | string | dict | list; optional):
        The **`animation-fill-mode`** CSS property sets how a CSS
        animation applies styles to its target before and after its
        execution.  **Syntax**: `<single-animation-fill-mode>#`
        **Initial value**: `none`.

    - MozAnimationIterationCount (boolean | number | string | dict | list; optional):
        The **`animation-iteration-count`** CSS property sets the
        number of times an animation sequence should be played before
        stopping.  **Syntax**: `<single-animation-iteration-count>#`
        **Initial value**: `1`.

    - MozAnimationName (boolean | number | string | dict | list; optional):
        The **`animation-name`** CSS property specifies the names of
        one or more `@keyframes` at-rules that describe the animation
        to apply to an element. Multiple `@keyframe` at-rules are
        specified as a comma-separated list of names. If the specified
        name does not match any `@keyframe` at-rule, no properties are
        animated.  **Syntax**: `[ none | <keyframes-name> ]#`
        **Initial value**: `none`.

    - MozAnimationPlayState (boolean | number | string | dict | list; optional):
        The **`animation-play-state`** CSS property sets whether an
        animation is running or paused.  **Syntax**:
        `<single-animation-play-state>#`  **Initial value**:
        `running`.

    - MozAnimationTimingFunction (boolean | number | string | dict | list; optional):
        The **`animation-timing-function`** CSS property sets how an
        animation progresses through the duration of each cycle.
        **Syntax**: `<easing-function>#`  **Initial value**: `ease`.

    - MozAppearance (a value equal to: 'checkbox', 'inherit', 'range', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'button', 'listbox', 'menulist', 'radio', 'searchfield', 'menulist-button', 'textfield', '-moz-mac-unified-toolbar', '-moz-win-borderless-glass', '-moz-win-browsertabbar-toolbox', '-moz-win-communications-toolbox', '-moz-win-communicationstext', '-moz-win-exclude-glass', '-moz-win-glass', '-moz-win-media-toolbox', '-moz-win-mediatext', '-moz-window-button-box', '-moz-window-button-box-maximized', '-moz-window-button-close', '-moz-window-button-maximize', '-moz-window-button-minimize', '-moz-window-button-restore', '-moz-window-frame-bottom', '-moz-window-frame-left', '-moz-window-frame-right', '-moz-window-titlebar', '-moz-window-titlebar-maximized', 'button-arrow-down', 'button-arrow-next', 'button-arrow-previous', 'button-arrow-up', 'button-bevel', 'button-focus', 'caret', 'checkbox-container', 'checkbox-label', 'checkmenuitem', 'dualbutton', 'groupbox', 'listitem', 'menuarrow', 'menubar', 'menucheckbox', 'menuimage', 'menuitem', 'menuitemtext', 'menulist-text', 'menulist-textfield', 'menupopup', 'menuradio', 'menuseparator', 'meterbar', 'meterchunk', 'progressbar', 'progressbar-vertical', 'progresschunk', 'progresschunk-vertical', 'radio-container', 'radio-label', 'radiomenuitem', 'range-thumb', 'resizer', 'resizerpanel', 'scale-horizontal', 'scale-vertical', 'scalethumb-horizontal', 'scalethumb-vertical', 'scalethumbend', 'scalethumbstart', 'scalethumbtick', 'scrollbarbutton-down', 'scrollbarbutton-left', 'scrollbarbutton-right', 'scrollbarbutton-up', 'scrollbarthumb-horizontal', 'scrollbarthumb-vertical', 'scrollbartrack-horizontal', 'scrollbartrack-vertical', 'separator', 'sheet', 'spinner', 'spinner-downbutton', 'spinner-textfield', 'spinner-upbutton', 'splitter', 'statusbar', 'statusbarpanel', 'tab', 'tab-scroll-arrow-back', 'tab-scroll-arrow-forward', 'tabpanel', 'tabpanels', 'textfield-multiline', 'toolbar', 'toolbarbutton', 'toolbarbutton-dropdown', 'toolbargripper', 'toolbox', 'tooltip', 'treeheader', 'treeheadercell', 'treeheadersortarrow', 'treeitem', 'treeline', 'treetwisty', 'treetwistyopen', 'treeview'; optional):
        The **`appearance`** CSS property is used to control native
        appearance of UI controls, that are based on operating
        system's theme.  **Syntax**: `none | button |
        button-arrow-down | button-arrow-next | button-arrow-previous
        | button-arrow-up | button-bevel | button-focus | caret |
        checkbox | checkbox-container | checkbox-label | checkmenuitem
        | dualbutton | groupbox | listbox | listitem | menuarrow |
        menubar | menucheckbox | menuimage | menuitem | menuitemtext |
        menulist | menulist-button | menulist-text |
        menulist-textfield | menupopup | menuradio | menuseparator |
        meterbar | meterchunk | progressbar | progressbar-vertical |
        progresschunk | progresschunk-vertical | radio |
        radio-container | radio-label | radiomenuitem | range |
        range-thumb | resizer | resizerpanel | scale-horizontal |
        scalethumbend | scalethumb-horizontal | scalethumbstart |
        scalethumbtick | scalethumb-vertical | scale-vertical |
        scrollbarbutton-down | scrollbarbutton-left |
        scrollbarbutton-right | scrollbarbutton-up |
        scrollbarthumb-horizontal | scrollbarthumb-vertical |
        scrollbartrack-horizontal | scrollbartrack-vertical |
        searchfield | separator | sheet | spinner | spinner-downbutton
        | spinner-textfield | spinner-upbutton | splitter | statusbar
        | statusbarpanel | tab | tabpanel | tabpanels |
        tab-scroll-arrow-back | tab-scroll-arrow-forward | textfield |
        textfield-multiline | toolbar | toolbarbutton |
        toolbarbutton-dropdown | toolbargripper | toolbox | tooltip |
        treeheader | treeheadercell | treeheadersortarrow | treeitem |
        treeline | treetwisty | treetwistyopen | treeview |
        -moz-mac-unified-toolbar | -moz-win-borderless-glass |
        -moz-win-browsertabbar-toolbox | -moz-win-communicationstext |
        -moz-win-communications-toolbox | -moz-win-exclude-glass |
        -moz-win-glass | -moz-win-mediatext | -moz-win-media-toolbox |
        -moz-window-button-box | -moz-window-button-box-maximized |
        -moz-window-button-close | -moz-window-button-maximize |
        -moz-window-button-minimize | -moz-window-button-restore |
        -moz-window-frame-bottom | -moz-window-frame-left |
        -moz-window-frame-right | -moz-window-titlebar |
        -moz-window-titlebar-maximized`  **Initial value**: `none`
        (but this value is overridden in the user agent CSS).

    - MozBackfaceVisibility (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible'; optional):
        The **`backface-visibility`** CSS property sets whether the
        back face of an element is visible when turned towards the
        user.  **Syntax**: `visible | hidden`  **Initial value**:
        `visible` @,deprecated.

    - MozBackgroundClip (boolean | number | string | dict | list; optional):
        The **`background-clip`** CSS property sets whether an
        element's background extends underneath its border box,
        padding box, or content box.  **Syntax**: `<box>#`  **Initial
        value**: `border-box` @,deprecated.

    - MozBackgroundInlinePolicy (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'clone', 'slice'; optional):
        The **`box-decoration-break`** CSS property specifies how an
        element's fragments should be rendered when broken across
        multiple lines, columns, or pages.  **Syntax**: `slice |
        clone`  **Initial value**: `slice` @,deprecated.

    - MozBackgroundOrigin (boolean | number | string | dict | list; optional):
        The **`background-origin`** CSS property sets the background's
        origin: from the border start, inside the border, or inside
        the padding.  **Syntax**: `<box>#`  **Initial value**:
        `padding-box` @,deprecated.

    - MozBackgroundSize (string | number; optional):
        The **`background-size`** CSS property sets the size of the
        element's background image. The image can be left to its
        natural size, stretched, or constrained to fit the available
        space.  **Syntax**: `<bg-size>#`  **Initial value**: `auto
        auto` @,deprecated.

    - MozBinding (boolean | number | string | dict | list; optional):
        The **`-moz-binding`** CSS property is used by Mozilla-based
        applications to attach an XBL binding to a DOM element.
        **Syntax**: `<url> | none`  **Initial value**: `none`.

    - MozBorderBottomColors (boolean | number | string | dict | list; optional):
        In Mozilla applications like Firefox, the
        **`-moz-border-bottom-colors`** CSS property sets a list of
        colors for the bottom border.  **Syntax**: `<color>+ | none`
        **Initial value**: `none`.

    - MozBorderEndColor (boolean | number | string | dict | list; optional):
        The **`border-inline-end-color`** CSS property defines the
        color of the logical inline-end border of an element, which
        maps to a physical border color depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-color`, `border-right-color`,
        `border-bottom-color`, or `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>`  **Initial value**: `currentcolor`.

    - MozBorderEndStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-inline-end-style`** CSS property defines the
        style of the logical inline end border of an element, which
        maps to a physical border style depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-style`, `border-right-style`,
        `border-bottom-style`, or `border-left-style` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`.

    - MozBorderEndWidth (string | number; optional):
        The **`border-inline-end-width`** CSS property defines the
        width of the logical inline-end border of an element, which
        maps to a physical border width depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-width`, `border-right-width`,
        `border-bottom-width`, or `border-left-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`.

    - MozBorderImage (boolean | number | string | dict | list; optional):
        The **`border-image`** CSS property draws an image around a
        given element. It replaces the element's regular border.
        **Syntax**: `<'border-image-source'> || <'border-image-slice'>
        [ / <'border-image-width'> | / <'border-image-width'>? /
        <'border-image-outset'> ]? || <'border-image-repeat'>`.

    - MozBorderLeftColors (boolean | number | string | dict | list; optional):
        In Mozilla applications like Firefox, the
        **`-moz-border-left-colors`** CSS property sets a list of
        colors for the left border.  **Syntax**: `<color>+ | none`
        **Initial value**: `none`.

    - MozBorderRadius (string | number; optional):
        The **`border-radius`** CSS property rounds the corners of an
        element's outer border edge. You can set a single radius to
        make circular corners, or two radii to make elliptical
        corners.  **Syntax**: `<length-percentage>{1,4} [ /
        <length-percentage>{1,4} ]?` @,deprecated.

    - MozBorderRadiusBottomleft (string | number; optional):
        The **`border-bottom-left-radius`** CSS property rounds the
        bottom-left corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`
        @,deprecated.

    - MozBorderRadiusBottomright (string | number; optional):
        The **`border-bottom-right-radius`** CSS property rounds the
        bottom-right corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`
        @,deprecated.

    - MozBorderRadiusTopleft (string | number; optional):
        The **`border-top-left-radius`** CSS property rounds the
        top-left corner of an element by specifying the radius (or the
        radius of the semi-major and semi-minor axes) of the ellipse
        defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`
        @,deprecated.

    - MozBorderRadiusTopright (string | number; optional):
        The **`border-top-right-radius`** CSS property rounds the
        top-right corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`
        @,deprecated.

    - MozBorderRightColors (boolean | number | string | dict | list; optional):
        In Mozilla applications like Firefox, the
        **`-moz-border-right-colors`** CSS property sets a list of
        colors for the right border.  **Syntax**: `<color>+ | none`
        **Initial value**: `none`.

    - MozBorderStartColor (boolean | number | string | dict | list; optional):
        The **`border-inline-start-color`** CSS property defines the
        color of the logical inline start border of an element, which
        maps to a physical border color depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-color`, `border-right-color`,
        `border-bottom-color`, or `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>`  **Initial value**: `currentcolor`.

    - MozBorderStartStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-inline-start-style`** CSS property defines the
        style of the logical inline start border of an element, which
        maps to a physical border style depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-style`, `border-right-style`,
        `border-bottom-style`, or `border-left-style` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`.

    - MozBorderTopColors (boolean | number | string | dict | list; optional):
        In Mozilla applications like Firefox, the
        **`-moz-border-top-colors`** CSS property sets a list of
        colors for the top border.  **Syntax**: `<color>+ | none`
        **Initial value**: `none`.

    - MozBoxAlign (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'stretch', 'center', 'end', 'start', 'baseline'; optional):
        The **`box-align`** CSS property specifies how an element
        aligns its contents across its layout in a perpendicular
        direction. The effect of the property is only visible if there
        is extra space in the box.  **Syntax**: `start | center | end
        | baseline | stretch`  **Initial value**: `stretch`
        @,deprecated.

    - MozBoxDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'reverse'; optional):
        The **`box-direction`** CSS property specifies whether a box
        lays out its contents normally (from the top or left edge), or
        in reverse (from the bottom or right edge).  **Syntax**:
        `normal | reverse | inherit`  **Initial value**: `normal`
        @,deprecated.

    - MozBoxFlex (boolean | number | string | dict | list; optional):
        The **`-moz-box-flex`** and **`-webkit-box-flex`** CSS
        properties specify how a `-moz-box` or `-webkit-box` grows to
        fill the box that contains it, in the direction of the
        containing box's layout.  **Syntax**: `<number>`  **Initial
        value**: `0` @,deprecated.

    - MozBoxOrdinalGroup (boolean | number | string | dict | list; optional):
        The **`box-ordinal-group`** CSS property assigns the flexbox's
        child elements to an ordinal group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - MozBoxOrient (a value equal to: 'vertical', 'horizontal', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'block-axis', 'inline-axis'; optional):
        The **`box-orient`** CSS property sets whether an element lays
        out its contents horizontally or vertically.  **Syntax**:
        `horizontal | vertical | inline-axis | block-axis | inherit`
        **Initial value**: `inline-axis` (`horizontal` in XUL)
        @,deprecated.

    - MozBoxPack (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'justify'; optional):
        The **`-moz-box-pack`** and **`-webkit-box-pack`** CSS
        properties specify how a `-moz-box` or `-webkit-box` packs its
        contents in the direction of its layout. The effect of this is
        only visible if there is extra space in the box.  **Syntax**:
        `start | center | end | justify`  **Initial value**: `start`
        @,deprecated.

    - MozBoxShadow (boolean | number | string | dict | list; optional):
        The **`box-shadow`** CSS property adds shadow effects around
        an element's frame. You can set multiple effects separated by
        commas. A box shadow is described by X and Y offsets relative
        to the element, blur and spread radius, and color.
        **Syntax**: `none | <shadow>#`  **Initial value**: `none`
        @,deprecated.

    - MozBoxSizing (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'border-box', 'content-box'; optional):
        The **`box-sizing`** CSS property sets how the total width and
        height of an element is calculated.  **Syntax**: `content-box
        | border-box`  **Initial value**: `content-box`.

    - MozColumnCount (boolean | number | string | dict | list; optional):
        The **`column-count`** CSS property breaks an element's
        content into the specified number of columns.  **Syntax**:
        `<integer> | auto`  **Initial value**: `auto`.

    - MozColumnFill (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'balance', 'balance-all'; optional):
        The **`column-fill`** CSS property controls how an element's
        contents are balanced when broken into columns.  **Syntax**:
        `auto | balance | balance-all`  **Initial value**: `balance`.

    - MozColumnRule (string | number; optional):
        The **`column-rule`** shorthand CSS property sets the width,
        style, and color of the line drawn between columns in a
        multi-column layout.  **Syntax**: `<'column-rule-width'> ||
        <'column-rule-style'> || <'column-rule-color'>`.

    - MozColumnRuleColor (boolean | number | string | dict | list; optional):
        The **`column-rule-color`** CSS property sets the color of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<color>`  **Initial value**: `currentcolor`.

    - MozColumnRuleStyle (boolean | number | string | dict | list; optional):
        The **`column-rule-style`** CSS property sets the style of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<'border-style'>`  **Initial value**: `none`.

    - MozColumnRuleWidth (string | number; optional):
        The **`column-rule-width`** CSS property sets the width of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<'border-width'>`  **Initial value**: `medium`.

    - MozColumnWidth (string | number; optional):
        The **`column-width`** CSS property sets the ideal column
        width in a multi-column layout. The container will have as
        many columns as can fit without any of them having a width
        less than the `column-width` value. If the width of the
        container is narrower than the specified value, the single
        column's width will be smaller than the declared column width.
        **Syntax**: `<length> | auto`  **Initial value**: `auto`.

    - MozColumns (string | number; optional):
        The **`columns`** CSS shorthand property sets the number of
        columns to use when drawing an element's contents, as well as
        those columns' widths.  **Syntax**: `<'column-width'> ||
        <'column-count'>`.

    - MozContextProperties (boolean | number | string | dict | list; optional):
        The **`-moz-context-properties`** property can be used within
        privileged contexts in Firefox to share the values of
        specified properties of the element with a child SVG image.
        **Syntax**: `none | [ fill | fill-opacity | stroke |
        stroke-opacity ]#`  **Initial value**: `none`.

    - MozFloatEdge (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'border-box', 'content-box', 'padding-box', 'margin-box'; optional):
        The non-standard **`-moz-float-edge`** CSS property specifies
        whether the height and width properties of the element include
        the margin, border, or padding thickness.  **Syntax**:
        `border-box | content-box | margin-box | padding-box`
        **Initial value**: `content-box` @,deprecated.

    - MozFontFeatureSettings (boolean | number | string | dict | list; optional):
        The **`font-feature-settings`** CSS property controls advanced
        typographic features in OpenType fonts.  **Syntax**: `normal |
        <feature-tag-value>#`  **Initial value**: `normal`.

    - MozFontLanguageOverride (boolean | number | string | dict | list; optional):
        The **`font-language-override`** CSS property controls the use
        of language-specific glyphs in a typeface.  **Syntax**:
        `normal | <string>`  **Initial value**: `normal`.

    - MozForceBrokenImageIcon (boolean | number | string | dict | list; optional):
        The **`-moz-force-broken-image-icon`** extended CSS property
        can be used to force the broken image icon to be shown even
        when a broken image has an `alt` attribute.  **Syntax**: `0 |
        1`  **Initial value**: `0` @,deprecated.

    - MozHyphens (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'manual'; optional):
        The **`hyphens`** CSS property specifies how words should be
        hyphenated when text wraps across multiple lines. It can
        prevent hyphenation entirely, hyphenate at manually-specified
        points within the text, or let the browser automatically
        insert hyphens where appropriate.  **Syntax**: `none | manual
        | auto`  **Initial value**: `manual`.

    - MozImageRegion (boolean | number | string | dict | list; optional):
        For certain XUL elements and pseudo-elements that use an image
        from the `list-style-image` property, this property specifies
        a region of the image that is used in place of the whole
        image. This allows elements to use different pieces of the
        same image to improve performance.  **Syntax**: `<shape> |
        auto`  **Initial value**: `auto`.

    - MozMarginEnd (string | number; optional):
        The **`margin-inline-end`** CSS property defines the logical
        inline end margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation. In other words, it
        corresponds to the `margin-top`, `margin-right`,
        `margin-bottom` or `margin-left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'margin-left'>`  **Initial
        value**: `0`.

    - MozMarginStart (string | number; optional):
        The **`margin-inline-start`** CSS property defines the logical
        inline start margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `margin-top`, `margin-right`, `margin-bottom`, or
        `margin-left` property depending on the values defined for
        `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'margin-left'>`  **Initial value**: `0`.

    - MozOpacity (boolean | number | string | dict | list; optional):
        The **`opacity`** CSS property sets the opacity of an element.
        Opacity is the degree to which content behind an element is
        hidden, and is the opposite of transparency.  **Syntax**:
        `<alpha-value>`  **Initial value**: `1` @,deprecated.

    - MozOrient (a value equal to: 'vertical', 'horizontal', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'block', 'inline'; optional):
        The **`-moz-orient`** CSS property specifies the orientation
        of the element to which it's applied.  **Syntax**: `inline |
        block | horizontal | vertical`  **Initial value**: `inline`.

    - MozOsxFontSmoothing (string | number; optional):
        The **`font-smooth`** CSS property controls the application of
        anti-aliasing when fonts are rendered.  **Syntax**: `auto |
        never | always | <absolute-size> | <length>`  **Initial
        value**: `auto`.

    - MozOutline (string | number; optional):
        The **`outline`** CSS shorthand property sets most of the
        outline properties in a single declaration.  **Syntax**: `[
        <'outline-color'> || <'outline-style'> || <'outline-width'> ]`
        @,deprecated.

    - MozOutlineColor (boolean | number | string | dict | list; optional):
        The **`outline-color`** CSS property sets the color of an
        element's outline.  **Syntax**: `<color> | invert`  **Initial
        value**: `invert`, for browsers supporting it, `currentColor`
        for the other @,deprecated.

    - MozOutlineRadius (string | number; optional):
        In Mozilla applications like Firefox, the
        **`-moz-outline-radius`** CSS shorthand property can be used
        to give an element's `outline` rounded corners.  **Syntax**:
        `<outline-radius>{1,4} [ / <outline-radius>{1,4} ]?`.

    - MozOutlineRadiusBottomleft (string | number; optional):
        In Mozilla applications, the
        **`-moz-outline-radius-bottomleft`** CSS property can be used
        to round the bottom-left corner of an element's `outline`.
        **Syntax**: `<outline-radius>`  **Initial value**: `0`.

    - MozOutlineRadiusBottomright (string | number; optional):
        In Mozilla applications, the
        **`-moz-outline-radius-bottomright`** CSS property can be used
        to round the bottom-right corner of an element's `outline`.
        **Syntax**: `<outline-radius>`  **Initial value**: `0`.

    - MozOutlineRadiusTopleft (string | number; optional):
        In Mozilla applications, the **`-moz-outline-radius-topleft`**
        CSS property can be used to round the top-left corner of an
        element's `outline`.  **Syntax**: `<outline-radius>`
        **Initial value**: `0`.

    - MozOutlineRadiusTopright (string | number; optional):
        In Mozilla applications, the
        **`-moz-outline-radius-topright`** CSS property can be used to
        round the top-right corner of an element's `outline`.
        **Syntax**: `<outline-radius>`  **Initial value**: `0`.

    - MozOutlineStyle (boolean | number | string | dict | list; optional):
        The **`outline-style`** CSS property sets the style of an
        element's outline. An outline is a line that is drawn around
        an element, outside the `border`.  **Syntax**: `auto |
        <'border-style'>`  **Initial value**: `none` @,deprecated.

    - MozOutlineWidth (string | number; optional):
        The CSS **`outline-width`** property sets the thickness of an
        element's outline. An outline is a line that is drawn around
        an element, outside the `border`.  **Syntax**: `<line-width>`
        **Initial value**: `medium` @,deprecated.

    - MozPaddingEnd (string | number; optional):
        The **`padding-inline-end`** CSS property defines the logical
        inline end padding of an element, which maps to a physical
        padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`.

    - MozPaddingStart (string | number; optional):
        The **`padding-inline-start`** CSS property defines the
        logical inline start padding of an element, which maps to a
        physical padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`.

    - MozPerspective (string | number; optional):
        The **`perspective`** CSS property determines the distance
        between the z=0 plane and the user in order to give a
        3D-positioned element some perspective.  **Syntax**: `none |
        <length>`  **Initial value**: `none` @,deprecated.

    - MozPerspectiveOrigin (string | number; optional):
        The **`perspective-origin`** CSS property determines the
        position at which the viewer is looking. It is used as the
        _vanishing point_ by the `perspective` property.  **Syntax**:
        `<position>`  **Initial value**: `50% 50%` @,deprecated.

    - MozStackSizing (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'ignore', 'stretch-to-fit'; optional):
        **`-moz-stack-sizing`** is an extended CSS property. Normally,
        a `<xul:stack>` will change its size so that all of its child
        elements are completely visible. For example, moving a child
        of the stack far to the right will widen the stack so the
        child remains visible.  **Syntax**: `ignore | stretch-to-fit`
        **Initial value**: `stretch-to-fit`.

    - MozTabSize (string | number; optional):
        The **`tab-size`** CSS property is used to customize the width
        of tab characters (U+0009).  **Syntax**: `<integer> |
        <length>`  **Initial value**: `8`.

    - MozTextAlignLast (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'left', 'right', 'justify'; optional):
        The **`text-align-last`** CSS property sets how the last line
        of a block or a line, right before a forced line break, is
        aligned.  **Syntax**: `auto | start | end | left | right |
        center | justify`  **Initial value**: `auto` @,deprecated.

    - MozTextBlink (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'blink'; optional):
        The **`-moz-text-blink`** non-standard Mozilla CSS extension
        specifies the blink mode.  **Syntax**: `none | blink`
        **Initial value**: `none`.

    - MozTextDecorationColor (boolean | number | string | dict | list; optional):
        The **`text-decoration-color`** CSS property sets the color of
        decorations added to text by `text-decoration-line`.
        **Syntax**: `<color>`  **Initial value**: `currentcolor`
        @,deprecated.

    - MozTextDecorationLine (boolean | number | string | dict | list; optional):
        The **`text-decoration-line`** CSS property sets the kind of
        decoration that is used on text in an element, such as an
        underline or overline.  **Syntax**: `none | [ underline ||
        overline || line-through || blink ] | spelling-error |
        grammar-error`  **Initial value**: `none` @,deprecated.

    - MozTextDecorationStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'dashed', 'dotted', 'double', 'solid', 'wavy'; optional):
        The **`text-decoration-style`** CSS property sets the style of
        the lines specified by `text-decoration-line`. The style
        applies to all lines that are set with `text-decoration-line`.
        **Syntax**: `solid | double | dotted | dashed | wavy`
        **Initial value**: `solid` @,deprecated.

    - MozTextSizeAdjust (boolean | number | string | dict | list; optional):
        The **`text-size-adjust`** CSS property controls the text
        inflation algorithm used on some smartphones and tablets.
        Other browsers will ignore this property.  **Syntax**: `none |
        auto | <percentage>`  **Initial value**: `auto` for smartphone
        browsers supporting inflation, `none` in other cases (and then
        not modifiable).

    - MozTransform (boolean | number | string | dict | list; optional):
        The **`transform`** CSS property lets you rotate, scale, skew,
        or translate an element. It modifies the coordinate space of
        the CSS visual formatting model.  **Syntax**: `none |
        <transform-list>`  **Initial value**: `none` @,deprecated.

    - MozTransformOrigin (string | number; optional):
        The **`transform-origin`** CSS property sets the origin for an
        element's transformations.  **Syntax**: `[ <length-percentage>
        | left | center | right | top | bottom ] | [ [
        <length-percentage> | left | center | right ] && [
        <length-percentage> | top | center | bottom ] ] <length>?`
        **Initial value**: `50% 50% 0` @,deprecated.

    - MozTransformStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'flat', 'preserve-3d'; optional):
        The **`transform-style`** CSS property sets whether children
        of an element are positioned in the 3D space or are flattened
        in the plane of the element.  **Syntax**: `flat | preserve-3d`
        **Initial value**: `flat` @,deprecated.

    - MozTransition (boolean | number | string | dict | list; optional):
        The **`transition`** CSS property is a shorthand property for
        `transition-property`, `transition-duration`,
        `transition-timing-function`, and `transition-delay`.
        **Syntax**: `<single-transition>#` @,deprecated.

    - MozTransitionDelay (boolean | number | string | dict | list; optional):
        The **`transition-delay`** CSS property specifies the duration
        to wait before starting a property's transition effect when
        its value changes.  **Syntax**: `<time>#`  **Initial value**:
        `0s` @,deprecated.

    - MozTransitionDuration (boolean | number | string | dict | list; optional):
        The **`transition-duration`** CSS property sets the length of
        time a transition animation should take to complete. By
        default, the value is `0s`, meaning that no animation will
        occur.  **Syntax**: `<time>#`  **Initial value**: `0s`
        @,deprecated.

    - MozTransitionProperty (boolean | number | string | dict | list; optional):
        The **`transition-property`** CSS property sets the CSS
        properties to which a transition effect should be applied.
        **Syntax**: `none | <single-transition-property>#`  **Initial
        value**: all @,deprecated.

    - MozTransitionTimingFunction (boolean | number | string | dict | list; optional):
        The **`transition-timing-function`** CSS property sets how
        intermediate values are calculated for CSS properties being
        affected by a transition effect.  **Syntax**:
        `<easing-function>#`  **Initial value**: `ease` @,deprecated.

    - MozUserFocus (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'ignore', 'select-after', 'select-all', 'select-before', 'select-menu', 'select-same'; optional):
        The **`-moz-user-focus`** CSS property is used to indicate
        whether an element can have the focus.  **Syntax**: `ignore |
        normal | select-after | select-before | select-menu |
        select-same | select-all | none`  **Initial value**: `none`.

    - MozUserInput (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'disabled', 'enabled'; optional):
        In Mozilla applications, **`-moz-user-input`** determines if
        an element will accept user input.  **Syntax**: `auto | none |
        enabled | disabled`  **Initial value**: `auto` @,deprecated.

    - MozUserModify (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'read-only', 'read-write', 'write-only'; optional):
        The **`user-modify`** property has no effect in Firefox. It
        was originally planned to determine whether or not the content
        of an element can be edited by a user.  **Syntax**: `read-only
        | read-write | write-only`  **Initial value**: `read-only`.

    - MozUserSelect (a value equal to: 'text', 'inherit', 'none', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain', '-moz-none', 'element'; optional):
        The **`user-select`** CSS property controls whether the user
        can select text. This doesn't have any effect on content
        loaded as part of a browser's user interface (its chrome),
        except in textboxes.  **Syntax**: `auto | text | none |
        contain | all`  **Initial value**: `auto`.

    - MozWindowDragging (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'drag', 'no-drag'; optional):
        The **`-moz-window-dragging`** CSS property specifies whether
        a window is draggable or not. It only works in Chrome code,
        and only on Mac OS X.  **Syntax**: `drag | no-drag`  **Initial
        value**: `drag`.

    - MozWindowShadow (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'default', 'menu', 'sheet', 'tooltip'; optional):
        The **`-moz-window-shadow`** CSS property specifies whether a
        window will have a shadow. It only works on Mac OS X.
        **Syntax**: `default | menu | tooltip | sheet | none`
        **Initial value**: `default`.

    - OAnimation (boolean | number | string | dict | list; optional):
        The **`animation`** shorthand CSS property applies an
        animation between styles. It is a shorthand for
        `animation-name`, `animation-duration`,
        `animation-timing-function`, `animation-delay`,
        `animation-iteration-count`, `animation-direction`,
        `animation-fill-mode`, and `animation-play-state`.
        **Syntax**: `<single-animation>#` @,deprecated.

    - OAnimationDelay (boolean | number | string | dict | list; optional):
        The **`animation-delay`** CSS property specifies the amount of
        time to wait from applying the animation to an element before
        beginning to perform the animation. The animation can start
        later, immediately from its beginning, or immediately and
        partway through the animation.  **Syntax**: `<time>#`
        **Initial value**: `0s` @,deprecated.

    - OAnimationDirection (boolean | number | string | dict | list; optional):
        The **`animation-direction`** CSS property sets whether an
        animation should play forward, backward, or alternate back and
        forth between playing the sequence forward and backward.
        **Syntax**: `<single-animation-direction>#`  **Initial
        value**: `normal` @,deprecated.

    - OAnimationDuration (boolean | number | string | dict | list; optional):
        The **`animation-duration`** CSS property sets the length of
        time that an animation takes to complete one cycle.
        **Syntax**: `<time>#`  **Initial value**: `0s` @,deprecated.

    - OAnimationFillMode (boolean | number | string | dict | list; optional):
        The **`animation-fill-mode`** CSS property sets how a CSS
        animation applies styles to its target before and after its
        execution.  **Syntax**: `<single-animation-fill-mode>#`
        **Initial value**: `none` @,deprecated.

    - OAnimationIterationCount (boolean | number | string | dict | list; optional):
        The **`animation-iteration-count`** CSS property sets the
        number of times an animation sequence should be played before
        stopping.  **Syntax**: `<single-animation-iteration-count>#`
        **Initial value**: `1` @,deprecated.

    - OAnimationName (boolean | number | string | dict | list; optional):
        The **`animation-name`** CSS property specifies the names of
        one or more `@keyframes` at-rules that describe the animation
        to apply to an element. Multiple `@keyframe` at-rules are
        specified as a comma-separated list of names. If the specified
        name does not match any `@keyframe` at-rule, no properties are
        animated.  **Syntax**: `[ none | <keyframes-name> ]#`
        **Initial value**: `none` @,deprecated.

    - OAnimationPlayState (boolean | number | string | dict | list; optional):
        The **`animation-play-state`** CSS property sets whether an
        animation is running or paused.  **Syntax**:
        `<single-animation-play-state>#`  **Initial value**: `running`
        @,deprecated.

    - OAnimationTimingFunction (boolean | number | string | dict | list; optional):
        The **`animation-timing-function`** CSS property sets how an
        animation progresses through the duration of each cycle.
        **Syntax**: `<easing-function>#`  **Initial value**: `ease`
        @,deprecated.

    - OBackgroundSize (string | number; optional):
        The **`background-size`** CSS property sets the size of the
        element's background image. The image can be left to its
        natural size, stretched, or constrained to fit the available
        space.  **Syntax**: `<bg-size>#`  **Initial value**: `auto
        auto` @,deprecated.

    - OBorderImage (boolean | number | string | dict | list; optional):
        The **`border-image`** CSS property draws an image around a
        given element. It replaces the element's regular border.
        **Syntax**: `<'border-image-source'> || <'border-image-slice'>
        [ / <'border-image-width'> | / <'border-image-width'>? /
        <'border-image-outset'> ]? || <'border-image-repeat'>`
        @,deprecated.

    - OObjectFit (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain', 'cover', 'fill', 'scale-down'; optional):
        The **`object-fit`** CSS property sets how the content of a
        replaced element, such as an `<img>` or `<video>`, should be
        resized to fit its container.  **Syntax**: `fill | contain |
        cover | none | scale-down`  **Initial value**: `fill`
        @,deprecated.

    - OObjectPosition (string | number; optional):
        The **`object-position`** CSS property specifies the alignment
        of the selected replaced element's contents within the
        element's box. Areas of the box which aren't covered by the
        replaced element's object will show the element's background.
        **Syntax**: `<position>`  **Initial value**: `50% 50%`
        @,deprecated.

    - OTabSize (string | number; optional):
        The **`tab-size`** CSS property is used to customize the width
        of tab characters (U+0009).  **Syntax**: `<integer> |
        <length>`  **Initial value**: `8` @,deprecated.

    - OTextOverflow (boolean | number | string | dict | list; optional):
        The **`text-overflow`** CSS property sets how hidden overflow
        content is signaled to users. It can be clipped, display an
        ellipsis ('`…`'), or display a custom string.  **Syntax**: `[
        clip | ellipsis | <string> ]{1,2}`  **Initial value**: `clip`
        @,deprecated.

    - OTransform (boolean | number | string | dict | list; optional):
        The **`transform`** CSS property lets you rotate, scale, skew,
        or translate an element. It modifies the coordinate space of
        the CSS visual formatting model.  **Syntax**: `none |
        <transform-list>`  **Initial value**: `none` @,deprecated.

    - OTransformOrigin (string | number; optional):
        The **`transform-origin`** CSS property sets the origin for an
        element's transformations.  **Syntax**: `[ <length-percentage>
        | left | center | right | top | bottom ] | [ [
        <length-percentage> | left | center | right ] && [
        <length-percentage> | top | center | bottom ] ] <length>?`
        **Initial value**: `50% 50% 0` @,deprecated.

    - OTransition (boolean | number | string | dict | list; optional):
        The **`transition`** CSS property is a shorthand property for
        `transition-property`, `transition-duration`,
        `transition-timing-function`, and `transition-delay`.
        **Syntax**: `<single-transition>#` @,deprecated.

    - OTransitionDelay (boolean | number | string | dict | list; optional):
        The **`transition-delay`** CSS property specifies the duration
        to wait before starting a property's transition effect when
        its value changes.  **Syntax**: `<time>#`  **Initial value**:
        `0s` @,deprecated.

    - OTransitionDuration (boolean | number | string | dict | list; optional):
        The **`transition-duration`** CSS property sets the length of
        time a transition animation should take to complete. By
        default, the value is `0s`, meaning that no animation will
        occur.  **Syntax**: `<time>#`  **Initial value**: `0s`
        @,deprecated.

    - OTransitionProperty (boolean | number | string | dict | list; optional):
        The **`transition-property`** CSS property sets the CSS
        properties to which a transition effect should be applied.
        **Syntax**: `none | <single-transition-property>#`  **Initial
        value**: all @,deprecated.

    - OTransitionTimingFunction (boolean | number | string | dict | list; optional):
        The **`transition-timing-function`** CSS property sets how
        intermediate values are calculated for CSS properties being
        affected by a transition effect.  **Syntax**:
        `<easing-function>#`  **Initial value**: `ease` @,deprecated.

    - WebkitAlignContent (boolean | number | string | dict | list; optional):
        The CSS **`align-content`** property sets the distribution of
        space between and around content items along a flexbox's
        cross-axis or a grid's block axis.  **Syntax**: `normal |
        <baseline-position> | <content-distribution> |
        <overflow-position>? <content-position>`  **Initial value**:
        `normal`.

    - WebkitAlignItems (boolean | number | string | dict | list; optional):
        The CSS **`align-items`** property sets the `align-self` value
        on all direct children as a group. In Flexbox, it controls the
        alignment of items on the Cross Axis. In Grid Layout, it
        controls the alignment of items on the Block Axis within their
        grid area.  **Syntax**: `normal | stretch |
        <baseline-position> | [ <overflow-position>? <self-position>
        ]`  **Initial value**: `normal`.

    - WebkitAlignSelf (boolean | number | string | dict | list; optional):
        The **`align-self`** CSS property overrides a grid or flex
        item's `align-items` value. In Grid, it aligns the item inside
        the grid area. In Flexbox, it aligns the item on the cross
        axis.  **Syntax**: `auto | normal | stretch |
        <baseline-position> | <overflow-position>? <self-position>`
        **Initial value**: `auto`.

    - WebkitAnimation (boolean | number | string | dict | list; optional):
        The **`animation`** shorthand CSS property applies an
        animation between styles. It is a shorthand for
        `animation-name`, `animation-duration`,
        `animation-timing-function`, `animation-delay`,
        `animation-iteration-count`, `animation-direction`,
        `animation-fill-mode`, and `animation-play-state`.
        **Syntax**: `<single-animation>#`.

    - WebkitAnimationDelay (boolean | number | string | dict | list; optional):
        The **`animation-delay`** CSS property specifies the amount of
        time to wait from applying the animation to an element before
        beginning to perform the animation. The animation can start
        later, immediately from its beginning, or immediately and
        partway through the animation.  **Syntax**: `<time>#`
        **Initial value**: `0s`.

    - WebkitAnimationDirection (boolean | number | string | dict | list; optional):
        The **`animation-direction`** CSS property sets whether an
        animation should play forward, backward, or alternate back and
        forth between playing the sequence forward and backward.
        **Syntax**: `<single-animation-direction>#`  **Initial
        value**: `normal`.

    - WebkitAnimationDuration (boolean | number | string | dict | list; optional):
        The **`animation-duration`** CSS property sets the length of
        time that an animation takes to complete one cycle.
        **Syntax**: `<time>#`  **Initial value**: `0s`.

    - WebkitAnimationFillMode (boolean | number | string | dict | list; optional):
        The **`animation-fill-mode`** CSS property sets how a CSS
        animation applies styles to its target before and after its
        execution.  **Syntax**: `<single-animation-fill-mode>#`
        **Initial value**: `none`.

    - WebkitAnimationIterationCount (boolean | number | string | dict | list; optional):
        The **`animation-iteration-count`** CSS property sets the
        number of times an animation sequence should be played before
        stopping.  **Syntax**: `<single-animation-iteration-count>#`
        **Initial value**: `1`.

    - WebkitAnimationName (boolean | number | string | dict | list; optional):
        The **`animation-name`** CSS property specifies the names of
        one or more `@keyframes` at-rules that describe the animation
        to apply to an element. Multiple `@keyframe` at-rules are
        specified as a comma-separated list of names. If the specified
        name does not match any `@keyframe` at-rule, no properties are
        animated.  **Syntax**: `[ none | <keyframes-name> ]#`
        **Initial value**: `none`.

    - WebkitAnimationPlayState (boolean | number | string | dict | list; optional):
        The **`animation-play-state`** CSS property sets whether an
        animation is running or paused.  **Syntax**:
        `<single-animation-play-state>#`  **Initial value**:
        `running`.

    - WebkitAnimationTimingFunction (boolean | number | string | dict | list; optional):
        The **`animation-timing-function`** CSS property sets how an
        animation progresses through the duration of each cycle.
        **Syntax**: `<easing-function>#`  **Initial value**: `ease`.

    - WebkitAppearance (a value equal to: 'checkbox', 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'button', 'listbox', 'menulist', 'meter', 'progress-bar', 'push-button', 'radio', 'searchfield', 'slider-horizontal', 'square-button', 'textarea', 'menulist-button', 'textfield', 'button-bevel', 'caret', 'listitem', 'menulist-text', 'menulist-textfield', '-apple-pay-button', 'default-button', 'inner-spin-button', 'media-controls-background', 'media-controls-fullscreen-background', 'media-current-time-display', 'media-enter-fullscreen-button', 'media-exit-fullscreen-button', 'media-fullscreen-button', 'media-mute-button', 'media-overlay-play-button', 'media-play-button', 'media-seek-back-button', 'media-seek-forward-button', 'media-slider', 'media-sliderthumb', 'media-time-remaining-display', 'media-toggle-closed-captions-button', 'media-volume-slider', 'media-volume-slider-container', 'media-volume-sliderthumb', 'progress-bar-value', 'searchfield-cancel-button', 'searchfield-decoration', 'searchfield-results-button', 'searchfield-results-decoration', 'slider-vertical', 'sliderthumb-horizontal', 'sliderthumb-vertical'; optional):
        The **`appearance`** CSS property is used to control native
        appearance of UI controls, that are based on operating
        system's theme.  **Syntax**: `none | button | button-bevel |
        caret | checkbox | default-button | inner-spin-button |
        listbox | listitem | media-controls-background |
        media-controls-fullscreen-background |
        media-current-time-display | media-enter-fullscreen-button |
        media-exit-fullscreen-button | media-fullscreen-button |
        media-mute-button | media-overlay-play-button |
        media-play-button | media-seek-back-button |
        media-seek-forward-button | media-slider | media-sliderthumb |
        media-time-remaining-display |
        media-toggle-closed-captions-button | media-volume-slider |
        media-volume-slider-container | media-volume-sliderthumb |
        menulist | menulist-button | menulist-text |
        menulist-textfield | meter | progress-bar | progress-bar-value
        | push-button | radio | searchfield |
        searchfield-cancel-button | searchfield-decoration |
        searchfield-results-button | searchfield-results-decoration |
        slider-horizontal | slider-vertical | sliderthumb-horizontal |
        sliderthumb-vertical | square-button | textarea | textfield |
        -apple-pay-button`  **Initial value**: `none` (but this value
        is overridden in the user agent CSS).

    - WebkitBackdropFilter (boolean | number | string | dict | list; optional):
        The **`backdrop-filter`** CSS property lets you apply
        graphical effects such as blurring or color shifting to the
        area behind an element. Because it applies to everything
        _behind_ the element, to see the effect you must make the
        element or its background at least partially transparent.
        **Syntax**: `none | <filter-function-list>`  **Initial
        value**: `none`.

    - WebkitBackfaceVisibility (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible'; optional):
        The **`backface-visibility`** CSS property sets whether the
        back face of an element is visible when turned towards the
        user.  **Syntax**: `visible | hidden`  **Initial value**:
        `visible`.

    - WebkitBackgroundClip (boolean | number | string | dict | list; optional):
        The **`background-clip`** CSS property sets whether an
        element's background extends underneath its border box,
        padding box, or content box.  **Syntax**: `<box>#`  **Initial
        value**: `border-box`.

    - WebkitBackgroundOrigin (boolean | number | string | dict | list; optional):
        The **`background-origin`** CSS property sets the background's
        origin: from the border start, inside the border, or inside
        the padding.  **Syntax**: `<box>#`  **Initial value**:
        `padding-box`.

    - WebkitBackgroundSize (string | number; optional):
        The **`background-size`** CSS property sets the size of the
        element's background image. The image can be left to its
        natural size, stretched, or constrained to fit the available
        space.  **Syntax**: `<bg-size>#`  **Initial value**: `auto
        auto`.

    - WebkitBorderBefore (string | number; optional):
        The **`-webkit-border-before`** CSS property is a shorthand
        property for setting the individual logical block start border
        property values in a single place in the style sheet.
        **Syntax**: `<'border-width'> || <'border-style'> || <color>`.

    - WebkitBorderBeforeColor (boolean | number | string | dict | list; optional):
        **Syntax**: `<color>`  **Initial value**: `currentcolor`.

    - WebkitBorderBeforeStyle (boolean | number | string | dict | list; optional):
        **Syntax**: `<'border-style'>`  **Initial value**: `none`.

    - WebkitBorderBeforeWidth (string | number; optional):
        **Syntax**: `<'border-width'>`  **Initial value**: `medium`.

    - WebkitBorderBottomLeftRadius (string | number; optional):
        The **`border-bottom-left-radius`** CSS property rounds the
        bottom-left corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`.

    - WebkitBorderBottomRightRadius (string | number; optional):
        The **`border-bottom-right-radius`** CSS property rounds the
        bottom-right corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`.

    - WebkitBorderImage (boolean | number | string | dict | list; optional):
        The **`border-image`** CSS property draws an image around a
        given element. It replaces the element's regular border.
        **Syntax**: `<'border-image-source'> || <'border-image-slice'>
        [ / <'border-image-width'> | / <'border-image-width'>? /
        <'border-image-outset'> ]? || <'border-image-repeat'>`.

    - WebkitBorderImageSlice (boolean | number | string | dict | list; optional):
        The **`border-image-slice`** CSS property divides the image
        specified by `border-image-source` into regions. These regions
        form the components of an element's border image.  **Syntax**:
        `<number-percentage>{1,4} && fill?`  **Initial value**:
        `100%`.

    - WebkitBorderRadius (string | number; optional):
        The **`border-radius`** CSS property rounds the corners of an
        element's outer border edge. You can set a single radius to
        make circular corners, or two radii to make elliptical
        corners.  **Syntax**: `<length-percentage>{1,4} [ /
        <length-percentage>{1,4} ]?`.

    - WebkitBorderTopLeftRadius (string | number; optional):
        The **`border-top-left-radius`** CSS property rounds the
        top-left corner of an element by specifying the radius (or the
        radius of the semi-major and semi-minor axes) of the ellipse
        defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`.

    - WebkitBorderTopRightRadius (string | number; optional):
        The **`border-top-right-radius`** CSS property rounds the
        top-right corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`.

    - WebkitBoxAlign (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'stretch', 'center', 'end', 'start', 'baseline'; optional):
        The **`box-align`** CSS property specifies how an element
        aligns its contents across its layout in a perpendicular
        direction. The effect of the property is only visible if there
        is extra space in the box.  **Syntax**: `start | center | end
        | baseline | stretch`  **Initial value**: `stretch`
        @,deprecated.

    - WebkitBoxDecorationBreak (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'clone', 'slice'; optional):
        The **`box-decoration-break`** CSS property specifies how an
        element's fragments should be rendered when broken across
        multiple lines, columns, or pages.  **Syntax**: `slice |
        clone`  **Initial value**: `slice`.

    - WebkitBoxDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'reverse'; optional):
        The **`box-direction`** CSS property specifies whether a box
        lays out its contents normally (from the top or left edge), or
        in reverse (from the bottom or right edge).  **Syntax**:
        `normal | reverse | inherit`  **Initial value**: `normal`
        @,deprecated.

    - WebkitBoxFlex (boolean | number | string | dict | list; optional):
        The **`-moz-box-flex`** and **`-webkit-box-flex`** CSS
        properties specify how a `-moz-box` or `-webkit-box` grows to
        fill the box that contains it, in the direction of the
        containing box's layout.  **Syntax**: `<number>`  **Initial
        value**: `0` @,deprecated.

    - WebkitBoxFlexGroup (boolean | number | string | dict | list; optional):
        The **`box-flex-group`** CSS property assigns the flexbox's
        child elements to a flex group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - WebkitBoxLines (a value equal to: 'inherit', 'single', 'multiple', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`box-lines`** CSS property determines whether the box
        may have a single or multiple lines (rows for horizontally
        oriented boxes, columns for vertically oriented boxes).
        **Syntax**: `single | multiple`  **Initial value**: `single`
        @,deprecated.

    - WebkitBoxOrdinalGroup (boolean | number | string | dict | list; optional):
        The **`box-ordinal-group`** CSS property assigns the flexbox's
        child elements to an ordinal group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - WebkitBoxOrient (a value equal to: 'vertical', 'horizontal', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'block-axis', 'inline-axis'; optional):
        The **`box-orient`** CSS property sets whether an element lays
        out its contents horizontally or vertically.  **Syntax**:
        `horizontal | vertical | inline-axis | block-axis | inherit`
        **Initial value**: `inline-axis` (`horizontal` in XUL)
        @,deprecated.

    - WebkitBoxPack (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'justify'; optional):
        The **`-moz-box-pack`** and **`-webkit-box-pack`** CSS
        properties specify how a `-moz-box` or `-webkit-box` packs its
        contents in the direction of its layout. The effect of this is
        only visible if there is extra space in the box.  **Syntax**:
        `start | center | end | justify`  **Initial value**: `start`
        @,deprecated.

    - WebkitBoxReflect (string | number; optional):
        The **`-webkit-box-reflect`** CSS property lets you reflect
        the content of an element in one specific direction.
        **Syntax**: `[ above | below | right | left ]? <length>?
        <image>?`  **Initial value**: `none`.

    - WebkitBoxShadow (boolean | number | string | dict | list; optional):
        The **`box-shadow`** CSS property adds shadow effects around
        an element's frame. You can set multiple effects separated by
        commas. A box shadow is described by X and Y offsets relative
        to the element, blur and spread radius, and color.
        **Syntax**: `none | <shadow>#`  **Initial value**: `none`.

    - WebkitBoxSizing (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'border-box', 'content-box'; optional):
        The **`box-sizing`** CSS property sets how the total width and
        height of an element is calculated.  **Syntax**: `content-box
        | border-box`  **Initial value**: `content-box`.

    - WebkitClipPath (boolean | number | string | dict | list; optional):
        The **`clip-path`** CSS property creates a clipping region
        that sets what part of an element should be shown. Parts that
        are inside the region are shown, while those outside are
        hidden.  **Syntax**: `<clip-source> | [ <basic-shape> ||
        <geometry-box> ] | none`  **Initial value**: `none`.

    - WebkitColumnCount (boolean | number | string | dict | list; optional):
        The **`column-count`** CSS property breaks an element's
        content into the specified number of columns.  **Syntax**:
        `<integer> | auto`  **Initial value**: `auto`.

    - WebkitColumnFill (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'balance', 'balance-all'; optional):
        The **`column-fill`** CSS property controls how an element's
        contents are balanced when broken into columns.  **Syntax**:
        `auto | balance | balance-all`  **Initial value**: `balance`.

    - WebkitColumnRule (string | number; optional):
        The **`column-rule`** shorthand CSS property sets the width,
        style, and color of the line drawn between columns in a
        multi-column layout.  **Syntax**: `<'column-rule-width'> ||
        <'column-rule-style'> || <'column-rule-color'>`.

    - WebkitColumnRuleColor (boolean | number | string | dict | list; optional):
        The **`column-rule-color`** CSS property sets the color of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<color>`  **Initial value**: `currentcolor`.

    - WebkitColumnRuleStyle (boolean | number | string | dict | list; optional):
        The **`column-rule-style`** CSS property sets the style of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<'border-style'>`  **Initial value**: `none`.

    - WebkitColumnRuleWidth (string | number; optional):
        The **`column-rule-width`** CSS property sets the width of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<'border-width'>`  **Initial value**: `medium`.

    - WebkitColumnSpan (a value equal to: 'inherit', 'none', 'all', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`column-span`** CSS property makes it possible for an
        element to span across all columns when its value is set to
        `all`.  **Syntax**: `none | all`  **Initial value**: `none`.

    - WebkitColumnWidth (string | number; optional):
        The **`column-width`** CSS property sets the ideal column
        width in a multi-column layout. The container will have as
        many columns as can fit without any of them having a width
        less than the `column-width` value. If the width of the
        container is narrower than the specified value, the single
        column's width will be smaller than the declared column width.
        **Syntax**: `<length> | auto`  **Initial value**: `auto`.

    - WebkitColumns (string | number; optional):
        The **`columns`** CSS shorthand property sets the number of
        columns to use when drawing an element's contents, as well as
        those columns' widths.  **Syntax**: `<'column-width'> ||
        <'column-count'>`.

    - WebkitFilter (boolean | number | string | dict | list; optional):
        The **`filter`** CSS property applies graphical effects like
        blur or color shift to an element. Filters are commonly used
        to adjust the rendering of images, backgrounds, and borders.
        **Syntax**: `none | <filter-function-list>`  **Initial
        value**: `none`.

    - WebkitFlex (string | number; optional):
        The **`flex`** CSS shorthand property sets how a flex _item_
        will grow or shrink to fit the space available in its flex
        container.  **Syntax**: `none | [ <'flex-grow'>
        <'flex-shrink'>? || <'flex-basis'> ]`.

    - WebkitFlexBasis (string | number; optional):
        The **`flex-basis`** CSS property sets the initial main size
        of a flex item. It sets the size of the content box unless
        otherwise set with `box-sizing`.  **Syntax**: `content |
        <'width'>`  **Initial value**: `auto`.

    - WebkitFlexDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'column', 'column-reverse', 'row', 'row-reverse'; optional):
        The **`flex-direction`** CSS property sets how flex items are
        placed in the flex container defining the main axis and the
        direction (normal or reversed).  **Syntax**: `row |
        row-reverse | column | column-reverse`  **Initial value**:
        `row`.

    - WebkitFlexFlow (boolean | number | string | dict | list; optional):
        The **`flex-flow`** CSS shorthand property specifies the
        direction of a flex container, as well as its wrapping
        behavior.  **Syntax**: `<'flex-direction'> || <'flex-wrap'>`.

    - WebkitFlexGrow (boolean | number | string | dict | list; optional):
        The **`flex-grow`** CSS property sets the flex grow factor of
        a flex item's main size.  **Syntax**: `<number>`  **Initial
        value**: `0`.

    - WebkitFlexShrink (boolean | number | string | dict | list; optional):
        The **`flex-shrink`** CSS property sets the flex shrink factor
        of a flex item. If the size of all flex items is larger than
        the flex container, items shrink to fit according to
        `flex-shrink`.  **Syntax**: `<number>`  **Initial value**:
        `1`.

    - WebkitFlexWrap (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'nowrap', 'wrap', 'wrap-reverse'; optional):
        The **`flex-wrap`** CSS property sets whether flex items are
        forced onto one line or can wrap onto multiple lines. If
        wrapping is allowed, it sets the direction that lines are
        stacked.  **Syntax**: `nowrap | wrap | wrap-reverse`
        **Initial value**: `nowrap`.

    - WebkitFontFeatureSettings (boolean | number | string | dict | list; optional):
        The **`font-feature-settings`** CSS property controls advanced
        typographic features in OpenType fonts.  **Syntax**: `normal |
        <feature-tag-value>#`  **Initial value**: `normal`.

    - WebkitFontKerning (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal'; optional):
        The **`font-kerning`** CSS property sets the use of the
        kerning information stored in a font.  **Syntax**: `auto |
        normal | none`  **Initial value**: `auto`.

    - WebkitFontSmoothing (string | number; optional):
        The **`font-smooth`** CSS property controls the application of
        anti-aliasing when fonts are rendered.  **Syntax**: `auto |
        never | always | <absolute-size> | <length>`  **Initial
        value**: `auto`.

    - WebkitFontVariantLigatures (boolean | number | string | dict | list; optional):
        The **`font-variant-ligatures`** CSS property controls which
        ligatures and contextual forms are used in textual content of
        the elements it applies to. This leads to more harmonized
        forms in the resulting text.  **Syntax**: `normal | none | [
        <common-lig-values> || <discretionary-lig-values> ||
        <historical-lig-values> || <contextual-alt-values> ]`
        **Initial value**: `normal`.

    - WebkitHyphenateCharacter (boolean | number | string | dict | list; optional):
        The **`hyphenate-character`** CSS property sets the character
        (or string) used at the end of a line before a hyphenation
        break.  **Syntax**: `auto | <string>`  **Initial value**:
        `auto`.

    - WebkitHyphens (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'manual'; optional):
        The **`hyphens`** CSS property specifies how words should be
        hyphenated when text wraps across multiple lines. It can
        prevent hyphenation entirely, hyphenate at manually-specified
        points within the text, or let the browser automatically
        insert hyphens where appropriate.  **Syntax**: `none | manual
        | auto`  **Initial value**: `manual`.

    - WebkitInitialLetter (boolean | number | string | dict | list; optional):
        The `initial-letter` CSS property sets styling for dropped,
        raised, and sunken initial letters.  **Syntax**: `normal | [
        <number> <integer>? ]`  **Initial value**: `normal`.

    - WebkitJustifyContent (boolean | number | string | dict | list; optional):
        The CSS **`justify-content`** property defines how the browser
        distributes space between and around content items along the
        main-axis of a flex container, and the inline axis of a grid
        container.  **Syntax**: `normal | <content-distribution> |
        <overflow-position>? [ <content-position> | left | right ]`
        **Initial value**: `normal`.

    - WebkitLineBreak (a value equal to: 'loose', 'strict', 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'anywhere'; optional):
        The **`line-break`** CSS property sets how to break lines of
        Chinese, Japanese, or Korean (CJK) text when working with
        punctuation and symbols.  **Syntax**: `auto | loose | normal |
        strict | anywhere`  **Initial value**: `auto`.

    - WebkitLineClamp (boolean | number | string | dict | list; optional):
        The **`-webkit-line-clamp`** CSS property allows limiting of
        the contents of a block to the specified number of lines.
        **Syntax**: `none | <integer>`  **Initial value**: `none`.

    - WebkitMarginEnd (string | number; optional):
        The **`margin-inline-end`** CSS property defines the logical
        inline end margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation. In other words, it
        corresponds to the `margin-top`, `margin-right`,
        `margin-bottom` or `margin-left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'margin-left'>`  **Initial
        value**: `0`.

    - WebkitMarginStart (string | number; optional):
        The **`margin-inline-start`** CSS property defines the logical
        inline start margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `margin-top`, `margin-right`, `margin-bottom`, or
        `margin-left` property depending on the values defined for
        `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'margin-left'>`  **Initial value**: `0`.

    - WebkitMask (string | number; optional):
        The **`mask`** CSS shorthand property hides an element
        (partially or fully) by masking or clipping the image at
        specific points.  **Syntax**: `[ <mask-reference> ||
        <position> [ / <bg-size> ]? || <repeat-style> || [ <box> |
        border | padding | content | text ] || [ <box> | border |
        padding | content ] ]#`.

    - WebkitMaskAttachment (boolean | number | string | dict | list; optional):
        If a `mask-image` is specified, `-webkit-mask-attachment`
        determines whether the mask image's position is fixed within
        the viewport, or scrolls along with its containing block.
        **Syntax**: `<attachment>#`  **Initial value**: `scroll`.

    - WebkitMaskBoxImage (boolean | number | string | dict | list; optional):
        The **`mask-border`** CSS shorthand property lets you create a
        mask along the edge of an element's border.  **Syntax**:
        `<'mask-border-source'> || <'mask-border-slice'> [ /
        <'mask-border-width'>? [ / <'mask-border-outset'> ]? ]? ||
        <'mask-border-repeat'> || <'mask-border-mode'>`.

    - WebkitMaskBoxImageOutset (string | number; optional):
        The **`mask-border-outset`** CSS property specifies the
        distance by which an element's mask border is set out from its
        border box.  **Syntax**: `[ <length> | <number> ]{1,4}`
        **Initial value**: `0`.

    - WebkitMaskBoxImageRepeat (boolean | number | string | dict | list; optional):
        The **`mask-border-repeat`** CSS property sets how the edge
        regions of a source image are adjusted to fit the dimensions
        of an element's mask border.  **Syntax**: `[ stretch | repeat
        | round | space ]{1,2}`  **Initial value**: `stretch`.

    - WebkitMaskBoxImageSlice (boolean | number | string | dict | list; optional):
        The **`mask-border-slice`** CSS property divides the image set
        by `mask-border-source` into regions. These regions are used
        to form the components of an element's mask border.
        **Syntax**: `<number-percentage>{1,4} fill?`  **Initial
        value**: `0`.

    - WebkitMaskBoxImageSource (boolean | number | string | dict | list; optional):
        The **`mask-border-source`** CSS property sets the source
        image used to create an element's mask border.  **Syntax**:
        `none | <image>`  **Initial value**: `none`.

    - WebkitMaskBoxImageWidth (string | number; optional):
        The **`mask-border-width`** CSS property sets the width of an
        element's mask border.  **Syntax**: `[ <length-percentage> |
        <number> | auto ]{1,4}`  **Initial value**: `auto`.

    - WebkitMaskClip (boolean | number | string | dict | list; optional):
        The **`mask-clip`** CSS property determines the area which is
        affected by a mask. The painted content of an element must be
        restricted to this area.  **Syntax**: `[ <box> | border |
        padding | content | text ]#`  **Initial value**: `border`.

    - WebkitMaskComposite (boolean | number | string | dict | list; optional):
        The **`-webkit-mask-composite`** property specifies the manner
        in which multiple mask images applied to the same element are
        composited with one another. Mask images are composited in the
        opposite order that they are declared with the
        `-webkit-mask-image` property.  **Syntax**:
        `<composite-style>#`  **Initial value**: `source-over`.

    - WebkitMaskImage (boolean | number | string | dict | list; optional):
        The **`mask-image`** CSS property sets the image that is used
        as mask layer for an element. By default this means the alpha
        channel of the mask image will be multiplied with the alpha
        channel of the element. This can be controlled with the
        `mask-mode` property.  **Syntax**: `<mask-reference>#`
        **Initial value**: `none`.

    - WebkitMaskOrigin (boolean | number | string | dict | list; optional):
        The **`mask-origin`** CSS property sets the origin of a mask.
        **Syntax**: `[ <box> | border | padding | content ]#`
        **Initial value**: `padding`.

    - WebkitMaskPosition (string | number; optional):
        The **`mask-position`** CSS property sets the initial
        position, relative to the mask position layer set by
        `mask-origin`, for each defined mask image.  **Syntax**:
        `<position>#`  **Initial value**: `0% 0%`.

    - WebkitMaskPositionX (string | number; optional):
        The `-webkit-mask-position-x` CSS property sets the initial
        horizontal position of a mask image.  **Syntax**: `[
        <length-percentage> | left | center | right ]#`  **Initial
        value**: `0%`.

    - WebkitMaskPositionY (string | number; optional):
        The `-webkit-mask-position-y` CSS property sets the initial
        vertical position of a mask image.  **Syntax**: `[
        <length-percentage> | top | center | bottom ]#`  **Initial
        value**: `0%`.

    - WebkitMaskRepeat (boolean | number | string | dict | list; optional):
        The **`mask-repeat`** CSS property sets how mask images are
        repeated. A mask image can be repeated along the horizontal
        axis, the vertical axis, both axes, or not repeated at all.
        **Syntax**: `<repeat-style>#`  **Initial value**: `repeat`.

    - WebkitMaskRepeatX (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'no-repeat', 'repeat', 'round', 'space'; optional):
        The `-webkit-mask-repeat-x` property specifies whether and how
        a mask image is repeated (tiled) horizontally.  **Syntax**:
        `repeat | no-repeat | space | round`  **Initial value**:
        `repeat`.

    - WebkitMaskRepeatY (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'no-repeat', 'repeat', 'round', 'space'; optional):
        The `-webkit-mask-repeat-y` property sets whether and how a
        mask image is repeated (tiled) vertically.  **Syntax**:
        `repeat | no-repeat | space | round`  **Initial value**:
        `repeat`.

    - WebkitMaskSize (string | number; optional):
        The **`mask-size`** CSS property specifies the sizes of the
        mask images. The size of the image can be fully or partially
        constrained in order to preserve its intrinsic ratio.
        **Syntax**: `<bg-size>#`  **Initial value**: `auto auto`.

    - WebkitMaxInlineSize (string | number; optional):
        The **`max-inline-size`** CSS property defines the horizontal
        or vertical maximum size of an element's block, depending on
        its writing mode. It corresponds to either the `max-width` or
        the `max-height` property, depending on the value of
        `writing-mode`.  **Syntax**: `<'max-width'>`  **Initial
        value**: `none`.

    - WebkitOrder (boolean | number | string | dict | list; optional):
        The **`order`** CSS property sets the order to lay out an item
        in a flex or grid container. Items in a container are sorted
        by ascending `order` value and then by their source code
        order.  **Syntax**: `<integer>`  **Initial value**: `0`.

    - WebkitOverflowScrolling (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'touch'; optional):
        The `-webkit-overflow-scrolling` CSS property controls whether
        or not touch devices use momentum-based scrolling for a given
        element.  **Syntax**: `auto | touch`  **Initial value**:
        `auto`.

    - WebkitPaddingEnd (string | number; optional):
        The **`padding-inline-end`** CSS property defines the logical
        inline end padding of an element, which maps to a physical
        padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`.

    - WebkitPaddingStart (string | number; optional):
        The **`padding-inline-start`** CSS property defines the
        logical inline start padding of an element, which maps to a
        physical padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`.

    - WebkitPerspective (string | number; optional):
        The **`perspective`** CSS property determines the distance
        between the z=0 plane and the user in order to give a
        3D-positioned element some perspective.  **Syntax**: `none |
        <length>`  **Initial value**: `none`.

    - WebkitPerspectiveOrigin (string | number; optional):
        The **`perspective-origin`** CSS property determines the
        position at which the viewer is looking. It is used as the
        _vanishing point_ by the `perspective` property.  **Syntax**:
        `<position>`  **Initial value**: `50% 50%`.

    - WebkitPrintColorAdjust (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'economy', 'exact'; optional):
        The **`print-color-adjust`** CSS property sets what, if
        anything, the user agent may do to optimize the appearance of
        the element on the output device. By default, the browser is
        allowed to make any adjustments to the element's appearance it
        determines to be necessary and prudent given the type and
        capabilities of the output device.  **Syntax**: `economy |
        exact`  **Initial value**: `economy`.

    - WebkitRubyPosition (boolean | number | string | dict | list; optional):
        The **`ruby-position`** CSS property defines the position of a
        ruby element relatives to its base element. It can be
        positioned over the element (`over`), under it (`under`), or
        between the characters on their right side
        (`inter-character`).  **Syntax**: `[ alternate || [ over |
        under ] ] | inter-character`  **Initial value**: `alternate`.

    - WebkitScrollSnapType (boolean | number | string | dict | list; optional):
        The **`scroll-snap-type`** CSS property sets how strictly snap
        points are enforced on the scroll container in case there is
        one.  **Syntax**: `none | [ x | y | block | inline | both ] [
        mandatory | proximity ]?`  **Initial value**: `none`.

    - WebkitShapeMargin (string | number; optional):
        The **`shape-margin`** CSS property sets a margin for a CSS
        shape created using `shape-outside`.  **Syntax**:
        `<length-percentage>`  **Initial value**: `0`.

    - WebkitTapHighlightColor (boolean | number | string | dict | list; optional):
        **`-webkit-tap-highlight-color`** is a non-standard CSS
        property that sets the color of the highlight that appears
        over a link while it's being tapped. The highlighting
        indicates to the user that their tap is being successfully
        recognized, and indicates which element they're tapping on.
        **Syntax**: `<color>`  **Initial value**: `black`.

    - WebkitTextCombine (boolean | number | string | dict | list; optional):
        The **`text-combine-upright`** CSS property sets the
        combination of characters into the space of a single
        character. If the combined text is wider than 1em, the user
        agent must fit the contents within 1em. The resulting
        composition is treated as a single upright glyph for layout
        and decoration. This property only has an effect in vertical
        writing modes.  **Syntax**: `none | all | [ digits <integer>?
        ]`  **Initial value**: `none`.

    - WebkitTextDecorationColor (boolean | number | string | dict | list; optional):
        The **`text-decoration-color`** CSS property sets the color of
        decorations added to text by `text-decoration-line`.
        **Syntax**: `<color>`  **Initial value**: `currentcolor`.

    - WebkitTextDecorationLine (boolean | number | string | dict | list; optional):
        The **`text-decoration-line`** CSS property sets the kind of
        decoration that is used on text in an element, such as an
        underline or overline.  **Syntax**: `none | [ underline ||
        overline || line-through || blink ] | spelling-error |
        grammar-error`  **Initial value**: `none`.

    - WebkitTextDecorationSkip (boolean | number | string | dict | list; optional):
        The **`text-decoration-skip`** CSS property sets what parts of
        an element's content any text decoration affecting the element
        must skip over. It controls all text decoration lines drawn by
        the element and also any text decoration lines drawn by its
        ancestors.  **Syntax**: `none | [ objects || [ spaces | [
        leading-spaces || trailing-spaces ] ] || edges ||
        box-decoration ]`  **Initial value**: `objects`.

    - WebkitTextDecorationStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'dashed', 'dotted', 'double', 'solid', 'wavy'; optional):
        The **`text-decoration-style`** CSS property sets the style of
        the lines specified by `text-decoration-line`. The style
        applies to all lines that are set with `text-decoration-line`.
        **Syntax**: `solid | double | dotted | dashed | wavy`
        **Initial value**: `solid`.

    - WebkitTextEmphasis (boolean | number | string | dict | list; optional):
        The **`text-emphasis`** CSS property applies emphasis marks to
        text (except spaces and control characters). It is a shorthand
        for `text-emphasis-style` and `text-emphasis-color`.
        **Syntax**: `<'text-emphasis-style'> ||
        <'text-emphasis-color'>`.

    - WebkitTextEmphasisColor (boolean | number | string | dict | list; optional):
        The **`text-emphasis-color`** CSS property sets the color of
        emphasis marks. This value can also be set using the
        `text-emphasis` shorthand.  **Syntax**: `<color>`  **Initial
        value**: `currentcolor`.

    - WebkitTextEmphasisPosition (boolean | number | string | dict | list; optional):
        The **`text-emphasis-position`** CSS property sets where
        emphasis marks are drawn. Like ruby text, if there isn't
        enough room for emphasis marks, the line height is increased.
        **Syntax**: `[ over | under ] && [ right | left ]`  **Initial
        value**: `over right`.

    - WebkitTextEmphasisStyle (boolean | number | string | dict | list; optional):
        The **`text-emphasis-style`** CSS property sets the appearance
        of emphasis marks. It can also be set, and reset, using the
        `text-emphasis` shorthand.  **Syntax**: `none | [ [ filled |
        open ] || [ dot | circle | double-circle | triangle | sesame ]
        ] | <string>`  **Initial value**: `none`.

    - WebkitTextFillColor (boolean | number | string | dict | list; optional):
        The **`-webkit-text-fill-color`** CSS property specifies the
        fill color of characters of text. If this property is not set,
        the value of the `color` property is used.  **Syntax**:
        `<color>`  **Initial value**: `currentcolor`.

    - WebkitTextOrientation (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'mixed', 'sideways', 'upright'; optional):
        The **`text-orientation`** CSS property sets the orientation
        of the text characters in a line. It only affects text in
        vertical mode (when `writing-mode` is not `horizontal-tb`). It
        is useful for controlling the display of languages that use
        vertical script, and also for making vertical table headers.
        **Syntax**: `mixed | upright | sideways`  **Initial value**:
        `mixed`.

    - WebkitTextSizeAdjust (boolean | number | string | dict | list; optional):
        The **`text-size-adjust`** CSS property controls the text
        inflation algorithm used on some smartphones and tablets.
        Other browsers will ignore this property.  **Syntax**: `none |
        auto | <percentage>`  **Initial value**: `auto` for smartphone
        browsers supporting inflation, `none` in other cases (and then
        not modifiable).

    - WebkitTextStroke (string | number; optional):
        The **`-webkit-text-stroke`** CSS property specifies the width
        and color of strokes for text characters. This is a shorthand
        property for the longhand properties
        `-webkit-text-stroke-width` and `-webkit-text-stroke-color`.
        **Syntax**: `<length> || <color>`.

    - WebkitTextStrokeColor (boolean | number | string | dict | list; optional):
        The **`-webkit-text-stroke-color`** CSS property specifies the
        stroke color of characters of text. If this property is not
        set, the value of the `color` property is used.  **Syntax**:
        `<color>`  **Initial value**: `currentcolor`.

    - WebkitTextStrokeWidth (string | number; optional):
        The **`-webkit-text-stroke-width`** CSS property specifies the
        width of the stroke for text.  **Syntax**: `<length>`
        **Initial value**: `0`.

    - WebkitTextUnderlinePosition (boolean | number | string | dict | list; optional):
        The **`text-underline-position`** CSS property specifies the
        position of the underline which is set using the
        `text-decoration` property's `underline` value.  **Syntax**:
        `auto | from-font | [ under || [ left | right ] ]`  **Initial
        value**: `auto`.

    - WebkitTouchCallout (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'default'; optional):
        The `-webkit-touch-callout` CSS property controls the display
        of the default callout shown when you touch and hold a touch
        target.  **Syntax**: `default | none`  **Initial value**:
        `default`.

    - WebkitTransform (boolean | number | string | dict | list; optional):
        The **`transform`** CSS property lets you rotate, scale, skew,
        or translate an element. It modifies the coordinate space of
        the CSS visual formatting model.  **Syntax**: `none |
        <transform-list>`  **Initial value**: `none`.

    - WebkitTransformOrigin (string | number; optional):
        The **`transform-origin`** CSS property sets the origin for an
        element's transformations.  **Syntax**: `[ <length-percentage>
        | left | center | right | top | bottom ] | [ [
        <length-percentage> | left | center | right ] && [
        <length-percentage> | top | center | bottom ] ] <length>?`
        **Initial value**: `50% 50% 0`.

    - WebkitTransformStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'flat', 'preserve-3d'; optional):
        The **`transform-style`** CSS property sets whether children
        of an element are positioned in the 3D space or are flattened
        in the plane of the element.  **Syntax**: `flat | preserve-3d`
        **Initial value**: `flat`.

    - WebkitTransition (boolean | number | string | dict | list; optional):
        The **`transition`** CSS property is a shorthand property for
        `transition-property`, `transition-duration`,
        `transition-timing-function`, and `transition-delay`.
        **Syntax**: `<single-transition>#`.

    - WebkitTransitionDelay (boolean | number | string | dict | list; optional):
        The **`transition-delay`** CSS property specifies the duration
        to wait before starting a property's transition effect when
        its value changes.  **Syntax**: `<time>#`  **Initial value**:
        `0s`.

    - WebkitTransitionDuration (boolean | number | string | dict | list; optional):
        The **`transition-duration`** CSS property sets the length of
        time a transition animation should take to complete. By
        default, the value is `0s`, meaning that no animation will
        occur.  **Syntax**: `<time>#`  **Initial value**: `0s`.

    - WebkitTransitionProperty (boolean | number | string | dict | list; optional):
        The **`transition-property`** CSS property sets the CSS
        properties to which a transition effect should be applied.
        **Syntax**: `none | <single-transition-property>#`  **Initial
        value**: all.

    - WebkitTransitionTimingFunction (boolean | number | string | dict | list; optional):
        The **`transition-timing-function`** CSS property sets how
        intermediate values are calculated for CSS properties being
        affected by a transition effect.  **Syntax**:
        `<easing-function>#`  **Initial value**: `ease`.

    - WebkitUserModify (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'read-only', 'read-write', 'read-write-plaintext-only'; optional):
        **Syntax**: `read-only | read-write |
        read-write-plaintext-only`  **Initial value**: `read-only`.

    - WebkitUserSelect (a value equal to: 'text', 'inherit', 'none', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain', '-moz-none', 'element'; optional):
        The **`user-select`** CSS property controls whether the user
        can select text. This doesn't have any effect on content
        loaded as part of a browser's user interface (its chrome),
        except in textboxes.  **Syntax**: `auto | text | none |
        contain | all`  **Initial value**: `auto`.

    - WebkitWritingMode (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'horizontal-tb', 'sideways-lr', 'sideways-rl', 'vertical-lr', 'vertical-rl'; optional):
        The **`writing-mode`** CSS property sets whether lines of text
        are laid out horizontally or vertically, as well as the
        direction in which blocks progress. When set for an entire
        document, it should be set on the root element (`html` element
        for HTML documents).  **Syntax**: `horizontal-tb | vertical-rl
        | vertical-lr | sideways-rl | sideways-lr`  **Initial value**:
        `horizontal-tb`.

    - accentColor (boolean | number | string | dict | list; optional):
        The **`accent-color`** CSS property sets the accent color for
        user-interface controls generated by some elements.
        **Syntax**: `auto | <color>`  **Initial value**: `auto`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **93** | **92**  | **15.4** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/accent-color.

    - alignContent (boolean | number | string | dict | list; optional):
        The CSS **`align-content`** property sets the distribution of
        space between and around content items along a flexbox's
        cross-axis or a grid's block axis.  **Syntax**: `normal |
        <baseline-position> | <content-distribution> |
        <overflow-position>? <content-position>`  **Initial value**:
        `normal`  |  Chrome  | Firefox | Safari  |  Edge  |   IE   | |
        :------: | :-----: | :-----: | :----: | :----: | |  **29**  |
        **28**  |  **9**  | **12** | **11** | | 21 _-x-_ |         | 7
        _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/align-content.

    - alignItems (boolean | number | string | dict | list; optional):
        The CSS **`align-items`** property sets the `align-self` value
        on all direct children as a group. In Flexbox, it controls the
        alignment of items on the Cross Axis. In Grid Layout, it
        controls the alignment of items on the Block Axis within their
        grid area.  **Syntax**: `normal | stretch |
        <baseline-position> | [ <overflow-position>? <self-position>
        ]`  **Initial value**: `normal`  |  Chrome  | Firefox | Safari
        |  Edge  |   IE   | | :------: | :-----: | :-----: | :----: |
        :----: | |  **29**  | **20**  |  **9**  | **12** | **11** | |
        21 _-x-_ |         | 7 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/align-items.

    - alignSelf (boolean | number | string | dict | list; optional):
        The **`align-self`** CSS property overrides a grid or flex
        item's `align-items` value. In Grid, it aligns the item inside
        the grid area. In Flexbox, it aligns the item on the cross
        axis.  **Syntax**: `auto | normal | stretch |
        <baseline-position> | <overflow-position>? <self-position>`
        **Initial value**: `auto`  |  Chrome  | Firefox | Safari  |
        Edge  |   IE   | | :------: | :-----: | :-----: | :----: |
        :----: | |  **29**  | **20**  |  **9**  | **12** | **10** | |
        21 _-x-_ |         | 7 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/align-self.

    - alignTracks (boolean | number | string | dict | list; optional):
        The **`align-tracks`** CSS property sets the alignment in the
        masonry axis for grid containers that have masonry in their
        block axis.  **Syntax**: `[ normal | <baseline-position> |
        <content-distribution> | <overflow-position>?
        <content-position> ]#`  **Initial value**: `normal`  | Chrome
        | Firefox | Safari | Edge | IE  | | :----: | :-----: | :----:
        | :--: | :-: | |   No   |   n/a   |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/align-tracks.

    - alignmentBaseline (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'baseline', 'middle', 'after-edge', 'alphabetic', 'before-edge', 'central', 'hanging', 'ideographic', 'mathematical', 'text-after-edge', 'text-before-edge'; optional)

    - all (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`all`** shorthand CSS property resets all of an
        element's properties except `unicode-bidi`, `direction`, and
        CSS Custom Properties. It can set properties to their initial
        or inherited values, or to the values specified in another
        cascade layer or stylesheet origin.  **Syntax**: `initial |
        inherit | unset | revert | revert-layer`  **Initial value**:
        There is no practical initial value for it.  | Chrome |
        Firefox | Safari  | Edge | IE  | | :----: | :-----: | :-----:
        | :--: | :-: | | **37** | **27**  | **9.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/all.

    - animation (boolean | number | string | dict | list; optional):
        The **`animation`** shorthand CSS property applies an
        animation between styles. It is a shorthand for
        `animation-name`, `animation-duration`,
        `animation-timing-function`, `animation-delay`,
        `animation-iteration-count`, `animation-direction`,
        `animation-fill-mode`, and `animation-play-state`.
        **Syntax**: `<single-animation>#`  | Chrome  | Firefox |
        Safari  |  Edge  |   IE   | | :-----: | :-----: | :-----: |
        :----: | :----: | | **43**  | **16**  |  **9**  | **12** |
        **10** | | 3 _-x-_ | 5 _-x-_ | 4 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation.

    - animationComposition (boolean | number | string | dict | list; optional):
        The **`animation-composition`** CSS property specifies the
        composite operation to use when multiple animations affect the
        same property simultaneously.  **Syntax**:
        `<single-animation-composition>#`  **Initial value**:
        `replace`  | Chrome  | Firefox | Safari | Edge | IE  | |
        :-----: | :-----: | :----: | :--: | :-: | | **112** | **115**
        | **16** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-composition.

    - animationDelay (boolean | number | string | dict | list; optional):
        The **`animation-delay`** CSS property specifies the amount of
        time to wait from applying the animation to an element before
        beginning to perform the animation. The animation can start
        later, immediately from its beginning, or immediately and
        partway through the animation.  **Syntax**: `<time>#`
        **Initial value**: `0s`  | Chrome  | Firefox | Safari  |  Edge
        |   IE   | | :-----: | :-----: | :-----: | :----: | :----: | |
        **43**  | **16**  |  **9**  | **12** | **10** | | 3 _-x-_ | 5
        _-x-_ | 4 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-delay.

    - animationDirection (boolean | number | string | dict | list; optional):
        The **`animation-direction`** CSS property sets whether an
        animation should play forward, backward, or alternate back and
        forth between playing the sequence forward and backward.
        **Syntax**: `<single-animation-direction>#`  **Initial
        value**: `normal`  | Chrome  | Firefox | Safari  |  Edge  |
        IE   | | :-----: | :-----: | :-----: | :----: | :----: | |
        **43**  | **16**  |  **9**  | **12** | **10** | | 3 _-x-_ | 5
        _-x-_ | 4 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-direction.

    - animationDuration (boolean | number | string | dict | list; optional):
        The **`animation-duration`** CSS property sets the length of
        time that an animation takes to complete one cycle.
        **Syntax**: `<time>#`  **Initial value**: `0s`  | Chrome  |
        Firefox | Safari  |  Edge  |   IE   | | :-----: | :-----: |
        :-----: | :----: | :----: | | **43**  | **16**  |  **9**  |
        **12** | **10** | | 3 _-x-_ | 5 _-x-_ | 4 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-duration.

    - animationFillMode (boolean | number | string | dict | list; optional):
        The **`animation-fill-mode`** CSS property sets how a CSS
        animation applies styles to its target before and after its
        execution.  **Syntax**: `<single-animation-fill-mode>#`
        **Initial value**: `none`  | Chrome  | Firefox | Safari  |
        Edge  |   IE   | | :-----: | :-----: | :-----: | :----: |
        :----: | | **43**  | **16**  |  **9**  | **12** | **10** | | 3
        _-x-_ | 5 _-x-_ | 5 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-fill-mode.

    - animationIterationCount (boolean | number | string | dict | list; optional):
        The **`animation-iteration-count`** CSS property sets the
        number of times an animation sequence should be played before
        stopping.  **Syntax**: `<single-animation-iteration-count>#`
        **Initial value**: `1`  | Chrome  | Firefox | Safari  |  Edge
        |   IE   | | :-----: | :-----: | :-----: | :----: | :----: | |
        **43**  | **16**  |  **9**  | **12** | **10** | | 3 _-x-_ | 5
        _-x-_ | 4 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-iteration-count.

    - animationName (boolean | number | string | dict | list; optional):
        The **`animation-name`** CSS property specifies the names of
        one or more `@keyframes` at-rules that describe the animation
        to apply to an element. Multiple `@keyframe` at-rules are
        specified as a comma-separated list of names. If the specified
        name does not match any `@keyframe` at-rule, no properties are
        animated.  **Syntax**: `[ none | <keyframes-name> ]#`
        **Initial value**: `none`  | Chrome  | Firefox | Safari  |
        Edge  |   IE   | | :-----: | :-----: | :-----: | :----: |
        :----: | | **43**  | **16**  |  **9**  | **12** | **10** | | 3
        _-x-_ | 5 _-x-_ | 4 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-name.

    - animationPlayState (boolean | number | string | dict | list; optional):
        The **`animation-play-state`** CSS property sets whether an
        animation is running or paused.  **Syntax**:
        `<single-animation-play-state>#`  **Initial value**: `running`
        | Chrome  | Firefox | Safari  |  Edge  |   IE   | | :-----: |
        :-----: | :-----: | :----: | :----: | | **43**  | **16**  |
        **9**  | **12** | **10** | | 3 _-x-_ | 5 _-x-_ | 4 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-play-state.

    - animationRange (string | number; optional):
        The **`animation-range`** CSS shorthand property is used to
        set the start and end of an animation's attachment range along
        its timeline, i.e. where along the timeline an animation will
        start and end.  **Syntax**: `[ <'animation-range-start'>
        <'animation-range-end'>? ]#`  | Chrome  | Firefox | Safari |
        Edge | IE  | | :-----: | :-----: | :----: | :--: | :-: | |
        **115** |   No    |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-range.

    - animationRangeEnd (string | number; optional):
        The **`animation-range-end`** CSS property is used to set the
        end of an animation's attachment range along its timeline,
        i.e. where along the timeline an animation will end.
        **Syntax**: `[ normal | <length-percentage> |
        <timeline-range-name> <length-percentage>? ]#`  **Initial
        value**: `normal`  | Chrome  | Firefox | Safari | Edge | IE  |
        | :-----: | :-----: | :----: | :--: | :-: | | **115** |   No
        |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-range-end.

    - animationRangeStart (string | number; optional):
        The **`animation-range-start`** CSS property is used to set
        the start of an animation's attachment range along its
        timeline, i.e. where along the timeline an animation will
        start.  **Syntax**: `[ normal | <length-percentage> |
        <timeline-range-name> <length-percentage>? ]#`  **Initial
        value**: `normal`  | Chrome  | Firefox | Safari | Edge | IE  |
        | :-----: | :-----: | :----: | :--: | :-: | | **115** |   No
        |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-range-start.

    - animationTimeline (boolean | number | string | dict | list; optional):
        The **`animation-timeline`** CSS property specifies the
        timeline that is used to control the progress of an animation.
        **Syntax**: `<single-animation-timeline>#`  **Initial value**:
        `auto`  | Chrome  | Firefox | Safari | Edge | IE  | | :-----:
        | :-----: | :----: | :--: | :-: | | **115** |   n/a   |   No
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-timeline.

    - animationTimingFunction (boolean | number | string | dict | list; optional):
        The **`animation-timing-function`** CSS property sets how an
        animation progresses through the duration of each cycle.
        **Syntax**: `<easing-function>#`  **Initial value**: `ease`  |
        Chrome  | Firefox | Safari  |  Edge  |   IE   | | :-----: |
        :-----: | :-----: | :----: | :----: | | **43**  | **16**  |
        **9**  | **12** | **10** | | 3 _-x-_ | 5 _-x-_ | 4 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/animation-timing-function.

    - appearance (a value equal to: 'checkbox', 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'button', 'listbox', 'menulist', 'meter', 'progress-bar', 'push-button', 'radio', 'searchfield', 'slider-horizontal', 'square-button', 'textarea', 'menulist-button', 'textfield'; optional):
        The **`appearance`** CSS property is used to control native
        appearance of UI controls, that are based on operating
        system's theme.  **Syntax**: `none | auto | textfield |
        menulist-button | <compat-auto>`  **Initial value**: `none`  |
        Chrome  | Firefox |  Safari  |   Edge   | IE  | | :-----: |
        :-----: | :------: | :------: | :-: | | **84**  | **80**  |
        **15.4** |  **84**  | No  | | 1 _-x-_ | 1 _-x-_ | 3 _-x-_  |
        12 _-x-_ |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/appearance.

    - aspectRatio (boolean | number | string | dict | list; optional):
        The **`aspect-ratio`** CSS property sets a **preferred aspect
        ratio** for the box, which will be used in the calculation of
        auto sizes and some other layout functions.  **Syntax**: `auto
        | <ratio>`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | | **88** | **89**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/aspect-ratio.

    - azimuth (boolean | number | string | dict | list; optional):
        In combination with `elevation`, the **`azimuth`** CSS
        property enables different audio sources to be positioned
        spatially for aural presentation. This is important in that it
        provides a natural way to tell several voices apart, as each
        can be positioned to originate at a different location on the
        sound stage. Stereo output produce a lateral sound stage,
        while binaural headphones and multi-speaker setups allow for a
        fully three-dimensional stage.  **Syntax**: `<angle> | [ [
        left-side | far-left | left | center-left | center |
        center-right | right | far-right | right-side ] || behind ] |
        leftwards | rightwards`  **Initial value**: `center`
        @,deprecated.

    - backdropFilter (boolean | number | string | dict | list; optional):
        The **`backdrop-filter`** CSS property lets you apply
        graphical effects such as blurring or color shifting to the
        area behind an element. Because it applies to everything
        _behind_ the element, to see the effect you must make the
        element or its background at least partially transparent.
        **Syntax**: `none | <filter-function-list>`  **Initial
        value**: `none`  | Chrome | Firefox |   Safari    |  Edge  |
        IE  | | :----: | :-----: | :---------: | :----: | :-: | |
        **76** | **103** | **9** _-x-_ | **17** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/backdrop-filter.

    - backfaceVisibility (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible'; optional):
        The **`backface-visibility`** CSS property sets whether the
        back face of an element is visible when turned towards the
        user.  **Syntax**: `visible | hidden`  **Initial value**:
        `visible`  |  Chrome  | Firefox |  Safari   |  Edge  |   IE
        | | :------: | :-----: | :-------: | :----: | :----: | |
        **36**  | **16**  | **15.4**  | **12** | **10** | | 12 _-x-_ |
        | 5.1 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/backface-visibility.

    - background (string | number; optional):
        The **`background`** shorthand CSS property sets all
        background style properties at once, such as color, image,
        origin and size, or repeat method.  **Syntax**: `[ <bg-layer>
        , ]* <final-bg-layer>`  | Chrome | Firefox | Safari |  Edge  |
        IE   | | :----: | :-----: | :----: | :----: | :---: | | **1**
        |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background.

    - backgroundAttachment (boolean | number | string | dict | list; optional):
        The **`background-attachment`** CSS property sets whether a
        background image's position is fixed within the viewport, or
        scrolls with its containing block.  **Syntax**:
        `<attachment>#`  **Initial value**: `scroll`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-attachment.

    - backgroundBlendMode (boolean | number | string | dict | list; optional):
        The **`background-blend-mode`** CSS property sets how an
        element's background images should blend with each other and
        with the element's background color.  **Syntax**:
        `<blend-mode>#`  **Initial value**: `normal`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **35** | **30**  | **8**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-blend-mode.

    - backgroundClip (boolean | number | string | dict | list; optional):
        The **`background-clip`** CSS property sets whether an
        element's background extends underneath its border box,
        padding box, or content box.  **Syntax**: `<box>#`  **Initial
        value**: `border-box`  | Chrome | Firefox | Safari  |  Edge  |
        IE   | | :----: | :-----: | :-----: | :----: | :---: | | **1**
        |  **4**  |  **5**  | **12** | **9** | |        |         | 3
        _-x-_ |        |       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-clip.

    - backgroundColor (boolean | number | string | dict | list; optional):
        The **`background-color`** CSS property sets the background
        color of an element.  **Syntax**: `<color>`  **Initial
        value**: `transparent`  | Chrome | Firefox | Safari |  Edge  |
        IE   | | :----: | :-----: | :----: | :----: | :---: | | **1**
        |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-color.

    - backgroundImage (boolean | number | string | dict | list; optional):
        The **`background-image`** CSS property sets one or more
        background images on an element.  **Syntax**: `<bg-image>#`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |  IE   | | :----: | :-----: | :----: | :----: | :---: | |
        **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-image.

    - backgroundOrigin (boolean | number | string | dict | list; optional):
        The **`background-origin`** CSS property sets the background's
        origin: from the border start, inside the border, or inside
        the padding.  **Syntax**: `<box>#`  **Initial value**:
        `padding-box`  | Chrome | Firefox | Safari |  Edge  |  IE   |
        | :----: | :-----: | :----: | :----: | :---: | | **1**  |
        **4**  | **3**  | **12** | **9** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-origin.

    - backgroundPosition (string | number; optional):
        The **`background-position`** CSS property sets the initial
        position for each background image. The position is relative
        to the position layer set by `background-origin`.  **Syntax**:
        `<bg-position>#`  **Initial value**: `0% 0%`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-position.

    - backgroundPositionX (string | number; optional):
        The **`background-position-x`** CSS property sets the initial
        horizontal position for each background image. The position is
        relative to the position layer set by `background-origin`.
        **Syntax**: `[ center | [ [ left | right | x-start | x-end ]?
        <length-percentage>? ]! ]#`  **Initial value**: `0%`  | Chrome
        | Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  | **49**  | **1**  | **12**
        | **6** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-position-x.

    - backgroundPositionY (string | number; optional):
        The **`background-position-y`** CSS property sets the initial
        vertical position for each background image. The position is
        relative to the position layer set by `background-origin`.
        **Syntax**: `[ center | [ [ top | bottom | y-start | y-end ]?
        <length-percentage>? ]! ]#`  **Initial value**: `0%`  | Chrome
        | Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  | **49**  | **1**  | **12**
        | **6** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-position-y.

    - backgroundRepeat (boolean | number | string | dict | list; optional):
        The **`background-repeat`** CSS property sets how background
        images are repeated. A background image can be repeated along
        the horizontal and vertical axes, or not repeated at all.
        **Syntax**: `<repeat-style>#`  **Initial value**: `repeat`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-repeat.

    - backgroundSize (string | number; optional):
        The **`background-size`** CSS property sets the size of the
        element's background image. The image can be left to its
        natural size, stretched, or constrained to fit the available
        space.  **Syntax**: `<bg-size>#`  **Initial value**: `auto
        auto`  | Chrome  | Firefox | Safari  |  Edge  |  IE   | |
        :-----: | :-----: | :-----: | :----: | :---: | |  **3**  |
        **4**  |  **5**  | **12** | **9** | | 1 _-x-_ |         | 3
        _-x-_ |        |       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/background-size.

    - baselineShift (string | number; optional)

    - blockOverflow (boolean | number | string | dict | list; optional):
        **Syntax**: `clip | ellipsis | <string>`  **Initial value**:
        `clip`.

    - blockSize (string | number; optional):
        The **`block-size`** CSS property defines the horizontal or
        vertical size of an element's block, depending on its writing
        mode. It corresponds to either the `width` or the `height`
        property, depending on the value of `writing-mode`.
        **Syntax**: `<'width'>`  **Initial value**: `auto`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **57** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/block-size.

    - border (string | number; optional):
        The **`border`** shorthand CSS property sets an element's
        border. It sets the values of `border-width`, `border-style`,
        and `border-color`.  **Syntax**: `<line-width> || <line-style>
        || <color>`  | Chrome | Firefox | Safari |  Edge  |  IE   | |
        :----: | :-----: | :----: | :----: | :---: | | **1**  |  **1**
        | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border.

    - borderBlock (string | number; optional):
        The **`border-block`** CSS property is a shorthand property
        for setting the individual logical block border property
        values in a single place in the style sheet.  **Syntax**:
        `<'border-top-width'> || <'border-top-style'> || <color>`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block.

    - borderBlockColor (boolean | number | string | dict | list; optional):
        The **`border-block-color`** CSS property defines the color of
        the logical block borders of an element, which maps to a
        physical border color depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `border-top-color` and `border-bottom-color`, or
        `border-right-color` and `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>{1,2}`  **Initial value**: `currentcolor`
        | Chrome | Firefox |  Safari  | Edge | IE  | | :----: |
        :-----: | :------: | :--: | :-: | | **87** | **66**  |
        **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-color.

    - borderBlockEnd (string | number; optional):
        The **`border-block-end`** CSS property is a shorthand
        property for setting the individual logical block-end border
        property values in a single place in the style sheet.
        **Syntax**: `<'border-top-width'> || <'border-top-style'> ||
        <color>`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **69** | **41**
        | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-end.

    - borderBlockEndColor (boolean | number | string | dict | list; optional):
        The **`border-block-end-color`** CSS property defines the
        color of the logical block-end border of an element, which
        maps to a physical border color depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-color`, `border-right-color`,
        `border-bottom-color`, or `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>`  **Initial value**: `currentcolor`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-end-color.

    - borderBlockEndStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-block-end-style`** CSS property defines the
        style of the logical block-end border of an element, which
        maps to a physical border style depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-style`, `border-right-style`,
        `border-bottom-style`, or `border-left-style` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-end-style.

    - borderBlockEndWidth (string | number; optional):
        The **`border-block-end-width`** CSS property defines the
        width of the logical block-end border of an element, which
        maps to a physical border width depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-width`, `border-right-width`,
        `border-bottom-width`, or `border-left-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`  | Chrome
        | Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-end-width.

    - borderBlockStart (string | number; optional):
        The **`border-block-start`** CSS property is a shorthand
        property for setting the individual logical block-start border
        property values in a single place in the style sheet.
        **Syntax**: `<'border-top-width'> || <'border-top-style'> ||
        <color>`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **69** | **41**
        | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-start.

    - borderBlockStartColor (boolean | number | string | dict | list; optional):
        The **`border-block-start-color`** CSS property defines the
        color of the logical block-start border of an element, which
        maps to a physical border color depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-color`, `border-right-color`,
        `border-bottom-color`, or `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>`  **Initial value**: `currentcolor`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-start-color.

    - borderBlockStartStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-block-start-style`** CSS property defines the
        style of the logical block start border of an element, which
        maps to a physical border style depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-style`, `border-right-style`,
        `border-bottom-style`, or `border-left-style` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-start-style.

    - borderBlockStartWidth (string | number; optional):
        The **`border-block-start-width`** CSS property defines the
        width of the logical block-start border of an element, which
        maps to a physical border width depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-width`, `border-right-width`,
        `border-bottom-width`, or `border-left-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`  | Chrome
        | Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-start-width.

    - borderBlockStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-block-style`** CSS property defines the style of
        the logical block borders of an element, which maps to a
        physical border style depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `border-top-style` and `border-bottom-style`, or
        `border-left-style` and `border-right-style` properties
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-style.

    - borderBlockWidth (string | number; optional):
        The **`border-block-width`** CSS property defines the width of
        the logical block borders of an element, which maps to a
        physical border width depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `border-top-width` and `border-bottom-width`, or
        `border-left-width`, and `border-right-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`  | Chrome
        | Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-block-width.

    - borderBottom (string | number; optional):
        The **`border-bottom`** shorthand CSS property sets an
        element's bottom border. It sets the values of
        `border-bottom-width`, `border-bottom-style` and
        `border-bottom-color`.  **Syntax**: `<line-width> ||
        <line-style> || <color>`  | Chrome | Firefox | Safari |  Edge
        |  IE   | | :----: | :-----: | :----: | :----: | :---: | |
        **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-bottom.

    - borderBottomColor (boolean | number | string | dict | list; optional):
        The **`border-bottom-color`** CSS property sets the color of
        an element's bottom border. It can also be set with the
        shorthand CSS properties `border-color` or `border-bottom`.
        **Syntax**: `<'border-top-color'>`  **Initial value**:
        `currentcolor`  | Chrome | Firefox | Safari |  Edge  |  IE   |
        | :----: | :-----: | :----: | :----: | :---: | | **1**  |
        **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-bottom-color.

    - borderBottomLeftRadius (string | number; optional):
        The **`border-bottom-left-radius`** CSS property rounds the
        bottom-left corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`  | Chrome
        | Firefox | Safari  |  Edge  |  IE   | | :-----: | :-----: |
        :-----: | :----: | :---: | |  **4**  |  **4**  |  **5**  |
        **12** | **9** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-bottom-left-radius.

    - borderBottomRightRadius (string | number; optional):
        The **`border-bottom-right-radius`** CSS property rounds the
        bottom-right corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`  | Chrome
        | Firefox | Safari  |  Edge  |  IE   | | :-----: | :-----: |
        :-----: | :----: | :---: | |  **4**  |  **4**  |  **5**  |
        **12** | **9** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-bottom-right-radius.

    - borderBottomStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-bottom-style`** CSS property sets the line style
        of an element's bottom `border`.  **Syntax**: `<line-style>`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |   IE    | | :----: | :-----: | :----: | :----: | :-----: | |
        **1**  |  **1**  | **1**  | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-bottom-style.

    - borderBottomWidth (string | number; optional):
        The **`border-bottom-width`** CSS property sets the width of
        the bottom border of an element.  **Syntax**: `<line-width>`
        **Initial value**: `medium`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-bottom-width.

    - borderCollapse (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'collapse', 'separate'; optional):
        The **`border-collapse`** CSS property sets whether cells
        inside a `<table>` have shared or separate borders.
        **Syntax**: `collapse | separate`  **Initial value**:
        `separate`  | Chrome | Firefox | Safari  |  Edge  |  IE   | |
        :----: | :-----: | :-----: | :----: | :---: | | **1**  |
        **1**  | **1.2** | **12** | **5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-collapse.

    - borderColor (boolean | number | string | dict | list; optional):
        The **`border-color`** shorthand CSS property sets the color
        of an element's border.  **Syntax**: `<color>{1,4}`  | Chrome
        | Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-color.

    - borderEndEndRadius (string | number; optional):
        The **`border-end-end-radius`** CSS property defines a logical
        border radius on an element, which maps to a physical border
        radius that depends on the element's `writing-mode`,
        `direction`, and `text-orientation`. This is useful when
        building styles to work regardless of the text orientation and
        writing mode.  **Syntax**: `<length-percentage>{1,2}`
        **Initial value**: `0`  | Chrome | Firefox | Safari | Edge |
        IE  | | :----: | :-----: | :----: | :--: | :-: | | **89** |
        **66**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-end-end-radius.

    - borderEndStartRadius (string | number; optional):
        The **`border-end-start-radius`** CSS property defines a
        logical border radius on an element, which maps to a physical
        border radius depending on the element's `writing-mode`,
        `direction`, and `text-orientation`. This is useful when
        building styles to work regardless of the text orientation and
        writing mode.  **Syntax**: `<length-percentage>{1,2}`
        **Initial value**: `0`  | Chrome | Firefox | Safari | Edge |
        IE  | | :----: | :-----: | :----: | :--: | :-: | | **89** |
        **66**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-end-start-radius.

    - borderImage (boolean | number | string | dict | list; optional):
        The **`border-image`** CSS property draws an image around a
        given element. It replaces the element's regular border.
        **Syntax**: `<'border-image-source'> || <'border-image-slice'>
        [ / <'border-image-width'> | / <'border-image-width'>? /
        <'border-image-outset'> ]? || <'border-image-repeat'>`  |
        Chrome  |  Firefox  | Safari  |  Edge  |   IE   | | :-----: |
        :-------: | :-----: | :----: | :----: | | **16**  |  **15**
        |  **6**  | **12** | **11** | | 7 _-x-_ | 3.5 _-x-_ | 3 _-x-_
        |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-image.

    - borderImageOutset (string | number; optional):
        The **`border-image-outset`** CSS property sets the distance
        by which an element's border image is set out from its border
        box.  **Syntax**: `[ <length> | <number> ]{1,4}`  **Initial
        value**: `0`  | Chrome | Firefox | Safari |  Edge  |   IE   |
        | :----: | :-----: | :----: | :----: | :----: | | **15** |
        **15**  | **6**  | **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-image-outset.

    - borderImageRepeat (boolean | number | string | dict | list; optional):
        The **`border-image-repeat`** CSS property defines how the
        edge regions and middle region of a source image are adjusted
        to fit the dimensions of an element's border image. The middle
        region can be displayed by using the keyword \"fill\" in the
        border-image-slice property.  **Syntax**: `[ stretch | repeat
        | round | space ]{1,2}`  **Initial value**: `stretch`  |
        Chrome | Firefox | Safari |  Edge  |   IE   | | :----: |
        :-----: | :----: | :----: | :----: | | **15** | **15**  |
        **6**  | **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-image-repeat.

    - borderImageSlice (boolean | number | string | dict | list; optional):
        The **`border-image-slice`** CSS property divides the image
        specified by `border-image-source` into regions. These regions
        form the components of an element's border image.  **Syntax**:
        `<number-percentage>{1,4} && fill?`  **Initial value**: `100%`
        | Chrome | Firefox | Safari |  Edge  |   IE   | | :----: |
        :-----: | :----: | :----: | :----: | | **15** | **15**  |
        **6**  | **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-image-slice.

    - borderImageSource (boolean | number | string | dict | list; optional):
        The **`border-image-source`** CSS property sets the source
        image used to create an element's border image.  **Syntax**:
        `none | <image>`  **Initial value**: `none`  | Chrome |
        Firefox | Safari |  Edge  |   IE   | | :----: | :-----: |
        :----: | :----: | :----: | | **15** | **15**  | **6**  |
        **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-image-source.

    - borderImageWidth (string | number; optional):
        The **`border-image-width`** CSS property sets the width of an
        element's border image.  **Syntax**: `[ <length-percentage> |
        <number> | auto ]{1,4}`  **Initial value**: `1`  | Chrome |
        Firefox | Safari |  Edge  |   IE   | | :----: | :-----: |
        :----: | :----: | :----: | | **15** | **13**  | **6**  |
        **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-image-width.

    - borderInline (string | number; optional):
        The **`border-inline`** CSS property is a shorthand property
        for setting the individual logical inline border property
        values in a single place in the style sheet.  **Syntax**:
        `<'border-top-width'> || <'border-top-style'> || <color>`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline.

    - borderInlineColor (boolean | number | string | dict | list; optional):
        The **`border-inline-color`** CSS property defines the color
        of the logical inline borders of an element, which maps to a
        physical border color depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `border-top-color` and `border-bottom-color`, or
        `border-right-color` and `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>{1,2}`  **Initial value**: `currentcolor`
        | Chrome | Firefox |  Safari  | Edge | IE  | | :----: |
        :-----: | :------: | :--: | :-: | | **87** | **66**  |
        **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-color.

    - borderInlineEnd (string | number; optional):
        The **`border-inline-end`** CSS property is a shorthand
        property for setting the individual logical inline-end border
        property values in a single place in the style sheet.
        **Syntax**: `<'border-top-width'> || <'border-top-style'> ||
        <color>`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **69** | **41**
        | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-end.

    - borderInlineEndColor (boolean | number | string | dict | list; optional):
        The **`border-inline-end-color`** CSS property defines the
        color of the logical inline-end border of an element, which
        maps to a physical border color depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-color`, `border-right-color`,
        `border-bottom-color`, or `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>`  **Initial value**: `currentcolor`  |
        Chrome |           Firefox           |  Safari  | Edge | IE  |
        | :----: | :-------------------------: | :------: | :--: | :-:
        | | **69** |           **41**            | **12.1** | n/a  |
        No  | |        | 3 _(-moz-border-end-color)_ |          |
        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-end-color.

    - borderInlineEndStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-inline-end-style`** CSS property defines the
        style of the logical inline end border of an element, which
        maps to a physical border style depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-style`, `border-right-style`,
        `border-bottom-style`, or `border-left-style` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`  | Chrome |
        Firefox           |  Safari  | Edge | IE  | | :----: |
        :-------------------------: | :------: | :--: | :-: | | **69**
        |           **41**            | **12.1** | n/a  | No  | |
        | 3 _(-moz-border-end-style)_ |          |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-end-style.

    - borderInlineEndWidth (string | number; optional):
        The **`border-inline-end-width`** CSS property defines the
        width of the logical inline-end border of an element, which
        maps to a physical border width depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-width`, `border-right-width`,
        `border-bottom-width`, or `border-left-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`  | Chrome
        |           Firefox           |  Safari  | Edge | IE  | |
        :----: | :-------------------------: | :------: | :--: | :-: |
        | **69** |           **41**            | **12.1** | n/a  | No
        | |        | 3 _(-moz-border-end-width)_ |          |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-end-width.

    - borderInlineStart (string | number; optional):
        The **`border-inline-start`** CSS property is a shorthand
        property for setting the individual logical inline-start
        border property values in a single place in the style sheet.
        **Syntax**: `<'border-top-width'> || <'border-top-style'> ||
        <color>`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **69** | **41**
        | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-start.

    - borderInlineStartColor (boolean | number | string | dict | list; optional):
        The **`border-inline-start-color`** CSS property defines the
        color of the logical inline start border of an element, which
        maps to a physical border color depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-color`, `border-right-color`,
        `border-bottom-color`, or `border-left-color` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-color'>`  **Initial value**: `currentcolor`  |
        Chrome |            Firefox            |  Safari  | Edge | IE
        | | :----: | :---------------------------: | :------: | :--: |
        :-: | | **69** |            **41**             | **12.1** |
        n/a  | No  | |        | 3 _(-moz-border-start-color)_ |
        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-start-color.

    - borderInlineStartStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-inline-start-style`** CSS property defines the
        style of the logical inline start border of an element, which
        maps to a physical border style depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-style`, `border-right-style`,
        `border-bottom-style`, or `border-left-style` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`  | Chrome |
        Firefox            |  Safari  | Edge | IE  | | :----: |
        :---------------------------: | :------: | :--: | :-: | |
        **69** |            **41**             | **12.1** | n/a  | No
        | |        | 3 _(-moz-border-start-style)_ |          |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-start-style.

    - borderInlineStartWidth (string | number; optional):
        The **`border-inline-start-width`** CSS property defines the
        width of the logical inline-start border of an element, which
        maps to a physical border width depending on the element's
        writing mode, directionality, and text orientation. It
        corresponds to the `border-top-width`, `border-right-width`,
        `border-bottom-width`, or `border-left-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`  | Chrome
        | Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **69** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-start-width.

    - borderInlineStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-inline-style`** CSS property defines the style
        of the logical inline borders of an element, which maps to a
        physical border style depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `border-top-style` and `border-bottom-style`, or
        `border-left-style` and `border-right-style` properties
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-style'>`  **Initial value**: `none`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-style.

    - borderInlineWidth (string | number; optional):
        The **`border-inline-width`** CSS property defines the width
        of the logical inline borders of an element, which maps to a
        physical border width depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `border-top-width` and `border-bottom-width`, or
        `border-left-width`, and `border-right-width` property
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'border-top-width'>`  **Initial value**: `medium`  | Chrome
        | Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-inline-width.

    - borderLeft (string | number; optional):
        The **`border-left`** shorthand CSS property sets all the
        properties of an element's left border.  **Syntax**:
        `<line-width> || <line-style> || <color>`  | Chrome | Firefox
        | Safari |  Edge  |  IE   | | :----: | :-----: | :----: |
        :----: | :---: | | **1**  |  **1**  | **1**  | **12** | **4**
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-left.

    - borderLeftColor (boolean | number | string | dict | list; optional):
        The **`border-left-color`** CSS property sets the color of an
        element's left border. It can also be set with the shorthand
        CSS properties `border-color` or `border-left`.  **Syntax**:
        `<color>`  **Initial value**: `currentcolor`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-left-color.

    - borderLeftStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-left-style`** CSS property sets the line style
        of an element's left `border`.  **Syntax**: `<line-style>`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |   IE    | | :----: | :-----: | :----: | :----: | :-----: | |
        **1**  |  **1**  | **1**  | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-left-style.

    - borderLeftWidth (string | number; optional):
        The **`border-left-width`** CSS property sets the width of the
        left border of an element.  **Syntax**: `<line-width>`
        **Initial value**: `medium`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-left-width.

    - borderRadius (string | number; optional):
        The **`border-radius`** CSS property rounds the corners of an
        element's outer border edge. You can set a single radius to
        make circular corners, or two radii to make elliptical
        corners.  **Syntax**: `<length-percentage>{1,4} [ /
        <length-percentage>{1,4} ]?`  | Chrome  | Firefox | Safari  |
        Edge  |  IE   | | :-----: | :-----: | :-----: | :----: | :---:
        | |  **4**  |  **4**  |  **5**  | **12** | **9** | | 1 _-x-_ |
        | 3 _-x-_ |        |       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-radius.

    - borderRight (string | number; optional):
        The **`border-right`** shorthand CSS property sets all the
        properties of an element's right border.  **Syntax**:
        `<line-width> || <line-style> || <color>`  | Chrome | Firefox
        | Safari |  Edge  |   IE    | | :----: | :-----: | :----: |
        :----: | :-----: | | **1**  |  **1**  | **1**  | **12** |
        **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-right.

    - borderRightColor (boolean | number | string | dict | list; optional):
        The **`border-right-color`** CSS property sets the color of an
        element's right border. It can also be set with the shorthand
        CSS properties `border-color` or `border-right`.  **Syntax**:
        `<color>`  **Initial value**: `currentcolor`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-right-color.

    - borderRightStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-right-style`** CSS property sets the line style
        of an element's right `border`.  **Syntax**: `<line-style>`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |   IE    | | :----: | :-----: | :----: | :----: | :-----: | |
        **1**  |  **1**  | **1**  | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-right-style.

    - borderRightWidth (string | number; optional):
        The **`border-right-width`** CSS property sets the width of
        the right border of an element.  **Syntax**: `<line-width>`
        **Initial value**: `medium`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-right-width.

    - borderSpacing (string | number; optional):
        The **`border-spacing`** CSS property sets the distance
        between the borders of adjacent cells in a `<table>`. This
        property applies only when `border-collapse` is `separate`.
        **Syntax**: `<length> <length>?`  **Initial value**: `0`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-spacing.

    - borderStartEndRadius (string | number; optional):
        The **`border-start-end-radius`** CSS property defines a
        logical border radius on an element, which maps to a physical
        border radius depending on the element's `writing-mode`,
        `direction`, and `text-orientation`. This is useful when
        building styles to work regardless of the text orientation and
        writing mode.  **Syntax**: `<length-percentage>{1,2}`
        **Initial value**: `0`  | Chrome | Firefox | Safari | Edge |
        IE  | | :----: | :-----: | :----: | :--: | :-: | | **89** |
        **66**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-start-end-radius.

    - borderStartStartRadius (string | number; optional):
        The **`border-start-start-radius`** CSS property defines a
        logical border radius on an element, which maps to a physical
        border radius that depends on the element's `writing-mode`,
        `direction`, and `text-orientation`. This is useful when
        building styles to work regardless of the text orientation and
        writing mode.  **Syntax**: `<length-percentage>{1,2}`
        **Initial value**: `0`  | Chrome | Firefox | Safari | Edge |
        IE  | | :----: | :-----: | :----: | :--: | :-: | | **89** |
        **66**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-start-start-radius.

    - borderStyle (boolean | number | string | dict | list; optional):
        The **`border-style`** shorthand CSS property sets the line
        style for all four sides of an element's border.  **Syntax**:
        `<line-style>{1,4}`  | Chrome | Firefox | Safari |  Edge  |
        IE   | | :----: | :-----: | :----: | :----: | :---: | | **1**
        |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-style.

    - borderTop (string | number; optional):
        The **`border-top`** shorthand CSS property sets all the
        properties of an element's top border.  **Syntax**:
        `<line-width> || <line-style> || <color>`  | Chrome | Firefox
        | Safari |  Edge  |  IE   | | :----: | :-----: | :----: |
        :----: | :---: | | **1**  |  **1**  | **1**  | **12** | **4**
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-top.

    - borderTopColor (boolean | number | string | dict | list; optional):
        The **`border-top-color`** CSS property sets the color of an
        element's top border. It can also be set with the shorthand
        CSS properties `border-color` or `border-top`.  **Syntax**:
        `<color>`  **Initial value**: `currentcolor`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-top-color.

    - borderTopLeftRadius (string | number; optional):
        The **`border-top-left-radius`** CSS property rounds the
        top-left corner of an element by specifying the radius (or the
        radius of the semi-major and semi-minor axes) of the ellipse
        defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`  | Chrome
        | Firefox | Safari  |  Edge  |  IE   | | :-----: | :-----: |
        :-----: | :----: | :---: | |  **4**  |  **4**  |  **5**  |
        **12** | **9** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-top-left-radius.

    - borderTopRightRadius (string | number; optional):
        The **`border-top-right-radius`** CSS property rounds the
        top-right corner of an element by specifying the radius (or
        the radius of the semi-major and semi-minor axes) of the
        ellipse defining the curvature of the corner.  **Syntax**:
        `<length-percentage>{1,2}`  **Initial value**: `0`  | Chrome
        | Firefox | Safari  |  Edge  |  IE   | | :-----: | :-----: |
        :-----: | :----: | :---: | |  **4**  |  **4**  |  **5**  |
        **12** | **9** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-top-right-radius.

    - borderTopStyle (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'dashed', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid'; optional):
        The **`border-top-style`** CSS property sets the line style of
        an element's top `border`.  **Syntax**: `<line-style>`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |   IE    | | :----: | :-----: | :----: | :----: | :-----: | |
        **1**  |  **1**  | **1**  | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-top-style.

    - borderTopWidth (string | number; optional):
        The **`border-top-width`** CSS property sets the width of the
        top border of an element.  **Syntax**: `<line-width>`
        **Initial value**: `medium`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-top-width.

    - borderWidth (string | number; optional):
        The **`border-width`** shorthand CSS property sets the width
        of an element's border.  **Syntax**: `<line-width>{1,4}`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/border-width.

    - bottom (string | number; optional):
        The **`bottom`** CSS property participates in setting the
        vertical position of a positioned element. It has no effect on
        non-positioned elements.  **Syntax**: `<length> | <percentage>
        | auto`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/bottom.

    - boxAlign (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'stretch', 'center', 'end', 'start', 'baseline'; optional):
        The **`box-align`** CSS property specifies how an element
        aligns its contents across its layout in a perpendicular
        direction. The effect of the property is only visible if there
        is extra space in the box.  **Syntax**: `start | center | end
        | baseline | stretch`  **Initial value**: `stretch`
        @,deprecated.

    - boxDecorationBreak (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'clone', 'slice'; optional):
        The **`box-decoration-break`** CSS property specifies how an
        element's fragments should be rendered when broken across
        multiple lines, columns, or pages.  **Syntax**: `slice |
        clone`  **Initial value**: `slice`  |    Chrome    | Firefox |
        Safari    | Edge | IE  | | :----------: | :-----: |
        :---------: | :--: | :-: | | **22** _-x-_ | **32**  | **7**
        _-x-_ | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/box-decoration-break.

    - boxDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'reverse'; optional):
        The **`box-direction`** CSS property specifies whether a box
        lays out its contents normally (from the top or left edge), or
        in reverse (from the bottom or right edge).  **Syntax**:
        `normal | reverse | inherit`  **Initial value**: `normal`
        @,deprecated.

    - boxFlex (boolean | number | string | dict | list; optional):
        The **`-moz-box-flex`** and **`-webkit-box-flex`** CSS
        properties specify how a `-moz-box` or `-webkit-box` grows to
        fill the box that contains it, in the direction of the
        containing box's layout.  **Syntax**: `<number>`  **Initial
        value**: `0` @,deprecated.

    - boxFlexGroup (boolean | number | string | dict | list; optional):
        The **`box-flex-group`** CSS property assigns the flexbox's
        child elements to a flex group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - boxLines (a value equal to: 'inherit', 'single', 'multiple', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`box-lines`** CSS property determines whether the box
        may have a single or multiple lines (rows for horizontally
        oriented boxes, columns for vertically oriented boxes).
        **Syntax**: `single | multiple`  **Initial value**: `single`
        @,deprecated.

    - boxOrdinalGroup (boolean | number | string | dict | list; optional):
        The **`box-ordinal-group`** CSS property assigns the flexbox's
        child elements to an ordinal group.  **Syntax**: `<integer>`
        **Initial value**: `1` @,deprecated.

    - boxOrient (a value equal to: 'vertical', 'horizontal', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'block-axis', 'inline-axis'; optional):
        The **`box-orient`** CSS property sets whether an element lays
        out its contents horizontally or vertically.  **Syntax**:
        `horizontal | vertical | inline-axis | block-axis | inherit`
        **Initial value**: `inline-axis` (`horizontal` in XUL)
        @,deprecated.

    - boxPack (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'justify'; optional):
        The **`-moz-box-pack`** and **`-webkit-box-pack`** CSS
        properties specify how a `-moz-box` or `-webkit-box` packs its
        contents in the direction of its layout. The effect of this is
        only visible if there is extra space in the box.  **Syntax**:
        `start | center | end | justify`  **Initial value**: `start`
        @,deprecated.

    - boxShadow (boolean | number | string | dict | list; optional):
        The **`box-shadow`** CSS property adds shadow effects around
        an element's frame. You can set multiple effects separated by
        commas. A box shadow is described by X and Y offsets relative
        to the element, blur and spread radius, and color.
        **Syntax**: `none | <shadow>#`  **Initial value**: `none`  |
        Chrome  | Firefox | Safari  |  Edge  |  IE   | | :-----: |
        :-----: | :-----: | :----: | :---: | | **10**  |  **4**  |
        **5.1** | **12** | **9** | | 1 _-x-_ |         | 3 _-x-_ |
        |       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/box-shadow.

    - boxSizing (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'border-box', 'content-box'; optional):
        The **`box-sizing`** CSS property sets how the total width and
        height of an element is calculated.  **Syntax**: `content-box
        | border-box`  **Initial value**: `content-box`  | Chrome  |
        Firefox | Safari  |  Edge  |  IE   | | :-----: | :-----: |
        :-----: | :----: | :---: | | **10**  | **29**  | **5.1** |
        **12** | **8** | | 1 _-x-_ | 1 _-x-_ | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/box-sizing.

    - breakAfter (a value equal to: 'inherit', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'left', 'right', 'always', 'avoid', 'avoid-column', 'avoid-page', 'avoid-region', 'column', 'page', 'recto', 'region', 'verso'; optional):
        The **`break-after`** CSS property sets how page, column, or
        region breaks should behave after a generated box. If there is
        no generated box, the property is ignored.  **Syntax**: `auto
        | avoid | always | all | avoid-page | page | left | right |
        recto | verso | avoid-column | column | avoid-region | region`
        **Initial value**: `auto`  | Chrome | Firefox | Safari |  Edge
        |   IE   | | :----: | :-----: | :----: | :----: | :----: | |
        **50** | **65**  | **10** | **12** | **10** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/break-after.

    - breakBefore (a value equal to: 'inherit', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'left', 'right', 'always', 'avoid', 'avoid-column', 'avoid-page', 'avoid-region', 'column', 'page', 'recto', 'region', 'verso'; optional):
        The **`break-before`** CSS property sets how page, column, or
        region breaks should behave before a generated box. If there
        is no generated box, the property is ignored.  **Syntax**:
        `auto | avoid | always | all | avoid-page | page | left |
        right | recto | verso | avoid-column | column | avoid-region |
        region`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari |  Edge  |   IE   | | :----: | :-----: | :----: |
        :----: | :----: | | **50** | **65**  | **10** | **12** |
        **10** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/break-before.

    - breakInside (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'avoid', 'avoid-column', 'avoid-page', 'avoid-region'; optional):
        The **`break-inside`** CSS property sets how page, column, or
        region breaks should behave inside a generated box. If there
        is no generated box, the property is ignored.  **Syntax**:
        `auto | avoid | avoid-page | avoid-column | avoid-region`
        **Initial value**: `auto`  | Chrome | Firefox | Safari |  Edge
        |   IE   | | :----: | :-----: | :----: | :----: | :----: | |
        **50** | **65**  | **10** | **12** | **10** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/break-inside.

    - captionSide (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'bottom', 'top', 'block-end', 'block-start', 'inline-end', 'inline-start'; optional):
        The **`caption-side`** CSS property puts the content of a
        table's `<caption>` on the specified side. The values are
        relative to the `writing-mode` of the table.  **Syntax**: `top
        | bottom | block-start | block-end | inline-start |
        inline-end`  **Initial value**: `top`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/caption-side.

    - caret (boolean | number | string | dict | list; optional):
        **Syntax**: `<'caret-color'> || <'caret-shape'>`.

    - caretColor (boolean | number | string | dict | list; optional):
        The **`caret-color`** CSS property sets the color of the
        **insertion caret**, the visible marker where the next
        character typed will be inserted. This is sometimes referred
        to as the **text input cursor**. The caret appears in elements
        such as `<input>` or those with the `contenteditable`
        attribute. The caret is typically a thin vertical line that
        flashes to help make it more noticeable. By default, it is
        black, but its color can be altered with this property.
        **Syntax**: `auto | <color>`  **Initial value**: `auto`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **57** | **53**  | **11.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/caret-color.

    - caretShape (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'bar', 'block', 'underscore'; optional):
        **Syntax**: `auto | bar | block | underscore`  **Initial
        value**: `auto`.

    - clear (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'both', 'left', 'right', 'inline-end', 'inline-start'; optional):
        The **`clear`** CSS property sets whether an element must be
        moved below (cleared) floating elements that precede it. The
        `clear` property applies to floating and non-floating
        elements.  **Syntax**: `none | left | right | both |
        inline-start | inline-end`  **Initial value**: `none`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/clear.

    - clip (boolean | number | string | dict | list; optional):
        The **`clip`** CSS property defines a visible portion of an
        element. The `clip` property applies only to absolutely
        positioned elements — that is, elements with
        `position:absolute` or `position:fixed`.  **Syntax**: `<shape>
        | auto`  **Initial value**: `auto` @,deprecated.

    - clipPath (boolean | number | string | dict | list; optional):
        The **`clip-path`** CSS property creates a clipping region
        that sets what part of an element should be shown. Parts that
        are inside the region are shown, while those outside are
        hidden.  **Syntax**: `<clip-source> | [ <basic-shape> ||
        <geometry-box> ] | none`  **Initial value**: `none`  |  Chrome
        | Firefox | Safari  |  Edge  |   IE   | | :------: | :-----: |
        :-----: | :----: | :----: | |  **55**  | **3.5** | **9.1** |
        **79** | **10** | | 23 _-x-_ |         | 7 _-x-_ |        |
        | @,see,https,://developer.mozilla.org/docs/Web/CSS/clip-path.

    - clipRule (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'evenodd', 'nonzero'; optional)

    - color (boolean | number | string | dict | list; optional):
        The **`color`** CSS property sets the foreground color value
        of an element's text and text decorations, and sets the
        `currentcolor` value. `currentcolor` may be used as an
        indirect value on _other_ properties and is the default for
        other color properties, such as `border-color`.  **Syntax**:
        `<color>`  **Initial value**: `canvastext`  | Chrome | Firefox
        | Safari |  Edge  |  IE   | | :----: | :-----: | :----: |
        :----: | :---: | | **1**  |  **1**  | **1**  | **12** | **3**
        | @,see,https,://developer.mozilla.org/docs/Web/CSS/color.

    - colorAdjust (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'economy', 'exact'; optional):
        The **`print-color-adjust`** CSS property sets what, if
        anything, the user agent may do to optimize the appearance of
        the element on the output device. By default, the browser is
        allowed to make any adjustments to the element's appearance it
        determines to be necessary and prudent given the type and
        capabilities of the output device.  **Syntax**: `economy |
        exact`  **Initial value**: `economy`  |    Chrome    |
        Firefox       |  Safari  |     Edge     | IE  | | :----------:
        | :-----------------: | :------: | :----------: | :-: | |
        **17** _-x-_ |       **97**        | **15.4** | **79** _-x-_ |
        No  | |              | 48 _(color-adjust)_ | 6 _-x-_  |
        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/print-color-adjust.

    - colorInterpolation (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'linearRGB', 'sRGB'; optional)

    - colorRendering (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'optimizeSpeed', 'optimizeQuality'; optional)

    - colorScheme (boolean | number | string | dict | list; optional):
        The **`color-scheme`** CSS property allows an element to
        indicate which color schemes it can comfortably be rendered
        in.  **Syntax**: `normal | [ light | dark | <custom-ident> ]+
        && only?`  **Initial value**: `normal`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | | **81** | **96**  | **13** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/color-scheme.

    - columnCount (boolean | number | string | dict | list; optional):
        The **`column-count`** CSS property breaks an element's
        content into the specified number of columns.  **Syntax**:
        `<integer> | auto`  **Initial value**: `auto`  | Chrome  |
        Firefox | Safari  |  Edge  |   IE   | | :-----: | :-----: |
        :-----: | :----: | :----: | | **50**  | **52**  |  **9**  |
        **12** | **10** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-count.

    - columnFill (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'balance', 'balance-all'; optional):
        The **`column-fill`** CSS property controls how an element's
        contents are balanced when broken into columns.  **Syntax**:
        `auto | balance | balance-all`  **Initial value**: `balance`
        | Chrome | Firefox | Safari  |  Edge  |   IE   | | :----: |
        :-----: | :-----: | :----: | :----: | | **50** | **52**  |
        **9**  | **12** | **10** | |        |         | 8 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-fill.

    - columnGap (string | number; optional):
        The **`column-gap`** CSS property sets the size of the gap
        (gutter) between an element's columns.  **Syntax**: `normal |
        <length-percentage>`  **Initial value**: `normal`  | Chrome |
        Firefox | Safari |  Edge  |   IE   | | :----: | :-----: |
        :----: | :----: | :----: | | **1**  | **1.5** | **3**  |
        **12** | **10** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-gap.

    - columnRule (string | number; optional):
        The **`column-rule`** shorthand CSS property sets the width,
        style, and color of the line drawn between columns in a
        multi-column layout.  **Syntax**: `<'column-rule-width'> ||
        <'column-rule-style'> || <'column-rule-color'>`  | Chrome  |
        Firefox | Safari  |  Edge  |   IE   | | :-----: | :-----: |
        :-----: | :----: | :----: | | **50**  | **52**  |  **9**  |
        **12** | **10** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-rule.

    - columnRuleColor (boolean | number | string | dict | list; optional):
        The **`column-rule-color`** CSS property sets the color of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<color>`  **Initial value**: `currentcolor`  |
        Chrome  | Firefox | Safari  |  Edge  |   IE   | | :-----: |
        :-----: | :-----: | :----: | :----: | | **50**  | **52**  |
        **9**  | **12** | **10** | | 1 _-x-_ |         | 3 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-rule-color.

    - columnRuleStyle (boolean | number | string | dict | list; optional):
        The **`column-rule-style`** CSS property sets the style of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<'border-style'>`  **Initial value**: `none`  |
        Chrome  | Firefox | Safari  |  Edge  |   IE   | | :-----: |
        :-----: | :-----: | :----: | :----: | | **50**  | **52**  |
        **9**  | **12** | **10** | | 1 _-x-_ |         | 3 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-rule-style.

    - columnRuleWidth (string | number; optional):
        The **`column-rule-width`** CSS property sets the width of the
        line drawn between columns in a multi-column layout.
        **Syntax**: `<'border-width'>`  **Initial value**: `medium`  |
        Chrome  | Firefox | Safari  |  Edge  |   IE   | | :-----: |
        :-----: | :-----: | :----: | :----: | | **50**  | **52**  |
        **9**  | **12** | **10** | | 1 _-x-_ |         | 3 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-rule-width.

    - columnSpan (a value equal to: 'inherit', 'none', 'all', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`column-span`** CSS property makes it possible for an
        element to span across all columns when its value is set to
        `all`.  **Syntax**: `none | all`  **Initial value**: `none`  |
        Chrome  | Firefox |  Safari   |  Edge  |   IE   | | :-----: |
        :-----: | :-------: | :----: | :----: | | **50**  | **71**  |
        **9**   | **12** | **10** | | 6 _-x-_ |         | 5.1 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-span.

    - columnWidth (string | number; optional):
        The **`column-width`** CSS property sets the ideal column
        width in a multi-column layout. The container will have as
        many columns as can fit without any of them having a width
        less than the `column-width` value. If the width of the
        container is narrower than the specified value, the single
        column's width will be smaller than the declared column width.
        **Syntax**: `<length> | auto`  **Initial value**: `auto`  |
        Chrome  | Firefox | Safari  |  Edge  |   IE   | | :-----: |
        :-----: | :-----: | :----: | :----: | | **50**  | **50**  |
        **9**  | **12** | **10** | | 1 _-x-_ |         | 3 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/column-width.

    - columns (string | number; optional):
        The **`columns`** CSS shorthand property sets the number of
        columns to use when drawing an element's contents, as well as
        those columns' widths.  **Syntax**: `<'column-width'> ||
        <'column-count'>`  | Chrome | Firefox | Safari  |  Edge  |
        IE   | | :----: | :-----: | :-----: | :----: | :----: | |
        **50** | **52**  |  **9**  | **12** | **10** | |        |
        | 3 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/columns.

    - contain (boolean | number | string | dict | list; optional):
        The **`contain`** CSS property indicates that an element and
        its contents are, as much as possible, independent from the
        rest of the document tree. Containment enables isolating a
        subsection of the DOM, providing performance benefits by
        limiting calculations of layout, style, paint, size, or any
        combination to a DOM subtree rather than the entire page.
        Containment can also be used to scope CSS counters and quotes.
        **Syntax**: `none | strict | content | [ [ size || inline-size
        ] || layout || style || paint ]`  **Initial value**: `none`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **52** | **69**  | **15.4** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/contain.

    - containIntrinsicBlockSize (string | number; optional):
        The **`contain-intrinsic-block-size`** CSS logical property
        defines the block size of an element that a browser can use
        for layout when the element is subject to size containment.
        **Syntax**: `auto? [ none | <length> ]`  **Initial value**:
        `none`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | | **95** | **107** | **17** |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/contain-intrinsic-contain-intrinsic-block-size.

    - containIntrinsicHeight (string | number; optional):
        The **`contain-intrinsic-length`** CSS property sets the
        height of an element that a browser can use for layout when
        the element is subject to size containment.  **Syntax**:
        `auto? [ none | <length> ]`  **Initial value**: `none`  |
        Chrome | Firefox | Safari | Edge | IE  | | :----: | :-----: |
        :----: | :--: | :-: | | **95** | **107** | **17** | n/a  | No
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/contain-intrinsic-height.

    - containIntrinsicInlineSize (string | number; optional):
        The **`contain-intrinsic-inline-size`** CSS logical property
        defines the inline-size of an element that a browser can use
        for layout when the element is subject to size containment.
        **Syntax**: `auto? [ none | <length> ]`  **Initial value**:
        `none`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | | **95** | **107** | **17** |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/contain-intrinsic-contain-intrinsic-inline-size.

    - containIntrinsicSize (string | number; optional):
        The **`contain-intrinsic-size`** CSS shorthand property sets
        the size of an element that a browser will use for layout when
        the element is subject to size containment.  **Syntax**: `[
        auto? [ none | <length> ] ]{1,2}`  | Chrome | Firefox | Safari
        | Edge | IE  | | :----: | :-----: | :----: | :--: | :-: | |
        **83** | **107** | **17** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/contain-intrinsic-size.

    - containIntrinsicWidth (string | number; optional):
        The **`contain-intrinsic-width`** CSS property sets the width
        of an element that a browser will use for layout when the
        element is subject to size containment.  **Syntax**: `auto? [
        none | <length> ]`  **Initial value**: `none`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **95** | **107** | **17** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/contain-intrinsic-width.

    - container (boolean | number | string | dict | list; optional):
        The **container** shorthand CSS property establishes the
        element as a query container and specifies the name or name
        for the containment context used in a container query.
        **Syntax**: `<'container-name'> [ / <'container-type'> ]?`  |
        Chrome  | Firefox | Safari | Edge | IE  | | :-----: | :-----:
        | :----: | :--: | :-: | | **105** | **110** | **16** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/container.

    - containerName (boolean | number | string | dict | list; optional):
        The **container-name** CSS property specifies a list of query
        container names used by the @container at-rule in a container
        query. A container query will apply styles to elements based
        on the size of the nearest ancestor with a containment
        context. When a containment context is given a name, it can be
        specifically targeted using the `@container` at-rule instead
        of the nearest ancestor with containment.  **Syntax**: `none |
        <custom-ident>+`  **Initial value**: `none`  | Chrome  |
        Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----: |
        :--: | :-: | | **105** | **110** | **16** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/container-name.

    - containerType (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'inline-size', 'size'; optional):
        The **container-type** CSS property is used to define the type
        of containment used in a container query.  **Syntax**: `normal
        | size | inline-size`  **Initial value**: `normal`  | Chrome
        | Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----:
        | :--: | :-: | | **105** | **110** | **16** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/container-type.

    - content (boolean | number | string | dict | list; optional):
        The **`content`** CSS property replaces an element with a
        generated value. Objects inserted using the `content` property
        are **anonymous replaced elements**.  **Syntax**: `normal |
        none | [ <content-replacement> | <content-list> ] [/ [
        <string> | <counter> ]+ ]?`  **Initial value**: `normal`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/content.

    - contentVisibility (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible'; optional):
        The **`content-visibility`** CSS property controls whether or
        not an element renders its contents at all, along with forcing
        a strong set of containments, allowing user agents to
        potentially omit large swathes of layout and rendering work
        until it becomes needed. It enables the user agent to skip an
        element's rendering work (including layout and painting) until
        it is needed — which makes the initial page load much faster.
        **Syntax**: `visible | auto | hidden`  **Initial value**:
        `visible`  | Chrome |   Firefox   | Safari | Edge | IE  | |
        :----: | :---------: | :----: | :--: | :-: | | **85** |
        **preview** |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/content-visibility.

    - counterIncrement (boolean | number | string | dict | list; optional):
        The **`counter-increment`** CSS property increases or
        decreases the value of a CSS counter by a given value.
        **Syntax**: `[ <counter-name> <integer>? ]+ | none`  **Initial
        value**: `none`  | Chrome | Firefox | Safari |  Edge  |  IE
        | | :----: | :-----: | :----: | :----: | :---: | | **2**  |
        **1**  | **3**  | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/counter-increment.

    - counterReset (boolean | number | string | dict | list; optional):
        The **`counter-reset`** CSS property resets a CSS counter to a
        given value. This property will create a new counter or
        reversed counter with the given name on the specified element.
        **Syntax**: `[ <counter-name> <integer>? |
        <reversed-counter-name> <integer>? ]+ | none`  **Initial
        value**: `none`  | Chrome | Firefox | Safari |  Edge  |  IE
        | | :----: | :-----: | :----: | :----: | :---: | | **2**  |
        **1**  | **3**  | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/counter-reset.

    - counterSet (boolean | number | string | dict | list; optional):
        The **`counter-set`** CSS property sets a CSS counter to a
        given value. It manipulates the value of existing counters,
        and will only create new counters if there isn't already a
        counter of the given name on the element.  **Syntax**: `[
        <counter-name> <integer>? ]+ | none`  **Initial value**:
        `none`  | Chrome | Firefox |  Safari  | Edge | IE  | | :----:
        | :-----: | :------: | :--: | :-: | | **85** | **68**  |
        **17.2** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/counter-set.

    - cursor (boolean | number | string | dict | list; optional):
        The **`cursor`** CSS property sets the mouse cursor, if any,
        to show when the mouse pointer is over an element.
        **Syntax**: `[ [ <url> [ <x> <y> ]? , ]* [ auto | default |
        none | context-menu | help | pointer | progress | wait | cell
        | crosshair | text | vertical-text | alias | copy | move |
        no-drop | not-allowed | e-resize | n-resize | ne-resize |
        nw-resize | s-resize | se-resize | sw-resize | w-resize |
        ew-resize | ns-resize | nesw-resize | nwse-resize | col-resize
        | row-resize | all-scroll | zoom-in | zoom-out | grab |
        grabbing ] ]`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari  |  Edge  |  IE   | | :----: | :-----: | :-----: |
        :----: | :---: | | **1**  |  **1**  | **1.2** | **12** | **4**
        | @,see,https,://developer.mozilla.org/docs/Web/CSS/cursor.

    - direction (a value equal to: 'ltr', 'rtl', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`direction`** CSS property sets the direction of text,
        table columns, and horizontal overflow. Use `rtl` for
        languages written from right to left (like Hebrew or Arabic),
        and `ltr` for those written from left to right (like English
        and most other languages).  **Syntax**: `ltr | rtl`  **Initial
        value**: `ltr`  | Chrome | Firefox | Safari |  Edge  |   IE
        | | :----: | :-----: | :----: | :----: | :-----: | | **2**  |
        **1**  | **1**  | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/direction.

    - display (boolean | number | string | dict | list; optional):
        The **`display`** CSS property sets whether an element is
        treated as a block or inline element and the layout used for
        its children, such as flow layout, grid or flex.  **Syntax**:
        `[ <display-outside> || <display-inside> ] |
        <display-listitem> | <display-internal> | <display-box> |
        <display-legacy>`  **Initial value**: `inline`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/display.

    - dominantBaseline (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'middle', 'alphabetic', 'central', 'hanging', 'ideographic', 'mathematical', 'text-after-edge', 'text-before-edge', 'no-change', 'reset-size', 'use-script'; optional)

    - emptyCells (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hide', 'show'; optional):
        The **`empty-cells`** CSS property sets whether borders and
        backgrounds appear around `<table>` cells that have no visible
        content.  **Syntax**: `show | hide`  **Initial value**: `show`
        | Chrome | Firefox | Safari  |  Edge  |  IE   | | :----: |
        :-----: | :-----: | :----: | :---: | | **1**  |  **1**  |
        **1.2** | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/empty-cells.

    - fill (boolean | number | string | dict | list; optional)

    - fillOpacity (boolean | number | string | dict | list; optional)

    - fillRule (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'evenodd', 'nonzero'; optional)

    - filter (boolean | number | string | dict | list; optional):
        The **`filter`** CSS property applies graphical effects like
        blur or color shift to an element. Filters are commonly used
        to adjust the rendering of images, backgrounds, and borders.
        **Syntax**: `none | <filter-function-list>`  **Initial
        value**: `none`  |  Chrome  | Firefox | Safari  |  Edge  | IE
        | | :------: | :-----: | :-----: | :----: | :-: | |  **53**  |
        **35**  | **9.1** | **12** | No  | | 18 _-x-_ |         | 6
        _-x-_ |        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/filter.

    - flex (string | number; optional):
        The **`flex`** CSS shorthand property sets how a flex _item_
        will grow or shrink to fit the space available in its flex
        container.  **Syntax**: `none | [ <'flex-grow'>
        <'flex-shrink'>? || <'flex-basis'> ]`  |  Chrome  | Firefox |
        Safari  |  Edge  |    IE    | | :------: | :-----: | :-----: |
        :----: | :------: | |  **29**  | **20**  |  **9**  | **12** |
        **11**  | | 21 _-x-_ |         | 7 _-x-_ |        | 10 _-x-_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex.

    - flexBasis (string | number; optional):
        The **`flex-basis`** CSS property sets the initial main size
        of a flex item. It sets the size of the content box unless
        otherwise set with `box-sizing`.  **Syntax**: `content |
        <'width'>`  **Initial value**: `auto`  |  Chrome  | Firefox |
        Safari  |  Edge  |   IE   | | :------: | :-----: | :-----: |
        :----: | :----: | |  **29**  | **22**  |  **9**  | **12** |
        **11** | | 22 _-x-_ |         | 7 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex-basis.

    - flexDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'column', 'column-reverse', 'row', 'row-reverse'; optional):
        The **`flex-direction`** CSS property sets how flex items are
        placed in the flex container defining the main axis and the
        direction (normal or reversed).  **Syntax**: `row |
        row-reverse | column | column-reverse`  **Initial value**:
        `row`  |  Chrome  | Firefox  | Safari  |  Edge  |    IE    | |
        :------: | :------: | :-----: | :----: | :------: | |  **29**
        |  **81**  |  **9**  | **12** |  **11**  | | 21 _-x-_ | 49
        _-x-_ | 7 _-x-_ |        | 10 _-x-_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex-direction.

    - flexFlow (boolean | number | string | dict | list; optional):
        The **`flex-flow`** CSS shorthand property specifies the
        direction of a flex container, as well as its wrapping
        behavior.  **Syntax**: `<'flex-direction'> || <'flex-wrap'>`
        |  Chrome  | Firefox | Safari  |  Edge  |   IE   | | :------:
        | :-----: | :-----: | :----: | :----: | |  **29**  | **28**  |
        **9**  | **12** | **11** | | 21 _-x-_ |         | 7 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex-flow.

    - flexGrow (boolean | number | string | dict | list; optional):
        The **`flex-grow`** CSS property sets the flex grow factor of
        a flex item's main size.  **Syntax**: `<number>`  **Initial
        value**: `0`  |  Chrome  | Firefox | Safari  |  Edge  |
        IE            | | :------: | :-----: | :-----: | :----: |
        :----------------------: | |  **29**  | **20**  |  **9**  |
        **12** |          **11**          | | 22 _-x-_ |         | 7
        _-x-_ |        | 10 _(-ms-flex-positive)_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex-grow.

    - flexShrink (boolean | number | string | dict | list; optional):
        The **`flex-shrink`** CSS property sets the flex shrink factor
        of a flex item. If the size of all flex items is larger than
        the flex container, items shrink to fit according to
        `flex-shrink`.  **Syntax**: `<number>`  **Initial value**: `1`
        |  Chrome  | Firefox | Safari  |  Edge  |   IE   | | :------:
        | :-----: | :-----: | :----: | :----: | |  **29**  | **20**  |
        **9**  | **12** | **10** | | 22 _-x-_ |         | 8 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex-shrink.

    - flexWrap (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'nowrap', 'wrap', 'wrap-reverse'; optional):
        The **`flex-wrap`** CSS property sets whether flex items are
        forced onto one line or can wrap onto multiple lines. If
        wrapping is allowed, it sets the direction that lines are
        stacked.  **Syntax**: `nowrap | wrap | wrap-reverse`
        **Initial value**: `nowrap`  |  Chrome  | Firefox | Safari  |
        Edge  |   IE   | | :------: | :-----: | :-----: | :----: |
        :----: | |  **29**  | **28**  |  **9**  | **12** | **11** | |
        21 _-x-_ |         | 7 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/flex-wrap.

    - float (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'left', 'right', 'inline-end', 'inline-start'; optional):
        The **`float`** CSS property places an element on the left or
        right side of its container, allowing text and inline elements
        to wrap around it. The element is removed from the normal flow
        of the page, though still remaining a part of the flow (in
        contrast to absolute positioning).  **Syntax**: `left | right
        | none | inline-start | inline-end`  **Initial value**: `none`
        | Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/float.

    - floodColor (boolean | number | string | dict | list; optional)

    - floodOpacity (boolean | number | string | dict | list; optional)

    - font (boolean | number | string | dict | list; optional):
        The **`font`** CSS shorthand property sets all the different
        properties of an element's font. Alternatively, it sets an
        element's font to a system font.  **Syntax**: `[ [
        <'font-style'> || <font-variant-css21> || <'font-weight'> ||
        <'font-stretch'> ]? <'font-size'> [ / <'line-height'> ]?
        <'font-family'> ] | caption | icon | menu | message-box |
        small-caption | status-bar`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font.

    - fontFamily (boolean | number | string | dict | list; optional):
        The **`font-family`** CSS property specifies a prioritized
        list of one or more font family names and/or generic family
        names for the selected element.  **Syntax**: `[ <family-name>
        | <generic-family> ]#`  **Initial value**: depends on user
        agent  | Chrome | Firefox | Safari |  Edge  |  IE   | | :----:
        | :-----: | :----: | :----: | :---: | | **1**  |  **1**  |
        **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-family.

    - fontFeatureSettings (boolean | number | string | dict | list; optional):
        The **`font-feature-settings`** CSS property controls advanced
        typographic features in OpenType fonts.  **Syntax**: `normal |
        <feature-tag-value>#`  **Initial value**: `normal`  |  Chrome
        | Firefox  | Safari  |  Edge  |   IE   | | :------: | :------:
        | :-----: | :----: | :----: | |  **48**  |  **34**  | **9.1**
        | **15** | **10** | | 16 _-x-_ | 15 _-x-_ |         |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-feature-settings.

    - fontKerning (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal'; optional):
        The **`font-kerning`** CSS property sets the use of the
        kerning information stored in a font.  **Syntax**: `auto |
        normal | none`  **Initial value**: `auto`  | Chrome | Firefox
        | Safari  | Edge | IE  | | :----: | :-----: | :-----: | :--: |
        :-: | | **33** | **32**  |  **9**  | n/a  | No  | |        |
        | 6 _-x-_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-kerning.

    - fontLanguageOverride (boolean | number | string | dict | list; optional):
        The **`font-language-override`** CSS property controls the use
        of language-specific glyphs in a typeface.  **Syntax**:
        `normal | <string>`  **Initial value**: `normal`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | |   No   | **34**  |   No   | n/a  | No  | |
        | 4 _-x-_ |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-language-override.

    - fontOpticalSizing (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`font-optical-sizing`** CSS property sets whether text
        rendering is optimized for viewing at different sizes.
        **Syntax**: `auto | none`  **Initial value**: `auto`  | Chrome
        | Firefox | Safari |  Edge  | IE  | | :----: | :-----: |
        :----: | :----: | :-: | | **79** | **62**  | **11** | **17** |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-optical-sizing.

    - fontPalette (boolean | number | string | dict | list; optional):
        **Syntax**: `normal | light | dark | <palette-identifier>`
        **Initial value**: `normal`  | Chrome  | Firefox |  Safari  |
        Edge | IE  | | :-----: | :-----: | :------: | :--: | :-: | |
        **101** | **107** | **15.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-palette.

    - fontSize (string | number; optional):
        The **`font-size`** CSS property sets the size of the font.
        Changing the font size also updates the sizes of the font
        size-relative `<length>` units, such as `em`, `ex`, and so
        forth.  **Syntax**: `<absolute-size> | <relative-size> |
        <length-percentage>`  **Initial value**: `medium`  | Chrome |
        Firefox | Safari |  Edge  |   IE    | | :----: | :-----: |
        :----: | :----: | :-----: | | **1**  |  **1**  | **1**  |
        **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-size.

    - fontSizeAdjust (boolean | number | string | dict | list; optional):
        The **`font-size-adjust`** CSS property sets the size of
        lower-case letters relative to the current font size (which
        defines the size of upper-case letters).  **Syntax**: `none |
        [ ex-height | cap-height | ch-width | ic-width | ic-height ]?
        [ from-font | <number> ]`  **Initial value**: `none`  | Chrome
        | Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | |   No   |  **3**  | **16.4** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-size-adjust.

    - fontSmooth (string | number; optional):
        The **`font-smooth`** CSS property controls the application of
        anti-aliasing when fonts are rendered.  **Syntax**: `auto |
        never | always | <absolute-size> | <length>`  **Initial
        value**: `auto`  |              Chrome              |
        Firefox               |              Safari              |
        Edge | IE  | | :------------------------------: |
        :--------------------------------: |
        :------------------------------: | :--: | :-: | | **5**
        _(-webkit-font-smoothing)_ | **25**
        _(-moz-osx-font-smoothing)_ | **4** _(-webkit-font-smoothing)_
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-smooth.

    - fontStretch (boolean | number | string | dict | list; optional):
        The **`font-stretch`** CSS property selects a normal,
        condensed, or expanded face from a font.  **Syntax**:
        `<font-stretch-absolute>`  **Initial value**: `normal`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **60** |  **9**  |
        **11** | **12** | **9** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-stretch.

    - fontStyle (boolean | number | string | dict | list; optional):
        The **`font-style`** CSS property sets whether a font should
        be styled with a normal, italic, or oblique face from its
        `font-family`.  **Syntax**: `normal | italic | oblique
        <angle>?`  **Initial value**: `normal`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-style.

    - fontSynthesis (boolean | number | string | dict | list; optional):
        The **`font-synthesis`** CSS property controls which missing
        typefaces, bold, italic, or small-caps, may be synthesized by
        the browser.  **Syntax**: `none | [ weight || style ||
        small-caps || position]`  **Initial value**: `weight style
        small-caps position `  | Chrome | Firefox | Safari | Edge | IE
        | | :----: | :-----: | :----: | :--: | :-: | | **97** | **34**
        | **9**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-synthesis.

    - fontSynthesisPosition (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`font-synthesis-position`** CSS property lets you
        specify whether or not a browser may synthesize the subscript
        and superscript \"position\" typefaces when they are missing
        in a font family, while using `font-variant-position` to set
        the positions.  **Syntax**: `auto | none`  **Initial value**:
        `none`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | |   No   | **118** |   No   |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-synthesis-position.

    - fontSynthesisSmallCaps (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`font-synthesis-small-caps`** CSS property lets you
        specify whether or not the browser may synthesize small-caps
        typeface when it is missing in a font family. Small-caps
        glyphs typically use the form of uppercase letters but are
        reduced to the size of lowercase letters.  **Syntax**: `auto |
        none`  **Initial value**: `auto`  | Chrome | Firefox |  Safari
        | Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **97** | **111** | **16.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-synthesis-small-caps.

    - fontSynthesisStyle (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`font-synthesis-style`** CSS property lets you specify
        whether or not the browser may synthesize the oblique typeface
        when it is missing in a font family.  **Syntax**: `auto |
        none`  **Initial value**: `auto`  | Chrome | Firefox |  Safari
        | Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **97** | **111** | **16.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-synthesis-style.

    - fontSynthesisWeight (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`font-synthesis-weight`** CSS property lets you specify
        whether or not the browser may synthesize the bold typeface
        when it is missing in a font family.  **Syntax**: `auto |
        none`  **Initial value**: `auto`  | Chrome | Firefox |  Safari
        | Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **97** | **111** | **16.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-synthesis-weight.

    - fontVariant (boolean | number | string | dict | list; optional):
        The **`font-variant`** CSS shorthand property allows you to
        set all the font variants for a font.  **Syntax**: `normal |
        none | [ <common-lig-values> || <discretionary-lig-values> ||
        <historical-lig-values> || <contextual-alt-values> ||
        stylistic( <feature-value-name> ) || historical-forms ||
        styleset( <feature-value-name># ) || character-variant(
        <feature-value-name># ) || swash( <feature-value-name> ) ||
        ornaments( <feature-value-name> ) || annotation(
        <feature-value-name> ) || [ small-caps | all-small-caps |
        petite-caps | all-petite-caps | unicase | titling-caps ] ||
        <numeric-figure-values> || <numeric-spacing-values> ||
        <numeric-fraction-values> || ordinal || slashed-zero ||
        <east-asian-variant-values> || <east-asian-width-values> ||
        ruby ]`  **Initial value**: `normal`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant.

    - fontVariantAlternates (boolean | number | string | dict | list; optional):
        The **`font-variant-alternates`** CSS property controls the
        usage of alternate glyphs. These alternate glyphs may be
        referenced by alternative names defined in
        `@font-feature-values`.  **Syntax**: `normal | [ stylistic(
        <feature-value-name> ) || historical-forms || styleset(
        <feature-value-name># ) || character-variant(
        <feature-value-name># ) || swash( <feature-value-name> ) ||
        ornaments( <feature-value-name> ) || annotation(
        <feature-value-name> ) ]`  **Initial value**: `normal`  |
        Chrome  | Firefox | Safari  | Edge | IE  | | :-----: | :-----:
        | :-----: | :--: | :-: | | **111** | **34**  | **9.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-alternates.

    - fontVariantCaps (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'small-caps', 'all-petite-caps', 'all-small-caps', 'petite-caps', 'titling-caps', 'unicase'; optional):
        The **`font-variant-caps`** CSS property controls the use of
        alternate glyphs for capital letters.  **Syntax**: `normal |
        small-caps | all-small-caps | petite-caps | all-petite-caps |
        unicase | titling-caps`  **Initial value**: `normal`  | Chrome
        | Firefox | Safari  | Edge | IE  | | :----: | :-----: |
        :-----: | :--: | :-: | | **52** | **34**  | **9.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-caps.

    - fontVariantEastAsian (boolean | number | string | dict | list; optional):
        The **`font-variant-east-asian`** CSS property controls the
        use of alternate glyphs for East Asian scripts, like Japanese
        and Chinese.  **Syntax**: `normal | [
        <east-asian-variant-values> || <east-asian-width-values> ||
        ruby ]`  **Initial value**: `normal`  | Chrome | Firefox |
        Safari  | Edge | IE  | | :----: | :-----: | :-----: | :--: |
        :-: | | **63** | **34**  | **9.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-east-asian.

    - fontVariantEmoji (a value equal to: 'text', 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'emoji', 'unicode'; optional):
        **Syntax**: `normal | text | emoji | unicode`  **Initial
        value**: `normal`  | Chrome | Firefox | Safari | Edge | IE  |
        | :----: | :-----: | :----: | :--: | :-: | |   No   |   n/a
        |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-emoji.

    - fontVariantLigatures (boolean | number | string | dict | list; optional):
        The **`font-variant-ligatures`** CSS property controls which
        ligatures and contextual forms are used in textual content of
        the elements it applies to. This leads to more harmonized
        forms in the resulting text.  **Syntax**: `normal | none | [
        <common-lig-values> || <discretionary-lig-values> ||
        <historical-lig-values> || <contextual-alt-values> ]`
        **Initial value**: `normal`  |  Chrome  | Firefox | Safari  |
        Edge | IE  | | :------: | :-----: | :-----: | :--: | :-: | |
        **34**  | **34**  | **9.1** | n/a  | No  | | 31 _-x-_ |
        | 7 _-x-_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-ligatures.

    - fontVariantNumeric (boolean | number | string | dict | list; optional):
        The **`font-variant-numeric`** CSS property controls the usage
        of alternate glyphs for numbers, fractions, and ordinal
        markers.  **Syntax**: `normal | [ <numeric-figure-values> ||
        <numeric-spacing-values> || <numeric-fraction-values> ||
        ordinal || slashed-zero ]`  **Initial value**: `normal`  |
        Chrome | Firefox | Safari  | Edge | IE  | | :----: | :-----: |
        :-----: | :--: | :-: | | **52** | **34**  | **9.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-numeric.

    - fontVariantPosition (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'sub', 'super'; optional):
        The **`font-variant-position`** CSS property controls the use
        of alternate, smaller glyphs that are positioned as
        superscript or subscript.  **Syntax**: `normal | sub | super`
        **Initial value**: `normal`  | Chrome  | Firefox | Safari  |
        Edge | IE  | | :-----: | :-----: | :-----: | :--: | :-: | |
        **117** | **34**  | **9.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variant-position.

    - fontVariationSettings (boolean | number | string | dict | list; optional):
        The **`font-variation-settings`** CSS property provides
        low-level control over variable font characteristics, by
        specifying the four letter axis names of the characteristics
        you want to vary, along with their values.  **Syntax**:
        `normal | [ <string> <number> ]#`  **Initial value**: `normal`
        | Chrome | Firefox | Safari |  Edge  | IE  | | :----: |
        :-----: | :----: | :----: | :-: | | **62** | **62**  | **11**
        | **17** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-variation-settings.

    - fontWeight (boolean | number | string | dict | list; optional):
        The **`font-weight`** CSS property sets the weight (or
        boldness) of the font. The weights available depend on the
        `font-family` that is currently set.  **Syntax**:
        `<font-weight-absolute> | bolder | lighter`  **Initial
        value**: `normal`  | Chrome | Firefox | Safari |  Edge  |  IE
        | | :----: | :-----: | :----: | :----: | :---: | | **2**  |
        **1**  | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/font-weight.

    - forcedColorAdjust (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`forced-color-adjust`** CSS property allows authors to
        opt certain elements out of forced colors mode. This then
        restores the control of those values to CSS.  **Syntax**:
        `auto | none`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari |              Edge               |                 IE
        | | :----: | :-----: | :----: |
        :-----------------------------: |
        :---------------------------------: | | **89** | **113** |
        No   |             **79**              | **10**
        _(-ms-high-contrast-adjust)_ | |        |         |        |
        12 _(-ms-high-contrast-adjust)_ |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/forced-color-adjust.

    - gap (string | number; optional):
        The **`gap`** CSS property sets the gaps (gutters) between
        rows and columns. It is a shorthand for `row-gap` and
        `column-gap`.  **Syntax**: `<'row-gap'> <'column-gap'>?`  |
        Chrome | Firefox |  Safari  |  Edge  | IE  | | :----: |
        :-----: | :------: | :----: | :-: | | **57** | **52**  |
        **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/gap.

    - glyphOrientationVertical (boolean | number | string | dict | list; optional)

    - grid (boolean | number | string | dict | list; optional):
        The **`grid`** CSS property is a shorthand property that sets
        all of the explicit and implicit grid properties in a single
        declaration.  **Syntax**: `<'grid-template'> |
        <'grid-template-rows'> / [ auto-flow && dense? ]
        <'grid-auto-columns'>? | [ auto-flow && dense? ]
        <'grid-auto-rows'>? / <'grid-template-columns'>`  | Chrome |
        Firefox |  Safari  |  Edge  | IE  | | :----: | :-----: |
        :------: | :----: | :-: | | **57** | **52**  | **10.1** |
        **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid.

    - gridArea (boolean | number | string | dict | list; optional):
        The **`grid-area`** CSS shorthand property specifies a grid
        item's size and location within a grid by contributing a line,
        a span, or nothing (automatic) to its grid placement, thereby
        specifying the edges of its grid area.  **Syntax**:
        `<grid-line> [ / <grid-line> ]{0,3}`  | Chrome | Firefox |
        Safari  |  Edge  | IE  | | :----: | :-----: | :------: |
        :----: | :-: | | **57** | **52**  | **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-area.

    - gridAutoColumns (string | number; optional):
        The **`grid-auto-columns`** CSS property specifies the size of
        an implicitly-created grid column track or pattern of tracks.
        **Syntax**: `<track-size>+`  **Initial value**: `auto`  |
        Chrome | Firefox |  Safari  |  Edge  |             IE
        | | :----: | :-----: | :------: | :----: |
        :-------------------------: | | **57** | **70**  | **10.1** |
        **16** | **10** _(-ms-grid-columns)_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-auto-columns.

    - gridAutoFlow (boolean | number | string | dict | list; optional):
        The **`grid-auto-flow`** CSS property controls how the
        auto-placement algorithm works, specifying exactly how
        auto-placed items get flowed into the grid.  **Syntax**: `[
        row | column ] || dense`  **Initial value**: `row`  | Chrome |
        Firefox |  Safari  |  Edge  | IE  | | :----: | :-----: |
        :------: | :----: | :-: | | **57** | **52**  | **10.1** |
        **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-auto-flow.

    - gridAutoRows (string | number; optional):
        The **`grid-auto-rows`** CSS property specifies the size of an
        implicitly-created grid row track or pattern of tracks.
        **Syntax**: `<track-size>+`  **Initial value**: `auto`  |
        Chrome | Firefox |  Safari  |  Edge  |            IE
        | | :----: | :-----: | :------: | :----: |
        :----------------------: | | **57** | **70**  | **10.1** |
        **16** | **10** _(-ms-grid-rows)_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-auto-rows.

    - gridColumn (boolean | number | string | dict | list; optional):
        The **`grid-column`** CSS shorthand property specifies a grid
        item's size and location within a grid column by contributing
        a line, a span, or nothing (automatic) to its grid placement,
        thereby specifying the inline-start and inline-end edge of its
        grid area.  **Syntax**: `<grid-line> [ / <grid-line> ]?`  |
        Chrome | Firefox |  Safari  |  Edge  | IE  | | :----: |
        :-----: | :------: | :----: | :-: | | **57** | **52**  |
        **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-column.

    - gridColumnEnd (boolean | number | string | dict | list; optional):
        The **`grid-column-end`** CSS property specifies a grid item's
        end position within the grid column by contributing a line, a
        span, or nothing (automatic) to its grid placement, thereby
        specifying the block-end edge of its grid area.  **Syntax**:
        `<grid-line>`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari  |  Edge  | IE  | | :----: | :-----: | :------: |
        :----: | :-: | | **57** | **52**  | **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-column-end.

    - gridColumnGap (string | number; optional):
        The **`column-gap`** CSS property sets the size of the gap
        (gutter) between an element's columns.  **Syntax**:
        `<length-percentage>`  **Initial value**: `0` @,deprecated.

    - gridColumnStart (boolean | number | string | dict | list; optional):
        The **`grid-column-start`** CSS property specifies a grid
        item's start position within the grid column by contributing a
        line, a span, or nothing (automatic) to its grid placement.
        This start position defines the block-start edge of the grid
        area.  **Syntax**: `<grid-line>`  **Initial value**: `auto`  |
        Chrome | Firefox |  Safari  |  Edge  | IE  | | :----: |
        :-----: | :------: | :----: | :-: | | **57** | **52**  |
        **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-column-start.

    - gridGap (string | number; optional):
        The **`gap`** CSS property sets the gaps (gutters) between
        rows and columns. It is a shorthand for `row-gap` and
        `column-gap`.  **Syntax**: `<'grid-row-gap'>
        <'grid-column-gap'>?` @,deprecated.

    - gridRow (boolean | number | string | dict | list; optional):
        The **`grid-row`** CSS shorthand property specifies a grid
        item's size and location within a grid row by contributing a
        line, a span, or nothing (automatic) to its grid placement,
        thereby specifying the inline-start and inline-end edge of its
        grid area.  **Syntax**: `<grid-line> [ / <grid-line> ]?`  |
        Chrome | Firefox |  Safari  |  Edge  | IE  | | :----: |
        :-----: | :------: | :----: | :-: | | **57** | **52**  |
        **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-row.

    - gridRowEnd (boolean | number | string | dict | list; optional):
        The **`grid-row-end`** CSS property specifies a grid item's
        end position within the grid row by contributing a line, a
        span, or nothing (automatic) to its grid placement, thereby
        specifying the inline-end edge of its grid area.  **Syntax**:
        `<grid-line>`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari  |  Edge  | IE  | | :----: | :-----: | :------: |
        :----: | :-: | | **57** | **52**  | **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-row-end.

    - gridRowGap (string | number; optional):
        The **`row-gap`** CSS property sets the size of the gap
        (gutter) between an element's rows.  **Syntax**:
        `<length-percentage>`  **Initial value**: `0` @,deprecated.

    - gridRowStart (boolean | number | string | dict | list; optional):
        The **`grid-row-start`** CSS property specifies a grid item's
        start position within the grid row by contributing a line, a
        span, or nothing (automatic) to its grid placement, thereby
        specifying the inline-start edge of its grid area.
        **Syntax**: `<grid-line>`  **Initial value**: `auto`  | Chrome
        | Firefox |  Safari  |  Edge  | IE  | | :----: | :-----: |
        :------: | :----: | :-: | | **57** | **52**  | **10.1** |
        **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-row-start.

    - gridTemplate (boolean | number | string | dict | list; optional):
        The **`grid-template`** CSS property is a shorthand property
        for defining grid columns, grid rows, and grid areas.
        **Syntax**: `none | [ <'grid-template-rows'> /
        <'grid-template-columns'> ] | [ <line-names>? <string>
        <track-size>? <line-names>? ]+ [ / <explicit-track-list> ]?`
        | Chrome | Firefox |  Safari  |  Edge  | IE  | | :----: |
        :-----: | :------: | :----: | :-: | | **57** | **52**  |
        **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-template.

    - gridTemplateAreas (boolean | number | string | dict | list; optional):
        The **`grid-template-areas`** CSS property specifies named
        grid areas, establishing the cells in the grid and assigning
        them names.  **Syntax**: `none | <string>+`  **Initial
        value**: `none`  | Chrome | Firefox |  Safari  |  Edge  | IE
        | | :----: | :-----: | :------: | :----: | :-: | | **57** |
        **52**  | **10.1** | **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-template-areas.

    - gridTemplateColumns (string | number; optional):
        The **`grid-template-columns`** CSS property defines the line
        names and track sizing functions of the grid columns.
        **Syntax**: `none | <track-list> | <auto-track-list> | subgrid
        <line-name-list>?`  **Initial value**: `none`  | Chrome |
        Firefox |  Safari  |  Edge  |             IE              | |
        :----: | :-----: | :------: | :----: |
        :-------------------------: | | **57** | **52**  | **10.1** |
        **16** | **10** _(-ms-grid-columns)_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-template-columns.

    - gridTemplateRows (string | number; optional):
        The **`grid-template-rows`** CSS property defines the line
        names and track sizing functions of the grid rows.
        **Syntax**: `none | <track-list> | <auto-track-list> | subgrid
        <line-name-list>?`  **Initial value**: `none`  | Chrome |
        Firefox |  Safari  |  Edge  |            IE            | |
        :----: | :-----: | :------: | :----: |
        :----------------------: | | **57** | **52**  | **10.1** |
        **16** | **10** _(-ms-grid-rows)_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/grid-template-rows.

    - hangingPunctuation (boolean | number | string | dict | list; optional):
        The **`hanging-punctuation`** CSS property specifies whether a
        punctuation mark should hang at the start or end of a line of
        text. Hanging punctuation may be placed outside the line box.
        **Syntax**: `none | [ first || [ force-end | allow-end ] ||
        last ]`  **Initial value**: `none`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | |   No   |   No    | **10** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/hanging-punctuation.

    - height (string | number; optional):
        The **`height`** CSS property specifies the height of an
        element. By default, the property defines the height of the
        content area. If `box-sizing` is set to `border-box`, however,
        it instead determines the height of the border area.
        **Syntax**: `auto | <length> | <percentage> | min-content |
        max-content | fit-content | fit-content(<length-percentage>)`
        **Initial value**: `auto`  | Chrome | Firefox | Safari |  Edge
        |  IE   | | :----: | :-----: | :----: | :----: | :---: | |
        **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/height.

    - hyphenateCharacter (boolean | number | string | dict | list; optional):
        The **`hyphenate-character`** CSS property sets the character
        (or string) used at the end of a line before a hyphenation
        break.  **Syntax**: `auto | <string>`  **Initial value**:
        `auto`  | Chrome  | Firefox |  Safari   | Edge | IE  | |
        :-----: | :-----: | :-------: | :--: | :-: | | **106** |
        **98**  |  **17**   | n/a  | No  | | 6 _-x-_ |         | 5.1
        _-x-_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/hyphenate-character.

    - hyphenateLimitChars (boolean | number | string | dict | list; optional):
        The **`hyphenate-limit-chars`** CSS property specifies the
        minimum word length to allow hyphenation of words as well as
        the the minimum number of characters before and after the
        hyphen.  **Syntax**: `[ auto | <integer> ]{1,3}`  **Initial
        value**: `auto`  | Chrome  | Firefox | Safari | Edge | IE  | |
        :-----: | :-----: | :----: | :--: | :-: | | **109** |   No
        |   No   | n/a  | No  |.

    - hyphens (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'manual'; optional):
        The **`hyphens`** CSS property specifies how words should be
        hyphenated when text wraps across multiple lines. It can
        prevent hyphenation entirely, hyphenate at manually-specified
        points within the text, or let the browser automatically
        insert hyphens where appropriate.  **Syntax**: `none | manual
        | auto`  **Initial value**: `manual`  |  Chrome  | Firefox |
        Safari   |  Edge  |      IE      | | :------: | :-----: |
        :-------: | :----: | :----------: | |  **55**  | **43**  |
        **17**   | **79** | **10** _-x-_ | | 13 _-x-_ | 6 _-x-_ | 5.1
        _-x-_ |        |              |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/hyphens.

    - imageOrientation (boolean | number | string | dict | list; optional):
        The **`image-orientation`** CSS property specifies a
        layout-independent correction to the orientation of an image.
        **Syntax**: `from-image | <angle> | [ <angle>? flip ]`
        **Initial value**: `from-image`  | Chrome | Firefox |  Safari
        | Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **81** | **26**  | **13.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/image-orientation.

    - imageRendering (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', '-moz-crisp-edges', '-webkit-optimize-contrast', 'crisp-edges', 'pixelated'; optional):
        The **`image-rendering`** CSS property sets an image scaling
        algorithm. The property applies to an element itself, to any
        images set in its other properties, and to its descendants.
        **Syntax**: `auto | crisp-edges | pixelated`  **Initial
        value**: `auto`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | | **13** | **3.6** |
        **6**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/image-rendering.

    - imageResolution (boolean | number | string | dict | list; optional):
        **Syntax**: `[ from-image || <resolution> ] && snap?`
        **Initial value**: `1dppx`.

    - imeMode (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'active', 'disabled', 'inactive'; optional):
        The **`ime-mode`** CSS property controls the state of the
        input method editor (IME) for text fields. This property is
        obsolete.  **Syntax**: `auto | normal | active | inactive |
        disabled`  **Initial value**: `auto` @,deprecated.

    - initialLetter (boolean | number | string | dict | list; optional):
        The `initial-letter` CSS property sets styling for dropped,
        raised, and sunken initial letters.  **Syntax**: `normal | [
        <number> <integer>? ]`  **Initial value**: `normal`  | Chrome
        | Firefox |   Safari    | Edge | IE  | | :-----: | :-----: |
        :---------: | :--: | :-: | | **110** |   No    | **9** _-x-_ |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/initial-letter.

    - inlineSize (string | number; optional):
        The **`inline-size`** CSS property defines the horizontal or
        vertical size of an element's block, depending on its writing
        mode. It corresponds to either the `width` or the `height`
        property, depending on the value of `writing-mode`.
        **Syntax**: `<'width'>`  **Initial value**: `auto`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **57** | **41**  | **12.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inline-size.

    - inputSecurity (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        **Syntax**: `auto | none`  **Initial value**: `auto`.

    - inset (string | number; optional):
        The **`inset`** CSS property is a shorthand that corresponds
        to the `top`, `right`, `bottom`, and/or `left` properties. It
        has the same multi-value syntax of the `margin` shorthand.
        **Syntax**: `<'top'>{1,4}`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **87** | **66**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset.

    - insetBlock (string | number; optional):
        The **`inset-block`** CSS property defines the logical block
        start and end offsets of an element, which maps to physical
        offsets depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `top` and `bottom`, or `right` and `left` properties depending
        on the values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'top'>{1,2}`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **63**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset-block.

    - insetBlockEnd (string | number; optional):
        The **`inset-block-end`** CSS property defines the logical
        block end offset of an element, which maps to a physical inset
        depending on the element's writing mode, directionality, and
        text orientation. It corresponds to the `top`, `right`,
        `bottom`, or `left` property depending on the values defined
        for `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'top'>`  **Initial value**: `auto`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **63**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset-block-end.

    - insetBlockStart (string | number; optional):
        The **`inset-block-start`** CSS property defines the logical
        block start offset of an element, which maps to a physical
        inset depending on the element's writing mode, directionality,
        and text orientation. It corresponds to the `top`, `right`,
        `bottom`, or `left` property depending on the values defined
        for `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'top'>`  **Initial value**: `auto`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **87** | **63**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset-block-start.

    - insetInline (string | number; optional):
        The **`inset-inline`** CSS property defines the logical start
        and end offsets of an element in the inline direction, which
        maps to physical offsets depending on the element's writing
        mode, directionality, and text orientation. It corresponds to
        the `top` and `bottom`, or `right` and `left` properties
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'top'>{1,2}`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **87** | **63**
        | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset-inline.

    - insetInlineEnd (string | number; optional):
        The **`inset-inline-end`** CSS property defines the logical
        inline end inset of an element, which maps to a physical
        offset depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `top`, `right`, `bottom`, or `left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'top'>`  **Initial value**:
        `auto`  | Chrome | Firefox |  Safari  | Edge | IE  | | :----:
        | :-----: | :------: | :--: | :-: | | **87** | **63**  |
        **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset-inline-end.

    - insetInlineStart (string | number; optional):
        The **`inset-inline-start`** CSS property defines the logical
        inline start inset of an element, which maps to a physical
        offset depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `top`, `right`, `bottom`, or `left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'top'>`  **Initial value**:
        `auto`  | Chrome | Firefox |  Safari  | Edge | IE  | | :----:
        | :-----: | :------: | :--: | :-: | | **87** | **63**  |
        **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/inset-inline-start.

    - isolation (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'isolate'; optional):
        The **`isolation`** CSS property determines whether an element
        must create a new stacking context.  **Syntax**: `auto |
        isolate`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | | **41** | **36**  | **8**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/isolation.

    - justifyContent (boolean | number | string | dict | list; optional):
        The CSS **`justify-content`** property defines how the browser
        distributes space between and around content items along the
        main-axis of a flex container, and the inline axis of a grid
        container.  **Syntax**: `normal | <content-distribution> |
        <overflow-position>? [ <content-position> | left | right ]`
        **Initial value**: `normal`  |  Chrome  | Firefox | Safari  |
        Edge  |   IE   | | :------: | :-----: | :-----: | :----: |
        :----: | |  **29**  | **20**  |  **9**  | **12** | **11** | |
        21 _-x-_ |         | 7 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/justify-content.

    - justifyItems (boolean | number | string | dict | list; optional):
        The CSS **`justify-items`** property defines the default
        `justify-self` for all items of the box, giving them all a
        default way of justifying each box along the appropriate axis.
        **Syntax**: `normal | stretch | <baseline-position> |
        <overflow-position>? [ <self-position> | left | right ] |
        legacy | legacy && [ left | right | center ]`  **Initial
        value**: `legacy`  | Chrome | Firefox | Safari |  Edge  |   IE
        | | :----: | :-----: | :----: | :----: | :----: | | **52** |
        **20**  | **9**  | **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/justify-items.

    - justifySelf (boolean | number | string | dict | list; optional):
        The CSS **`justify-self`** property sets the way a box is
        justified inside its alignment container along the appropriate
        axis.  **Syntax**: `auto | normal | stretch |
        <baseline-position> | <overflow-position>? [ <self-position> |
        left | right ]`  **Initial value**: `auto`  | Chrome | Firefox
        |  Safari  |  Edge  |   IE   | | :----: | :-----: | :------: |
        :----: | :----: | | **57** | **45**  | **10.1** | **16** |
        **10** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/justify-self.

    - justifyTracks (boolean | number | string | dict | list; optional):
        The **`justify-tracks`** CSS property sets the alignment in
        the masonry axis for grid containers that have masonry in
        their inline axis.  **Syntax**: `[ normal |
        <content-distribution> | <overflow-position>? [
        <content-position> | left | right ] ]#`  **Initial value**:
        `normal`  | Chrome | Firefox | Safari | Edge | IE  | | :----:
        | :-----: | :----: | :--: | :-: | |   No   |   n/a   |   No
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/justify-tracks.

    - left (string | number; optional):
        The **`left`** CSS property participates in specifying the
        horizontal position of a positioned element. It has no effect
        on non-positioned elements.  **Syntax**: `<length> |
        <percentage> | auto`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari |  Edge  |   IE    | | :----: | :-----: |
        :----: | :----: | :-----: | | **1**  |  **1**  | **1**  |
        **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/left.

    - letterSpacing (string | number; optional):
        The **`letter-spacing`** CSS property sets the horizontal
        spacing behavior between text characters. This value is added
        to the natural spacing between characters while rendering the
        text. Positive values of `letter-spacing` causes characters to
        spread farther apart, while negative values of
        `letter-spacing` bring characters closer together.
        **Syntax**: `normal | <length>`  **Initial value**: `normal`
        | Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/letter-spacing.

    - lightingColor (boolean | number | string | dict | list; optional)

    - lineBreak (a value equal to: 'loose', 'strict', 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'anywhere'; optional):
        The **`line-break`** CSS property sets how to break lines of
        Chinese, Japanese, or Korean (CJK) text when working with
        punctuation and symbols.  **Syntax**: `auto | loose | normal |
        strict | anywhere`  **Initial value**: `auto`  | Chrome  |
        Firefox | Safari  |  Edge  |   IE    | | :-----: | :-----: |
        :-----: | :----: | :-----: | | **58**  | **69**  | **11**  |
        **14** | **5.5** | | 1 _-x-_ |         | 3 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/line-break.

    - lineClamp (boolean | number | string | dict | list; optional):
        **Syntax**: `none | <integer>`  **Initial value**: `none`.

    - lineHeight (string | number; optional):
        The **`line-height`** CSS property sets the height of a line
        box. It's commonly used to set the distance between lines of
        text. On block-level elements, it specifies the minimum height
        of line boxes within the element. On non-replaced inline
        elements, it specifies the height that is used to calculate
        line box height.  **Syntax**: `normal | <number> | <length> |
        <percentage>`  **Initial value**: `normal`  | Chrome | Firefox
        | Safari |  Edge  |  IE   | | :----: | :-----: | :----: |
        :----: | :---: | | **1**  |  **1**  | **1**  | **12** | **4**
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/line-height.

    - lineHeightStep (string | number; optional):
        The **`line-height-step`** CSS property sets the step unit for
        line box heights. When the property is set, line box heights
        are rounded up to the closest multiple of the unit.
        **Syntax**: `<length>`  **Initial value**: `0`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | |  n/a   |   No    |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/line-height-step.

    - listStyle (boolean | number | string | dict | list; optional):
        The **`list-style`** CSS shorthand property allows you to set
        all the list style properties at once.  **Syntax**:
        `<'list-style-type'> || <'list-style-position'> ||
        <'list-style-image'>`  | Chrome | Firefox | Safari |  Edge  |
        IE   | | :----: | :-----: | :----: | :----: | :---: | | **1**
        |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/list-style.

    - listStyleImage (boolean | number | string | dict | list; optional):
        The **`list-style-image`** CSS property sets an image to be
        used as the list item marker.  **Syntax**: `<image> | none`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |  IE   | | :----: | :-----: | :----: | :----: | :---: | |
        **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/list-style-image.

    - listStylePosition (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'inside', 'outside'; optional):
        The **`list-style-position`** CSS property sets the position
        of the `::marker` relative to a list item.  **Syntax**:
        `inside | outside`  **Initial value**: `outside`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/list-style-position.

    - listStyleType (boolean | number | string | dict | list; optional):
        The **`list-style-type`** CSS property sets the marker (such
        as a disc, character, or custom counter style) of a list item
        element.  **Syntax**: `<counter-style> | <string> | none`
        **Initial value**: `disc`  | Chrome | Firefox | Safari |  Edge
        |  IE   | | :----: | :-----: | :----: | :----: | :---: | |
        **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/list-style-type.

    - margin (string | number; optional):
        The **`margin`** CSS shorthand property sets the margin area
        on all four sides of an element.  **Syntax**: `[ <length> |
        <percentage> | auto ]{1,4}`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin.

    - marginBlock (string | number; optional):
        The **`margin-block`** CSS shorthand property defines the
        logical block start and end margins of an element, which maps
        to physical margins depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'margin-left'>{1,2}`  | Chrome | Firefox |  Safari  | Edge |
        IE  | | :----: | :-----: | :------: | :--: | :-: | | **87** |
        **66**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-block.

    - marginBlockEnd (string | number; optional):
        The **`margin-block-end`** CSS property defines the logical
        block end margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'margin-left'>`  **Initial value**: `0`  | Chrome | Firefox
        |  Safari  | Edge | IE  | | :----: | :-----: | :------: | :--:
        | :-: | | **69** | **41**  | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-block-end.

    - marginBlockStart (string | number; optional):
        The **`margin-block-start`** CSS property defines the logical
        block start margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'margin-left'>`  **Initial value**: `0`  | Chrome | Firefox
        |  Safari  | Edge | IE  | | :----: | :-----: | :------: | :--:
        | :-: | | **69** | **41**  | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-block-start.

    - marginBottom (string | number; optional):
        The **`margin-bottom`** CSS property sets the margin area on
        the bottom of an element. A positive value places it farther
        from its neighbors, while a negative value places it closer.
        **Syntax**: `<length> | <percentage> | auto`  **Initial
        value**: `0`  | Chrome | Firefox | Safari |  Edge  |  IE   | |
        :----: | :-----: | :----: | :----: | :---: | | **1**  |  **1**
        | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-bottom.

    - marginInline (string | number; optional):
        The **`margin-inline`** CSS shorthand property is a shorthand
        property that defines both the logical inline start and end
        margins of an element, which maps to physical margins
        depending on the element's writing mode, directionality, and
        text orientation.  **Syntax**: `<'margin-left'>{1,2}`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **87** | **66**  | **14.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-inline.

    - marginInlineEnd (string | number; optional):
        The **`margin-inline-end`** CSS property defines the logical
        inline end margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation. In other words, it
        corresponds to the `margin-top`, `margin-right`,
        `margin-bottom` or `margin-left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'margin-left'>`  **Initial
        value**: `0`  |          Chrome          |        Firefox
        |          Safari          | Edge | IE  | |
        :----------------------: | :-------------------: |
        :----------------------: | :--: | :-: | |          **69**
        |        **41**         |         **12.1**         | n/a  | No
        | | 2 _(-webkit-margin-end)_ | 3 _(-moz-margin-end)_ | 3
        _(-webkit-margin-end)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-inline-end.

    - marginInlineStart (string | number; optional):
        The **`margin-inline-start`** CSS property defines the logical
        inline start margin of an element, which maps to a physical
        margin depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `margin-top`, `margin-right`, `margin-bottom`, or
        `margin-left` property depending on the values defined for
        `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'margin-left'>`  **Initial value**: `0`  |
        Chrome           |         Firefox         |           Safari
        | Edge | IE  | | :------------------------: |
        :---------------------: | :------------------------: | :--: |
        :-: | |           **69**           |         **41**          |
        **12.1**          | n/a  | No  | | 2 _(-webkit-margin-start)_
        | 3 _(-moz-margin-start)_ | 3 _(-webkit-margin-start)_ |
        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-inline-start.

    - marginLeft (string | number; optional):
        The **`margin-left`** CSS property sets the margin area on the
        left side of an element. A positive value places it farther
        from its neighbors, while a negative value places it closer.
        **Syntax**: `<length> | <percentage> | auto`  **Initial
        value**: `0`  | Chrome | Firefox | Safari |  Edge  |  IE   | |
        :----: | :-----: | :----: | :----: | :---: | | **1**  |  **1**
        | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-left.

    - marginRight (string | number; optional):
        The **`margin-right`** CSS property sets the margin area on
        the right side of an element. A positive value places it
        farther from its neighbors, while a negative value places it
        closer.  **Syntax**: `<length> | <percentage> | auto`
        **Initial value**: `0`  | Chrome | Firefox | Safari |  Edge  |
        IE   | | :----: | :-----: | :----: | :----: | :---: | | **1**
        |  **1**  | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-right.

    - marginTop (string | number; optional):
        The **`margin-top`** CSS property sets the margin area on the
        top of an element. A positive value places it farther from its
        neighbors, while a negative value places it closer.
        **Syntax**: `<length> | <percentage> | auto`  **Initial
        value**: `0`  | Chrome | Firefox | Safari |  Edge  |  IE   | |
        :----: | :-----: | :----: | :----: | :---: | | **1**  |  **1**
        | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-top.

    - marginTrim (a value equal to: 'inherit', 'none', 'all', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'in-flow'; optional):
        The `margin-trim` property allows the container to trim the
        margins of its children where they adjoin the container's
        edges.  **Syntax**: `none | in-flow | all`  **Initial value**:
        `none`  | Chrome | Firefox |  Safari  | Edge | IE  | | :----:
        | :-----: | :------: | :--: | :-: | |   No   |   No    |
        **16.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/margin-trim.

    - marker (boolean | number | string | dict | list; optional)

    - markerEnd (boolean | number | string | dict | list; optional)

    - markerMid (boolean | number | string | dict | list; optional)

    - markerStart (boolean | number | string | dict | list; optional)

    - mask (string | number; optional):
        The **`mask`** CSS shorthand property hides an element
        (partially or fully) by masking or clipping the image at
        specific points.  **Syntax**: `<mask-layer>#`  | Chrome |
        Firefox |  Safari   | Edge  | IE  | | :----: | :-----: |
        :-------: | :---: | :-: | | **1**  | **53**  | **15.4**  |
        12-79 | No  | |        |         | 3.1 _-x-_ |       |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask.

    - maskBorder (boolean | number | string | dict | list; optional):
        The **`mask-border`** CSS shorthand property lets you create a
        mask along the edge of an element's border.  **Syntax**:
        `<'mask-border-source'> || <'mask-border-slice'> [ /
        <'mask-border-width'>? [ / <'mask-border-outset'> ]? ]? ||
        <'mask-border-repeat'> || <'mask-border-mode'>`  |
        Chrome              | Firefox |             Safari
        | Edge | IE  | | :------------------------------: | :-----: |
        :----------------------------: | :--: | :-: | | **1**
        _(-webkit-mask-box-image)_ |   No    |            **17.2**
        | n/a  | No  | |                                  |         |
        3.1 _(-webkit-mask-box-image)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-border.

    - maskBorderMode (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'alpha', 'luminance'; optional):
        The **`mask-border-mode`** CSS property specifies the blending
        mode used in a mask border.  **Syntax**: `luminance | alpha`
        **Initial value**: `alpha`.

    - maskBorderOutset (string | number; optional):
        The **`mask-border-outset`** CSS property specifies the
        distance by which an element's mask border is set out from its
        border box.  **Syntax**: `[ <length> | <number> ]{1,4}`
        **Initial value**: `0`  |                 Chrome
        | Firefox |                Safari                 | Edge | IE
        | | :-------------------------------------: | :-----: |
        :-----------------------------------: | :--: | :-: | | **1**
        _(-webkit-mask-box-image-outset)_ |   No    |
        **17.2**                | n/a  | No  | |
        |         | 3.1 _(-webkit-mask-box-image-outset)_ |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-border-outset.

    - maskBorderRepeat (boolean | number | string | dict | list; optional):
        The **`mask-border-repeat`** CSS property sets how the edge
        regions of a source image are adjusted to fit the dimensions
        of an element's mask border.  **Syntax**: `[ stretch | repeat
        | round | space ]{1,2}`  **Initial value**: `stretch`  |
        Chrome                  | Firefox |                Safari
        | Edge | IE  | | :-------------------------------------: |
        :-----: | :-----------------------------------: | :--: | :-: |
        | **1** _(-webkit-mask-box-image-repeat)_ |   No    |
        **17.2**                | n/a  | No  | |
        |         | 3.1 _(-webkit-mask-box-image-repeat)_ |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-border-repeat.

    - maskBorderSlice (boolean | number | string | dict | list; optional):
        The **`mask-border-slice`** CSS property divides the image set
        by `mask-border-source` into regions. These regions are used
        to form the components of an element's mask border.
        **Syntax**: `<number-percentage>{1,4} fill?`  **Initial
        value**: `0`  |                 Chrome                 |
        Firefox |                Safari                | Edge | IE  |
        | :------------------------------------: | :-----: |
        :----------------------------------: | :--: | :-: | | **1**
        _(-webkit-mask-box-image-slice)_ |   No    |
        **17.2**               | n/a  | No  | |
        |         | 3.1 _(-webkit-mask-box-image-slice)_ |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-border-slice.

    - maskBorderSource (boolean | number | string | dict | list; optional):
        The **`mask-border-source`** CSS property sets the source
        image used to create an element's mask border.  **Syntax**:
        `none | <image>`  **Initial value**: `none`  |
        Chrome                  | Firefox |                Safari
        | Edge | IE  | | :-------------------------------------: |
        :-----: | :-----------------------------------: | :--: | :-: |
        | **1** _(-webkit-mask-box-image-source)_ |   No    |
        **17.2**                | n/a  | No  | |
        |         | 3.1 _(-webkit-mask-box-image-source)_ |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-border-source.

    - maskBorderWidth (string | number; optional):
        The **`mask-border-width`** CSS property sets the width of an
        element's mask border.  **Syntax**: `[ <length-percentage> |
        <number> | auto ]{1,4}`  **Initial value**: `auto`  |
        Chrome                 | Firefox |                Safari
        | Edge | IE  | | :------------------------------------: |
        :-----: | :----------------------------------: | :--: | :-: |
        | **1** _(-webkit-mask-box-image-width)_ |   No    |
        **17.2**               | n/a  | No  | |
        |         | 3.1 _(-webkit-mask-box-image-width)_ |      |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-border-width.

    - maskClip (boolean | number | string | dict | list; optional):
        The **`mask-clip`** CSS property determines the area which is
        affected by a mask. The painted content of an element must be
        restricted to this area.  **Syntax**: `[ <geometry-box> |
        no-clip ]#`  **Initial value**: `border-box`  | Chrome  |
        Firefox |  Safari  | Edge | IE  | | :-----: | :-----: |
        :------: | :--: | :-: | | **120** | **53**  | **15.4** | n/a
        | No  | | 1 _-x-_ |         | 4 _-x-_  |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-clip.

    - maskComposite (boolean | number | string | dict | list; optional):
        The **`mask-composite`** CSS property represents a compositing
        operation used on the current mask layer with the mask layers
        below it.  **Syntax**: `<compositing-operator>#`  **Initial
        value**: `add`  | Chrome  | Firefox |  Safari  | Edge  | IE  |
        | :-----: | :-----: | :------: | :---: | :-: | | **120** |
        **53**  | **15.4** | 18-79 | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-composite.

    - maskImage (boolean | number | string | dict | list; optional):
        The **`mask-image`** CSS property sets the image that is used
        as mask layer for an element. By default this means the alpha
        channel of the mask image will be multiplied with the alpha
        channel of the element. This can be controlled with the
        `mask-mode` property.  **Syntax**: `<mask-reference>#`
        **Initial value**: `none`  | Chrome  | Firefox |  Safari  |
        Edge  | IE  | | :-----: | :-----: | :------: | :---: | :-: | |
        **120** | **53**  | **15.4** | 16-79 | No  | | 1 _-x-_ |
        | 4 _-x-_  |       |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-image.

    - maskMode (boolean | number | string | dict | list; optional):
        The **`mask-mode`** CSS property sets whether the mask
        reference defined by `mask-image` is treated as a luminance or
        alpha mask.  **Syntax**: `<masking-mode>#`  **Initial value**:
        `match-source`  | Chrome  | Firefox |  Safari  | Edge | IE  |
        | :-----: | :-----: | :------: | :--: | :-: | | **120** |
        **53**  | **15.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-mode.

    - maskOrigin (boolean | number | string | dict | list; optional):
        The **`mask-origin`** CSS property sets the origin of a mask.
        **Syntax**: `<geometry-box>#`  **Initial value**: `border-box`
        | Chrome  | Firefox |  Safari  | Edge | IE  | | :-----: |
        :-----: | :------: | :--: | :-: | | **120** | **53**  |
        **15.4** | n/a  | No  | | 1 _-x-_ |         | 4 _-x-_  |
        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-origin.

    - maskPosition (string | number; optional):
        The **`mask-position`** CSS property sets the initial
        position, relative to the mask position layer set by
        `mask-origin`, for each defined mask image.  **Syntax**:
        `<position>#`  **Initial value**: `center`  | Chrome  |
        Firefox |  Safari   | Edge  | IE  | | :-----: | :-----: |
        :-------: | :---: | :-: | | **120** | **53**  | **15.4**  |
        18-79 | No  | | 1 _-x-_ |         | 3.1 _-x-_ |       |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-position.

    - maskRepeat (boolean | number | string | dict | list; optional):
        The **`mask-repeat`** CSS property sets how mask images are
        repeated. A mask image can be repeated along the horizontal
        axis, the vertical axis, both axes, or not repeated at all.
        **Syntax**: `<repeat-style>#`  **Initial value**: `repeat`  |
        Chrome  | Firefox |  Safari   | Edge  | IE  | | :-----: |
        :-----: | :-------: | :---: | :-: | | **120** | **53**  |
        **15.4**  | 18-79 | No  | | 1 _-x-_ |         | 3.1 _-x-_ |
        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-repeat.

    - maskSize (string | number; optional):
        The **`mask-size`** CSS property specifies the sizes of the
        mask images. The size of the image can be fully or partially
        constrained in order to preserve its intrinsic ratio.
        **Syntax**: `<bg-size>#`  **Initial value**: `auto`  | Chrome
        | Firefox |  Safari  | Edge  | IE  | | :-----: | :-----: |
        :------: | :---: | :-: | | **120** | **53**  | **15.4** |
        18-79 | No  | | 4 _-x-_ |         | 4 _-x-_  |       |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-size.

    - maskType (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'alpha', 'luminance'; optional):
        The **`mask-type`** CSS property sets whether an SVG `<mask>`
        element is used as a _luminance_ or an _alpha_ mask. It
        applies to the `<mask>` element itself.  **Syntax**:
        `luminance | alpha`  **Initial value**: `luminance`  | Chrome
        | Firefox | Safari | Edge | IE  | | :----: | :-----: | :----:
        | :--: | :-: | | **24** | **35**  | **7**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mask-type.

    - masonryAutoFlow (boolean | number | string | dict | list; optional):
        This feature is not Baseline because it does not work in some
        of the most widely-used browsers.  **Syntax**: `[ pack | next
        ] || [ definite-first | ordered ]`  **Initial value**: `pack`
        | Chrome | Firefox |   Safari    | Edge | IE  | | :----: |
        :-----: | :---------: | :--: | :-: | |   No   |   No    |
        **preview** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/masonry-auto-flow.

    - mathDepth (boolean | number | string | dict | list; optional):
        The **`math-depth`** property describes a notion of _depth_
        for each element of a mathematical formula, with respect to
        the top-level container of that formula. Concretely, this is
        used to determine the computed value of the font-size property
        when its specified value is `math`.  **Syntax**: `auto-add |
        add(<integer>) | <integer>`  **Initial value**: `0`  | Chrome
        | Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----:
        | :--: | :-: | | **109** | **117** |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/math-depth.

    - mathShift (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'compact'; optional):
        The `math-shift` property indicates whether superscripts
        inside MathML formulas should be raised by a normal or compact
        shift.  **Syntax**: `normal | compact`  **Initial value**:
        `normal`  | Chrome  | Firefox | Safari | Edge | IE  | |
        :-----: | :-----: | :----: | :--: | :-: | | **109** |   No
        |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/math-shift.

    - mathStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'compact'; optional):
        The `math-style` property indicates whether MathML equations
        should render with normal or compact height.  **Syntax**:
        `normal | compact`  **Initial value**: `normal`  | Chrome  |
        Firefox |  Safari  | Edge | IE  | | :-----: | :-----: |
        :------: | :--: | :-: | | **109** | **117** | **14.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/math-style.

    - maxBlockSize (string | number; optional):
        The **`max-block-size`** CSS property specifies the maximum
        size of an element in the direction opposite that of the
        writing direction as specified by `writing-mode`. That is, if
        the writing direction is horizontal, then `max-block-size` is
        equivalent to `max-height`; if the writing direction is
        vertical, `max-block-size` is the same as `max-width`.
        **Syntax**: `<'max-width'>`  **Initial value**: `none`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **57** | **41**  | **12.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/max-block-size.

    - maxHeight (string | number; optional):
        The **`max-height`** CSS property sets the maximum height of
        an element. It prevents the used value of the `height`
        property from becoming larger than the value specified for
        `max-height`.  **Syntax**: `none | <length-percentage> |
        min-content | max-content | fit-content |
        fit-content(<length-percentage>)`  **Initial value**: `none`
        | Chrome | Firefox | Safari  |  Edge  |  IE   | | :----: |
        :-----: | :-----: | :----: | :---: | | **18** |  **1**  |
        **1.3** | **12** | **7** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/max-height.

    - maxInlineSize (string | number; optional):
        The **`max-inline-size`** CSS property defines the horizontal
        or vertical maximum size of an element's block, depending on
        its writing mode. It corresponds to either the `max-width` or
        the `max-height` property, depending on the value of
        `writing-mode`.  **Syntax**: `<'max-width'>`  **Initial
        value**: `none`  | Chrome | Firefox |   Safari   | Edge | IE
        | | :----: | :-----: | :--------: | :--: | :-: | | **57** |
        **41**  |  **12.1**  | n/a  | No  | |        |         | 10.1
        _-x-_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/max-inline-size.

    - maxLines (boolean | number | string | dict | list; optional):
        **Syntax**: `none | <integer>`  **Initial value**: `none`.

    - maxWidth (string | number; optional):
        The **`max-width`** CSS property sets the maximum width of an
        element. It prevents the used value of the `width` property
        from becoming larger than the value specified by `max-width`.
        **Syntax**: `none | <length-percentage> | min-content |
        max-content | fit-content | fit-content(<length-percentage>)`
        **Initial value**: `none`  | Chrome | Firefox | Safari |  Edge
        |  IE   | | :----: | :-----: | :----: | :----: | :---: | |
        **1**  |  **1**  | **1**  | **12** | **7** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/max-width.

    - minBlockSize (string | number; optional):
        The **`min-block-size`** CSS property defines the minimum
        horizontal or vertical size of an element's block, depending
        on its writing mode. It corresponds to either the `min-width`
        or the `min-height` property, depending on the value of
        `writing-mode`.  **Syntax**: `<'min-width'>`  **Initial
        value**: `0`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **57** | **41**
        | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/min-block-size.

    - minHeight (string | number; optional):
        The **`min-height`** CSS property sets the minimum height of
        an element. It prevents the used value of the `height`
        property from becoming smaller than the value specified for
        `min-height`.  **Syntax**: `auto | <length> | <percentage> |
        min-content | max-content | fit-content |
        fit-content(<length-percentage>)`  **Initial value**: `auto`
        | Chrome | Firefox | Safari  |  Edge  |  IE   | | :----: |
        :-----: | :-----: | :----: | :---: | | **1**  |  **3**  |
        **1.3** | **12** | **7** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/min-height.

    - minInlineSize (string | number; optional):
        The **`min-inline-size`** CSS property defines the horizontal
        or vertical minimal size of an element's block, depending on
        its writing mode. It corresponds to either the `min-width` or
        the `min-height` property, depending on the value of
        `writing-mode`.  **Syntax**: `<'min-width'>`  **Initial
        value**: `0`  | Chrome | Firefox |  Safari  | Edge | IE  | |
        :----: | :-----: | :------: | :--: | :-: | | **57** | **41**
        | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/min-inline-size.

    - minWidth (string | number; optional):
        The **`min-width`** CSS property sets the minimum width of an
        element. It prevents the used value of the `width` property
        from becoming smaller than the value specified for
        `min-width`.  **Syntax**: `auto | <length> | <percentage> |
        min-content | max-content | fit-content |
        fit-content(<length-percentage>)`  **Initial value**: `auto`
        | Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **7** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/min-width.

    - mixBlendMode (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'color', 'color-burn', 'color-dodge', 'darken', 'difference', 'exclusion', 'hard-light', 'hue', 'lighten', 'luminosity', 'multiply', 'overlay', 'saturation', 'screen', 'soft-light', 'plus-lighter'; optional):
        The **`mix-blend-mode`** CSS property sets how an element's
        content should blend with the content of the element's parent
        and the element's background.  **Syntax**: `<blend-mode> |
        plus-lighter`  **Initial value**: `normal`  | Chrome | Firefox
        | Safari | Edge | IE  | | :----: | :-----: | :----: | :--: |
        :-: | | **41** | **32**  | **8**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/mix-blend-mode.

    - motion (string | number; optional):
        The **`offset`** CSS shorthand property sets all the
        properties required for animating an element along a defined
        path.  **Syntax**: `[ <'offset-position'>? [ <'offset-path'> [
        <'offset-distance'> || <'offset-rotate'> ]? ]? ]! [ /
        <'offset-anchor'> ]?`  |    Chrome     | Firefox | Safari |
        Edge | IE  | | :-----------: | :-----: | :----: | :--: | :-: |
        |    **55**     | **72**  | **16** | n/a  | No  | | 46
        _(motion)_ |         |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset.

    - motionDistance (string | number; optional):
        The **`offset-distance`** CSS property specifies a position
        along an `offset-path` for an element to be placed.
        **Syntax**: `<length-percentage>`  **Initial value**: `0`  |
        Chrome         | Firefox | Safari | Edge | IE  | |
        :--------------------: | :-----: | :----: | :--: | :-: | |
        **55**         | **72**  | **16** | n/a  | No  | | 46
        _(motion-distance)_ |         |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-distance.

    - motionPath (boolean | number | string | dict | list; optional):
        The **`offset-path`** CSS property specifies a motion path for
        an element to follow and defines the element's positioning
        within the parent container or SVG coordinate system.
        **Syntax**: `none | <offset-path> || <coord-box>`  **Initial
        value**: `none`  |       Chrome       | Firefox |  Safari  |
        Edge | IE  | | :----------------: | :-----: | :------: | :--:
        | :-: | |       **55**       | **72**  | **15.4** | n/a  | No
        | | 46 _(motion-path)_ |         |          |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-path.

    - motionRotation (boolean | number | string | dict | list; optional):
        The **`offset-rotate`** CSS property defines the
        orientation/direction of the element as it is positioned along
        the `offset-path`.  **Syntax**: `[ auto | reverse ] ||
        <angle>`  **Initial value**: `auto`  |         Chrome
        | Firefox | Safari | Edge | IE  | | :--------------------: |
        :-----: | :----: | :--: | :-: | |         **56**         |
        **72**  | **16** | n/a  | No  | | 46 _(motion-rotation)_ |
        |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-rotate.

    - msAccelerator (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'false', 'true'; optional):
        The **`-ms-accelerator`** CSS property is a Microsoft
        extension that sets or retrieves a string indicating whether
        the object represents a keyboard shortcut.  **Syntax**: `False
        | True`  **Initial value**: `False`.

    - msBlockProgression (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'bt', 'lr', 'rl', 'tb'; optional):
        The **`-ms-block-progression`** CSS property is a Microsoft
        extension that specifies the block progression and layout
        orientation.  **Syntax**: `tb | rl | bt | lr`  **Initial
        value**: `tb`.

    - msContentZoomChaining (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'chained'; optional):
        The **`-ms-content-zoom-chaining`** CSS property is a
        Microsoft extension specifying the zoom behavior that occurs
        when a user hits the zoom limit during page manipulation.
        **Syntax**: `none | chained`  **Initial value**: `none`.

    - msContentZoomLimit (boolean | number | string | dict | list; optional):
        The **`-ms-content-zoom-limit`** CSS shorthand property is a
        Microsoft extension that specifies values for the
        `-ms-content-zoom-limit-min` and `-ms-content-zoom-limit-max`
        properties.  **Syntax**: `<'-ms-content-zoom-limit-min'>
        <'-ms-content-zoom-limit-max'>`.

    - msContentZoomLimitMax (boolean | number | string | dict | list; optional):
        The **`-ms-content-zoom-limit-max`** CSS property is a
        Microsoft extension that specifies the selected elements'
        maximum zoom factor.  **Syntax**: `<percentage>`  **Initial
        value**: `400%`.

    - msContentZoomLimitMin (boolean | number | string | dict | list; optional):
        The **`-ms-content-zoom-limit-min`** CSS property is a
        Microsoft extension that specifies the minimum zoom factor.
        **Syntax**: `<percentage>`  **Initial value**: `100%`.

    - msContentZoomSnap (boolean | number | string | dict | list; optional):
        The **`-ms-content-zoom-snap`** CSS shorthand property is a
        Microsoft extension that specifies values for the
        `-ms-content-zoom-snap-type` and
        `-ms-content-zoom-snap-points` properties.  **Syntax**:
        `<'-ms-content-zoom-snap-type'> ||
        <'-ms-content-zoom-snap-points'>`.

    - msContentZoomSnapPoints (boolean | number | string | dict | list; optional):
        The **`-ms-content-zoom-snap-points`** CSS property is a
        Microsoft extension that specifies where zoom snap-points are
        located.  **Syntax**: `snapInterval( <percentage>,
        <percentage> ) | snapList( <percentage># )`  **Initial
        value**: `snapInterval(0%, 100%)`.

    - msContentZoomSnapType (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'mandatory', 'proximity'; optional):
        The **`-ms-content-zoom-snap-type`** CSS property is a
        Microsoft extension that specifies how zooming is affected by
        defined snap-points.  **Syntax**: `none | proximity |
        mandatory`  **Initial value**: `none`.

    - msContentZooming (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'zoom'; optional):
        The **`-ms-content-zooming`** CSS property is a Microsoft
        extension that specifies whether zooming is enabled.
        **Syntax**: `none | zoom`  **Initial value**: zoom for the top
        level element, none for all other elements.

    - msFilter (boolean | number | string | dict | list; optional):
        The `-ms-filter` CSS property is a Microsoft extension that
        sets or retrieves the filter or collection of filters applied
        to an object.  **Syntax**: `<string>`  **Initial value**: \"\"
        (the empty string).

    - msFlex (string | number; optional):
        The **`flex`** CSS shorthand property sets how a flex _item_
        will grow or shrink to fit the space available in its flex
        container.  **Syntax**: `none | [ <'flex-grow'>
        <'flex-shrink'>? || <'flex-basis'> ]`.

    - msFlexDirection (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'column', 'column-reverse', 'row', 'row-reverse'; optional):
        The **`flex-direction`** CSS property sets how flex items are
        placed in the flex container defining the main axis and the
        direction (normal or reversed).  **Syntax**: `row |
        row-reverse | column | column-reverse`  **Initial value**:
        `row`.

    - msFlexPositive (boolean | number | string | dict | list; optional):
        The **`flex-grow`** CSS property sets the flex grow factor of
        a flex item's main size.  **Syntax**: `<number>`  **Initial
        value**: `0`.

    - msFlowFrom (boolean | number | string | dict | list; optional):
        The **`-ms-flow-from`** CSS property is a Microsoft extension
        that gets or sets a value identifying a region container in
        the document that accepts the content flow from the data
        source.  **Syntax**: `[ none | <custom-ident> ]#`  **Initial
        value**: `none`.

    - msFlowInto (boolean | number | string | dict | list; optional):
        The **`-ms-flow-into`** CSS property is a Microsoft extension
        that gets or sets a value identifying an iframe container in
        the document that serves as the region's data source.
        **Syntax**: `[ none | <custom-ident> ]#`  **Initial value**:
        `none`.

    - msGridColumns (string | number; optional):
        The **`grid-template-columns`** CSS property defines the line
        names and track sizing functions of the grid columns.
        **Syntax**: `none | <track-list> | <auto-track-list>`
        **Initial value**: `none`.

    - msGridRows (string | number; optional):
        The **`grid-template-rows`** CSS property defines the line
        names and track sizing functions of the grid rows.
        **Syntax**: `none | <track-list> | <auto-track-list>`
        **Initial value**: `none`.

    - msHighContrastAdjust (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`-ms-high-contrast-adjust`** CSS property is a Microsoft
        extension that gets or sets a value indicating whether to
        override any CSS properties that would have been set in high
        contrast mode.  **Syntax**: `auto | none`  **Initial value**:
        `auto`.

    - msHyphenateLimitChars (boolean | number | string | dict | list; optional):
        The **`-ms-hyphenate-limit-chars`** CSS property is a
        Microsoft extension that specifies one to three values
        indicating the minimum number of characters in a hyphenated
        word. If the word does not meet the required minimum number of
        characters in the word, before the hyphen, or after the
        hyphen, then the word is not hyphenated.  **Syntax**: `auto |
        <integer>{1,3}`  **Initial value**: `auto`.

    - msHyphenateLimitLines (boolean | number | string | dict | list; optional):
        The **`-ms-hyphenate-limit-lines`** CSS property is a
        Microsoft extension specifying the maximum number of
        consecutive lines in an element that may be ended with a
        hyphenated word.  **Syntax**: `no-limit | <integer>`
        **Initial value**: `no-limit`.

    - msHyphenateLimitZone (string | number; optional):
        The `**-ms-hyphenate-limit-zone**` CSS property is a Microsoft
        extension specifying the width of the hyphenation zone.
        **Syntax**: `<percentage> | <length>`  **Initial value**: `0`.

    - msHyphens (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'manual'; optional):
        The **`hyphens`** CSS property specifies how words should be
        hyphenated when text wraps across multiple lines. It can
        prevent hyphenation entirely, hyphenate at manually-specified
        points within the text, or let the browser automatically
        insert hyphens where appropriate.  **Syntax**: `none | manual
        | auto`  **Initial value**: `manual`.

    - msImeAlign (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'after'; optional):
        The **`-ms-ime-align`** CSS property is a Microsoft extension
        aligning the Input Method Editor (IME) candidate window box
        relative to the element on which the IME composition is
        active. The extension is implemented in Microsoft Edge and
        Internet Explorer 11.  **Syntax**: `auto | after`  **Initial
        value**: `auto`.

    - msImeMode (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'active', 'disabled', 'inactive'; optional):
        The **`ime-mode`** CSS property controls the state of the
        input method editor (IME) for text fields. This property is
        obsolete.  **Syntax**: `auto | normal | active | inactive |
        disabled`  **Initial value**: `auto` @,deprecated.

    - msLineBreak (a value equal to: 'loose', 'strict', 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'anywhere'; optional):
        The **`line-break`** CSS property sets how to break lines of
        Chinese, Japanese, or Korean (CJK) text when working with
        punctuation and symbols.  **Syntax**: `auto | loose | normal |
        strict | anywhere`  **Initial value**: `auto`.

    - msOrder (boolean | number | string | dict | list; optional):
        The **`order`** CSS property sets the order to lay out an item
        in a flex or grid container. Items in a container are sorted
        by ascending `order` value and then by their source code
        order.  **Syntax**: `<integer>`  **Initial value**: `0`.

    - msOverflowStyle (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', '-ms-autohiding-scrollbar', 'scrollbar'; optional):
        The **`-ms-overflow-style`** CSS property is a Microsoft
        extension controlling the behavior of scrollbars when the
        content of an element overflows.  **Syntax**: `auto | none |
        scrollbar | -ms-autohiding-scrollbar`  **Initial value**:
        `auto`.

    - msOverflowX (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'scroll', 'clip', '-moz-hidden-unscrollable'; optional):
        The **`overflow-x`** CSS property sets what shows when content
        overflows a block-level element's left and right edges. This
        may be nothing, a scroll bar, or the overflow content.
        **Syntax**: `visible | hidden | clip | scroll | auto`
        **Initial value**: `visible`.

    - msOverflowY (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'scroll', 'clip', '-moz-hidden-unscrollable'; optional):
        The **`overflow-y`** CSS property sets what shows when content
        overflows a block-level element's top and bottom edges. This
        may be nothing, a scroll bar, or the overflow content.
        **Syntax**: `visible | hidden | clip | scroll | auto`
        **Initial value**: `visible`.

    - msScrollChaining (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'chained'; optional):
        The `**-ms-scroll-chaining**` CSS property is a Microsoft
        extension that specifies the scrolling behavior that occurs
        when a user hits the scroll limit during a manipulation.
        **Syntax**: `chained | none`  **Initial value**: `chained`.

    - msScrollLimit (boolean | number | string | dict | list; optional):
        The **\-ms-scroll-limit** CSS property is a Microsoft
        extension that specifies values for the
        `-ms-scroll-limit-x-min`, `-ms-scroll-limit-y-min`,
        `-ms-scroll-limit-x-max`, and `-ms-scroll-limit-y-max`
        properties.  **Syntax**: `<'-ms-scroll-limit-x-min'>
        <'-ms-scroll-limit-y-min'> <'-ms-scroll-limit-x-max'>
        <'-ms-scroll-limit-y-max'>`.

    - msScrollLimitXMax (string | number; optional):
        The `**-ms-scroll-limit-x-max**` CSS property is a Microsoft
        extension that specifies the maximum value for the
        `Element.scrollLeft` property.  **Syntax**: `auto | <length>`
        **Initial value**: `auto`.

    - msScrollLimitXMin (string | number; optional):
        The **`-ms-scroll-limit-x-min`** CSS property is a Microsoft
        extension that specifies the minimum value for the
        `Element.scrollLeft` property.  **Syntax**: `<length>`
        **Initial value**: `0`.

    - msScrollLimitYMax (string | number; optional):
        The **`-ms-scroll-limit-y-max`** CSS property is a Microsoft
        extension that specifies the maximum value for the
        `Element.scrollTop` property.  **Syntax**: `auto | <length>`
        **Initial value**: `auto`.

    - msScrollLimitYMin (string | number; optional):
        The **`-ms-scroll-limit-y-min`** CSS property is a Microsoft
        extension that specifies the minimum value for the
        `Element.scrollTop` property.  **Syntax**: `<length>`
        **Initial value**: `0`.

    - msScrollRails (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'railed'; optional):
        The **`-ms-scroll-rails`** CSS property is a Microsoft
        extension that specifies whether scrolling locks to the
        primary axis of motion.  **Syntax**: `none | railed`
        **Initial value**: `railed`.

    - msScrollSnapPointsX (boolean | number | string | dict | list; optional):
        The **`-ms-scroll-snap-points-x`** CSS property is a Microsoft
        extension that specifies where snap-points will be located
        along the x-axis.  **Syntax**: `snapInterval(
        <length-percentage>, <length-percentage> ) | snapList(
        <length-percentage># )`  **Initial value**: `snapInterval(0px,
        100%)`.

    - msScrollSnapPointsY (boolean | number | string | dict | list; optional):
        The **`-ms-scroll-snap-points-y`** CSS property is a Microsoft
        extension that specifies where snap-points will be located
        along the y-axis.  **Syntax**: `snapInterval(
        <length-percentage>, <length-percentage> ) | snapList(
        <length-percentage># )`  **Initial value**: `snapInterval(0px,
        100%)`.

    - msScrollSnapType (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'mandatory', 'proximity'; optional):
        The **`scroll-snap-type`** CSS property sets how strictly snap
        points are enforced on the scroll container in case there is
        one.  **Syntax**: `none | proximity | mandatory`  **Initial
        value**: `none`.

    - msScrollSnapX (boolean | number | string | dict | list; optional):
        The **`-ms-scroll-snap-x`** CSS shorthand property is a
        Microsoft extension that specifies values for the
        `-ms-scroll-snap-type` and `-ms-scroll-snap-points-x`
        properties.  **Syntax**: `<'-ms-scroll-snap-type'>
        <'-ms-scroll-snap-points-x'>`.

    - msScrollSnapY (boolean | number | string | dict | list; optional):
        The **`-ms-scroll-snap-x`** CSS shorthand property is a
        Microsoft extension that specifies values for the
        `-ms-scroll-snap-type` and `-ms-scroll-snap-points-y`
        properties.  **Syntax**: `<'-ms-scroll-snap-type'>
        <'-ms-scroll-snap-points-y'>`.

    - msScrollTranslation (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'vertical-to-horizontal'; optional):
        The **`-ms-scroll-translation`** CSS property is a Microsoft
        extension that specifies whether vertical-to-horizontal scroll
        wheel translation occurs on the specified element.
        **Syntax**: `none | vertical-to-horizontal`  **Initial
        value**: `none`.

    - msScrollbar3dlightColor (boolean | number | string | dict | list; optional):
        The **`-ms-scrollbar-3dlight-color`** CSS property is a
        Microsoft extension specifying the color of the top and left
        edges of the scroll box and scroll arrows of a scroll bar.
        **Syntax**: `<color>`  **Initial value**: depends on user
        agent.

    - msScrollbarArrowColor (boolean | number | string | dict | list; optional):
        The **`-ms-scrollbar-arrow-color`** CSS property is a
        Microsoft extension that specifies the color of the arrow
        elements of a scroll arrow.  **Syntax**: `<color>`  **Initial
        value**: `ButtonText`.

    - msScrollbarBaseColor (boolean | number | string | dict | list; optional):
        The `**-ms-scrollbar-base-color**` CSS property is a Microsoft
        extension that specifies the base color of the main elements
        of a scroll bar.  **Syntax**: `<color>`  **Initial value**:
        depends on user agent.

    - msScrollbarDarkshadowColor (boolean | number | string | dict | list; optional):
        The **`-ms-scrollbar-darkshadow-color`** CSS property is a
        Microsoft extension that specifies the color of a scroll bar's
        gutter.  **Syntax**: `<color>`  **Initial value**:
        `ThreeDDarkShadow`.

    - msScrollbarFaceColor (boolean | number | string | dict | list; optional):
        The `**-ms-scrollbar-face-color**` CSS property is a Microsoft
        extension that specifies the color of the scroll box and
        scroll arrows of a scroll bar.  **Syntax**: `<color>`
        **Initial value**: `ThreeDFace`.

    - msScrollbarHighlightColor (boolean | number | string | dict | list; optional):
        The `**-ms-scrollbar-highlight-color**` CSS property is a
        Microsoft extension that specifies the color of the slider
        tray, the top and left edges of the scroll box, and the scroll
        arrows of a scroll bar.  **Syntax**: `<color>`  **Initial
        value**: `ThreeDHighlight`.

    - msScrollbarShadowColor (boolean | number | string | dict | list; optional):
        The **`-ms-scrollbar-shadow-color`** CSS property is a
        Microsoft extension that specifies the color of the bottom and
        right edges of the scroll box and scroll arrows of a scroll
        bar.  **Syntax**: `<color>`  **Initial value**:
        `ThreeDDarkShadow`.

    - msScrollbarTrackColor (boolean | number | string | dict | list; optional):
        The **`-ms-scrollbar-track-color`** CSS property is a
        Microsoft extension that specifies the color of the track
        element of a scrollbar.  **Syntax**: `<color>`  **Initial
        value**: `Scrollbar`.

    - msTextAutospace (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'ideograph-alpha', 'ideograph-numeric', 'ideograph-parenthesis', 'ideograph-space'; optional):
        The **`-ms-text-autospace`** CSS property is a Microsoft
        extension that specifies the autospacing and narrow space
        width adjustment of text.  **Syntax**: `none | ideograph-alpha
        | ideograph-numeric | ideograph-parenthesis | ideograph-space`
        **Initial value**: `none`.

    - msTextCombineHorizontal (boolean | number | string | dict | list; optional):
        The **`text-combine-upright`** CSS property sets the
        combination of characters into the space of a single
        character. If the combined text is wider than 1em, the user
        agent must fit the contents within 1em. The resulting
        composition is treated as a single upright glyph for layout
        and decoration. This property only has an effect in vertical
        writing modes.  **Syntax**: `none | all | [ digits <integer>?
        ]`  **Initial value**: `none`.

    - msTextOverflow (boolean | number | string | dict | list; optional):
        The **`text-overflow`** CSS property sets how hidden overflow
        content is signaled to users. It can be clipped, display an
        ellipsis ('`…`'), or display a custom string.  **Syntax**: `[
        clip | ellipsis | <string> ]{1,2}`  **Initial value**: `clip`.

    - msTouchAction (boolean | number | string | dict | list; optional):
        The **`touch-action`** CSS property sets how an element's
        region can be manipulated by a touchscreen user (for example,
        by zooming features built into the browser).  **Syntax**:
        `auto | none | [ [ pan-x | pan-left | pan-right ] || [ pan-y |
        pan-up | pan-down ] || pinch-zoom ] | manipulation`  **Initial
        value**: `auto`.

    - msTouchSelect (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'grippers'; optional):
        The **`-ms-touch-select`** CSS property is a Microsoft
        extension that toggles the gripper visual elements that enable
        touch text selection.  **Syntax**: `grippers | none`
        **Initial value**: `grippers`.

    - msTransform (boolean | number | string | dict | list; optional):
        The **`transform`** CSS property lets you rotate, scale, skew,
        or translate an element. It modifies the coordinate space of
        the CSS visual formatting model.  **Syntax**: `none |
        <transform-list>`  **Initial value**: `none`.

    - msTransformOrigin (string | number; optional):
        The **`transform-origin`** CSS property sets the origin for an
        element's transformations.  **Syntax**: `[ <length-percentage>
        | left | center | right | top | bottom ] | [ [
        <length-percentage> | left | center | right ] && [
        <length-percentage> | top | center | bottom ] ] <length>?`
        **Initial value**: `50% 50% 0`.

    - msTransition (boolean | number | string | dict | list; optional):
        The **`transition`** CSS property is a shorthand property for
        `transition-property`, `transition-duration`,
        `transition-timing-function`, and `transition-delay`.
        **Syntax**: `<single-transition>#`.

    - msTransitionDelay (boolean | number | string | dict | list; optional):
        The **`transition-delay`** CSS property specifies the duration
        to wait before starting a property's transition effect when
        its value changes.  **Syntax**: `<time>#`  **Initial value**:
        `0s`.

    - msTransitionDuration (boolean | number | string | dict | list; optional):
        The **`transition-duration`** CSS property sets the length of
        time a transition animation should take to complete. By
        default, the value is `0s`, meaning that no animation will
        occur.  **Syntax**: `<time>#`  **Initial value**: `0s`.

    - msTransitionProperty (boolean | number | string | dict | list; optional):
        The **`transition-property`** CSS property sets the CSS
        properties to which a transition effect should be applied.
        **Syntax**: `none | <single-transition-property>#`  **Initial
        value**: all.

    - msTransitionTimingFunction (boolean | number | string | dict | list; optional):
        The **`transition-timing-function`** CSS property sets how
        intermediate values are calculated for CSS properties being
        affected by a transition effect.  **Syntax**:
        `<easing-function>#`  **Initial value**: `ease`.

    - msUserSelect (a value equal to: 'text', 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'element'; optional):
        The **`user-select`** CSS property controls whether the user
        can select text. This doesn't have any effect on content
        loaded as part of a browser's user interface (its chrome),
        except in textboxes.  **Syntax**: `none | element | text`
        **Initial value**: `text`.

    - msWordBreak (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'break-word', 'break-all', 'keep-all'; optional):
        The **`word-break`** CSS property sets whether line breaks
        appear wherever the text would otherwise overflow its content
        box.  **Syntax**: `normal | break-all | keep-all | break-word`
        **Initial value**: `normal`.

    - msWrapFlow (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'end', 'start', 'both', 'clear', 'maximum'; optional):
        The **`-ms-wrap-flow`** CSS property is a Microsoft extension
        that specifies how exclusions impact inline content within
        block-level elements.  **Syntax**: `auto | both | start | end
        | maximum | clear`  **Initial value**: `auto`.

    - msWrapMargin (string | number; optional):
        The **`-ms-wrap-margin`** CSS property is a Microsoft
        extension that specifies a margin that offsets the inner wrap
        shape from other shapes.  **Syntax**: `<length>`  **Initial
        value**: `0`.

    - msWrapThrough (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'wrap'; optional):
        The **`-ms-wrap-through`** CSS property is a Microsoft
        extension that specifies how content should wrap around an
        exclusion element.  **Syntax**: `wrap | none`  **Initial
        value**: `wrap`.

    - msWritingMode (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'horizontal-tb', 'sideways-lr', 'sideways-rl', 'vertical-lr', 'vertical-rl'; optional):
        The **`writing-mode`** CSS property sets whether lines of text
        are laid out horizontally or vertically, as well as the
        direction in which blocks progress. When set for an entire
        document, it should be set on the root element (`html` element
        for HTML documents).  **Syntax**: `horizontal-tb | vertical-rl
        | vertical-lr | sideways-rl | sideways-lr`  **Initial value**:
        `horizontal-tb`.

    - objectFit (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain', 'cover', 'fill', 'scale-down'; optional):
        The **`object-fit`** CSS property sets how the content of a
        replaced element, such as an `<img>` or `<video>`, should be
        resized to fit its container.  **Syntax**: `fill | contain |
        cover | none | scale-down`  **Initial value**: `fill`  |
        Chrome | Firefox | Safari |  Edge  | IE  | | :----: | :-----:
        | :----: | :----: | :-: | | **32** | **36**  | **10** | **79**
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/object-fit.

    - objectPosition (string | number; optional):
        The **`object-position`** CSS property specifies the alignment
        of the selected replaced element's contents within the
        element's box. Areas of the box which aren't covered by the
        replaced element's object will show the element's background.
        **Syntax**: `<position>`  **Initial value**: `50% 50%`  |
        Chrome | Firefox | Safari |  Edge  | IE  | | :----: | :-----:
        | :----: | :----: | :-: | | **32** | **36**  | **10** | **79**
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/object-position.

    - offset (string | number; optional):
        The **`offset`** CSS shorthand property sets all the
        properties required for animating an element along a defined
        path.  **Syntax**: `[ <'offset-position'>? [ <'offset-path'> [
        <'offset-distance'> || <'offset-rotate'> ]? ]? ]! [ /
        <'offset-anchor'> ]?`  |    Chrome     | Firefox | Safari |
        Edge | IE  | | :-----------: | :-----: | :----: | :--: | :-: |
        |    **55**     | **72**  | **16** | n/a  | No  | | 46
        _(motion)_ |         |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset.

    - offsetAnchor (string | number; optional):
        **Syntax**: `auto | <position>`  **Initial value**: `auto`  |
        Chrome  | Firefox | Safari | Edge | IE  | | :-----: | :-----:
        | :----: | :--: | :-: | | **116** | **72**  | **16** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-anchor.

    - offsetBlock (string | number; optional):
        The **`inset-block`** CSS property defines the logical block
        start and end offsets of an element, which maps to physical
        offsets depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `top` and `bottom`, or `right` and `left` properties depending
        on the values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'top'>{1,2}` @,deprecated.

    - offsetBlockEnd (string | number; optional):
        The **`inset-block-end`** CSS property defines the logical
        block end offset of an element, which maps to a physical inset
        depending on the element's writing mode, directionality, and
        text orientation. It corresponds to the `top`, `right`,
        `bottom`, or `left` property depending on the values defined
        for `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'top'>`  **Initial value**: `auto` @,deprecated.

    - offsetBlockStart (string | number; optional):
        The **`inset-block-start`** CSS property defines the logical
        block start offset of an element, which maps to a physical
        inset depending on the element's writing mode, directionality,
        and text orientation. It corresponds to the `top`, `right`,
        `bottom`, or `left` property depending on the values defined
        for `writing-mode`, `direction`, and `text-orientation`.
        **Syntax**: `<'top'>`  **Initial value**: `auto` @,deprecated.

    - offsetDistance (string | number; optional):
        The **`offset-distance`** CSS property specifies a position
        along an `offset-path` for an element to be placed.
        **Syntax**: `<length-percentage>`  **Initial value**: `0`  |
        Chrome         | Firefox | Safari | Edge | IE  | |
        :--------------------: | :-----: | :----: | :--: | :-: | |
        **55**         | **72**  | **16** | n/a  | No  | | 46
        _(motion-distance)_ |         |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-distance.

    - offsetInline (string | number; optional):
        The **`inset-inline`** CSS property defines the logical start
        and end offsets of an element in the inline direction, which
        maps to physical offsets depending on the element's writing
        mode, directionality, and text orientation. It corresponds to
        the `top` and `bottom`, or `right` and `left` properties
        depending on the values defined for `writing-mode`,
        `direction`, and `text-orientation`.  **Syntax**:
        `<'top'>{1,2}` @,deprecated.

    - offsetInlineEnd (string | number; optional):
        The **`inset-inline-end`** CSS property defines the logical
        inline end inset of an element, which maps to a physical
        offset depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `top`, `right`, `bottom`, or `left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'top'>`  **Initial value**:
        `auto` @,deprecated.

    - offsetInlineStart (string | number; optional):
        The **`inset-inline-start`** CSS property defines the logical
        inline start inset of an element, which maps to a physical
        offset depending on the element's writing mode,
        directionality, and text orientation. It corresponds to the
        `top`, `right`, `bottom`, or `left` property depending on the
        values defined for `writing-mode`, `direction`, and
        `text-orientation`.  **Syntax**: `<'top'>`  **Initial value**:
        `auto` @,deprecated.

    - offsetPath (boolean | number | string | dict | list; optional):
        The **`offset-path`** CSS property specifies a motion path for
        an element to follow and defines the element's positioning
        within the parent container or SVG coordinate system.
        **Syntax**: `none | <offset-path> || <coord-box>`  **Initial
        value**: `none`  |       Chrome       | Firefox |  Safari  |
        Edge | IE  | | :----------------: | :-----: | :------: | :--:
        | :-: | |       **55**       | **72**  | **15.4** | n/a  | No
        | | 46 _(motion-path)_ |         |          |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-path.

    - offsetPosition (string | number; optional):
        **Syntax**: `normal | auto | <position>`  **Initial value**:
        `auto`  | Chrome  | Firefox | Safari | Edge | IE  | | :-----:
        | :-----: | :----: | :--: | :-: | | **116** |   n/a   | **16**
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-position.

    - offsetRotate (boolean | number | string | dict | list; optional):
        The **`offset-rotate`** CSS property defines the
        orientation/direction of the element as it is positioned along
        the `offset-path`.  **Syntax**: `[ auto | reverse ] ||
        <angle>`  **Initial value**: `auto`  |         Chrome
        | Firefox | Safari | Edge | IE  | | :--------------------: |
        :-----: | :----: | :--: | :-: | |         **56**         |
        **72**  | **16** | n/a  | No  | | 46 _(motion-rotation)_ |
        |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-rotate.

    - offsetRotation (boolean | number | string | dict | list; optional):
        The **`offset-rotate`** CSS property defines the
        orientation/direction of the element as it is positioned along
        the `offset-path`.  **Syntax**: `[ auto | reverse ] ||
        <angle>`  **Initial value**: `auto`  |         Chrome
        | Firefox | Safari | Edge | IE  | | :--------------------: |
        :-----: | :----: | :--: | :-: | |         **56**         |
        **72**  | **16** | n/a  | No  | | 46 _(motion-rotation)_ |
        |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/offset-rotate.

    - opacity (boolean | number | string | dict | list; optional):
        The **`opacity`** CSS property sets the opacity of an element.
        Opacity is the degree to which content behind an element is
        hidden, and is the opposite of transparency.  **Syntax**:
        `<alpha-value>`  **Initial value**: `1`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **2**  | **12** | **9** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/opacity.

    - order (boolean | number | string | dict | list; optional):
        The **`order`** CSS property sets the order to lay out an item
        in a flex or grid container. Items in a container are sorted
        by ascending `order` value and then by their source code
        order.  **Syntax**: `<integer>`  **Initial value**: `0`  |
        Chrome  | Firefox | Safari  |  Edge  |    IE    | | :------: |
        :-----: | :-----: | :----: | :------: | |  **29**  | **20**  |
        **9**  | **12** |  **11**  | | 21 _-x-_ |         | 7 _-x-_ |
        | 10 _-x-_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/order.

    - orphans (boolean | number | string | dict | list; optional):
        The **`orphans`** CSS property sets the minimum number of
        lines in a block container that must be shown at the _bottom_
        of a page, region, or column.  **Syntax**: `<integer>`
        **Initial value**: `2`  | Chrome | Firefox | Safari  |  Edge
        |  IE   | | :----: | :-----: | :-----: | :----: | :---: | |
        **25** |   No    | **1.3** | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/orphans.

    - outline (string | number; optional):
        The **`outline`** CSS shorthand property sets most of the
        outline properties in a single declaration.  **Syntax**: `[
        <'outline-color'> || <'outline-style'> || <'outline-width'> ]`
        | Chrome | Firefox |  Safari  |  Edge  |  IE   | | :----: |
        :-----: | :------: | :----: | :---: | | **94** | **88**  |
        **16.4** | **94** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/outline.

    - outlineColor (boolean | number | string | dict | list; optional):
        The **`outline-color`** CSS property sets the color of an
        element's outline.  **Syntax**: `<color> | invert`  **Initial
        value**: `invert`, for browsers supporting it, `currentColor`
        for the other  | Chrome | Firefox | Safari  |  Edge  |  IE   |
        | :----: | :-----: | :-----: | :----: | :---: | | **1**  |
        **1.5** | **1.2** | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/outline-color.

    - outlineOffset (string | number; optional):
        The **`outline-offset`** CSS property sets the amount of space
        between an outline and the edge or border of an element.
        **Syntax**: `<length>`  **Initial value**: `0`  | Chrome |
        Firefox | Safari  |  Edge  | IE  | | :----: | :-----: |
        :-----: | :----: | :-: | | **1**  | **1.5** | **1.2** | **15**
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/outline-offset.

    - outlineStyle (boolean | number | string | dict | list; optional):
        The **`outline-style`** CSS property sets the style of an
        element's outline. An outline is a line that is drawn around
        an element, outside the `border`.  **Syntax**: `auto |
        <'border-style'>`  **Initial value**: `none`  | Chrome |
        Firefox | Safari  |  Edge  |  IE   | | :----: | :-----: |
        :-----: | :----: | :---: | | **1**  | **1.5** | **1.2** |
        **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/outline-style.

    - outlineWidth (string | number; optional):
        The CSS **`outline-width`** property sets the thickness of an
        element's outline. An outline is a line that is drawn around
        an element, outside the `border`.  **Syntax**: `<line-width>`
        **Initial value**: `medium`  | Chrome | Firefox | Safari  |
        Edge  |  IE   | | :----: | :-----: | :-----: | :----: | :---:
        | | **1**  | **1.5** | **1.2** | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/outline-width.

    - overflow (boolean | number | string | dict | list; optional):
        The **`overflow`** CSS shorthand property sets the desired
        behavior for an element's overflow — i.e. when an element's
        content is too big to fit in its block formatting context — in
        both directions.  **Syntax**: `[ visible | hidden | clip |
        scroll | auto ]{1,2}`  **Initial value**: `visible`  | Chrome
        | Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow.

    - overflowAnchor (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        **Syntax**: `auto | none`  **Initial value**: `auto`  | Chrome
        | Firefox | Safari | Edge | IE  | | :----: | :-----: | :----:
        | :--: | :-: | | **56** | **66**  |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-anchor.

    - overflowBlock (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'scroll', 'clip'; optional):
        **Syntax**: `visible | hidden | clip | scroll | auto`
        **Initial value**: `auto`  | Chrome | Firefox | Safari | Edge
        | IE  | | :----: | :-----: | :----: | :--: | :-: | |   No   |
        **69**  |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-block.

    - overflowClipBox (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'content-box', 'padding-box'; optional):
        The **`overflow-clip-box`** CSS property specifies relative to
        which box the clipping happens when there is an overflow. It
        is short hand for the `overflow-clip-box-inline` and
        `overflow-clip-box-block` properties.  **Syntax**:
        `padding-box | content-box`  **Initial value**: `padding-box`.

    - overflowClipMargin (string | number; optional):
        **Syntax**: `<visual-box> || <length [0,∞]>`  **Initial
        value**: `0px`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | | **90** | **102** |
        No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-clip-margin.

    - overflowInline (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'scroll', 'clip'; optional):
        **Syntax**: `visible | hidden | clip | scroll | auto`
        **Initial value**: `auto`  | Chrome | Firefox | Safari | Edge
        | IE  | | :----: | :-----: | :----: | :--: | :-: | |   No   |
        **69**  |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-inline.

    - overflowWrap (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'anywhere', 'break-word'; optional):
        The **`overflow-wrap`** CSS property applies to inline
        elements, setting whether the browser should insert line
        breaks within an otherwise unbreakable string to prevent text
        from overflowing its line box.  **Syntax**: `normal |
        break-word | anywhere`  **Initial value**: `normal`  |
        Chrome      |      Firefox      |     Safari      |       Edge
        |          IE           | | :-------------: |
        :---------------: | :-------------: | :--------------: |
        :-------------------: | |     **23**      |      **49**
        |      **7**      |      **18**      | **5.5** _(word-wrap)_ |
        | 1 _(word-wrap)_ | 3.5 _(word-wrap)_ | 1 _(word-wrap)_ | 12
        _(word-wrap)_ |                       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-wrap.

    - overflowX (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'scroll', 'clip', '-moz-hidden-unscrollable'; optional):
        The **`overflow-x`** CSS property sets what shows when content
        overflows a block-level element's left and right edges. This
        may be nothing, a scroll bar, or the overflow content.
        **Syntax**: `visible | hidden | clip | scroll | auto`
        **Initial value**: `visible`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  | **3.5** | **3**  | **12** | **5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-x.

    - overflowY (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'scroll', 'clip', '-moz-hidden-unscrollable'; optional):
        The **`overflow-y`** CSS property sets what shows when content
        overflows a block-level element's top and bottom edges. This
        may be nothing, a scroll bar, or the overflow content.
        **Syntax**: `visible | hidden | clip | scroll | auto`
        **Initial value**: `visible`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  | **3.5** | **3**  | **12** | **5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overflow-y.

    - overlay (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`overlay`** CSS property specifies whether an element
        appearing in the top layer (for example, a shown popover or
        modal `<dialog>` element) is actually rendered in the top
        layer. This property is only relevant within a list of
        `transition-property` values, and only if `allow-discrete` is
        set as the `transition-behavior`.  **Syntax**: `none | auto`
        **Initial value**: `none`  | Chrome  | Firefox | Safari | Edge
        | IE  | | :-----: | :-----: | :----: | :--: | :-: | | **117**
        |   No    |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overlay.

    - overscrollBehavior (boolean | number | string | dict | list; optional):
        The **`overscroll-behavior`** CSS property sets what a browser
        does when reaching the boundary of a scrolling area. It's a
        shorthand for `overscroll-behavior-x` and
        `overscroll-behavior-y`.  **Syntax**: `[ contain | none | auto
        ]{1,2}`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari |  Edge  | IE  | | :----: | :-----: | :----: | :----: |
        :-: | | **63** | **59**  | **16** | **18** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overscroll-behavior.

    - overscrollBehaviorBlock (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain'; optional):
        The **`overscroll-behavior-block`** CSS property sets the
        browser's behavior when the block direction boundary of a
        scrolling area is reached.  **Syntax**: `contain | none |
        auto`  **Initial value**: `auto`  | Chrome | Firefox | Safari
        | Edge | IE  | | :----: | :-----: | :----: | :--: | :-: | |
        **77** | **73**  | **16** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overscroll-behavior-block.

    - overscrollBehaviorInline (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain'; optional):
        The **`overscroll-behavior-inline`** CSS property sets the
        browser's behavior when the inline direction boundary of a
        scrolling area is reached.  **Syntax**: `contain | none |
        auto`  **Initial value**: `auto`  | Chrome | Firefox | Safari
        | Edge | IE  | | :----: | :-----: | :----: | :--: | :-: | |
        **77** | **73**  | **16** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overscroll-behavior-inline.

    - overscrollBehaviorX (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain'; optional):
        The **`overscroll-behavior-x`** CSS property sets the
        browser's behavior when the horizontal boundary of a scrolling
        area is reached.  **Syntax**: `contain | none | auto`
        **Initial value**: `auto`  | Chrome | Firefox | Safari |  Edge
        | IE  | | :----: | :-----: | :----: | :----: | :-: | | **63**
        | **59**  | **16** | **18** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overscroll-behavior-x.

    - overscrollBehaviorY (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain'; optional):
        The **`overscroll-behavior-y`** CSS property sets the
        browser's behavior when the vertical boundary of a scrolling
        area is reached.  **Syntax**: `contain | none | auto`
        **Initial value**: `auto`  | Chrome | Firefox | Safari |  Edge
        | IE  | | :----: | :-----: | :----: | :----: | :-: | | **63**
        | **59**  | **16** | **18** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/overscroll-behavior-y.

    - padding (string | number; optional):
        The **`padding`** CSS shorthand property sets the padding area
        on all four sides of an element at once.  **Syntax**: `[
        <length> | <percentage> ]{1,4}`  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding.

    - paddingBlock (string | number; optional):
        The **`padding-block`** CSS shorthand property defines the
        logical block start and end padding of an element, which maps
        to physical padding properties depending on the element's
        writing mode, directionality, and text orientation.
        **Syntax**: `<'padding-left'>{1,2}`  | Chrome | Firefox |
        Safari  | Edge | IE  | | :----: | :-----: | :------: | :--: |
        :-: | | **87** | **66**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-block.

    - paddingBlockEnd (string | number; optional):
        The **`padding-block-end`** CSS property defines the logical
        block end padding of an element, which maps to a physical
        padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`  | Chrome | Firefox
        |  Safari  | Edge | IE  | | :----: | :-----: | :------: | :--:
        | :-: | | **69** | **41**  | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-block-end.

    - paddingBlockStart (string | number; optional):
        The **`padding-block-start`** CSS property defines the logical
        block start padding of an element, which maps to a physical
        padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`  | Chrome | Firefox
        |  Safari  | Edge | IE  | | :----: | :-----: | :------: | :--:
        | :-: | | **69** | **41**  | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-block-start.

    - paddingBottom (string | number; optional):
        The **`padding-bottom`** CSS property sets the height of the
        padding area on the bottom of an element.  **Syntax**:
        `<length> | <percentage>`  **Initial value**: `0`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-bottom.

    - paddingInline (string | number; optional):
        The **`padding-inline`** CSS shorthand property defines the
        logical inline start and end padding of an element, which maps
        to physical padding properties depending on the element's
        writing mode, directionality, and text orientation.
        **Syntax**: `<'padding-left'>{1,2}`  | Chrome | Firefox |
        Safari  | Edge | IE  | | :----: | :-----: | :------: | :--: |
        :-: | | **87** | **66**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-inline.

    - paddingInlineEnd (string | number; optional):
        The **`padding-inline-end`** CSS property defines the logical
        inline end padding of an element, which maps to a physical
        padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`  |          Chrome
        |        Firefox         |          Safari           | Edge |
        IE  | | :-----------------------: | :--------------------: |
        :-----------------------: | :--: | :-: | |          **69**
        |         **41**         |         **12.1**          | n/a  |
        No  | | 2 _(-webkit-padding-end)_ | 3 _(-moz-padding-end)_ | 3
        _(-webkit-padding-end)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-inline-end.

    - paddingInlineStart (string | number; optional):
        The **`padding-inline-start`** CSS property defines the
        logical inline start padding of an element, which maps to a
        physical padding depending on the element's writing mode,
        directionality, and text orientation.  **Syntax**:
        `<'padding-left'>`  **Initial value**: `0`  |           Chrome
        |         Firefox          |           Safari            |
        Edge | IE  | | :-------------------------: |
        :----------------------: | :-------------------------: | :--:
        | :-: | |           **69**            |          **41**
        |          **12.1**           | n/a  | No  | | 2
        _(-webkit-padding-start)_ | 3 _(-moz-padding-start)_ | 3
        _(-webkit-padding-start)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-inline-start.

    - paddingLeft (string | number; optional):
        The **`padding-left`** CSS property sets the width of the
        padding area to the left of an element.  **Syntax**: `<length>
        | <percentage>`  **Initial value**: `0`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-left.

    - paddingRight (string | number; optional):
        The **`padding-right`** CSS property sets the width of the
        padding area on the right of an element.  **Syntax**:
        `<length> | <percentage>`  **Initial value**: `0`  | Chrome |
        Firefox | Safari |  Edge  |  IE   | | :----: | :-----: |
        :----: | :----: | :---: | | **1**  |  **1**  | **1**  | **12**
        | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-right.

    - paddingTop (string | number; optional):
        The **`padding-top`** CSS property sets the height of the
        padding area on the top of an element.  **Syntax**: `<length>
        | <percentage>`  **Initial value**: `0`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/padding-top.

    - page (boolean | number | string | dict | list; optional):
        The **`page`** CSS property is used to specify the named page,
        a specific type of page defined by the `@page` at-rule.
        **Syntax**: `auto | <custom-ident>`  **Initial value**: `auto`
        | Chrome | Firefox |  Safari   | Edge | IE  | | :----: |
        :-----: | :-------: | :--: | :-: | | **85** | **110** |
        **≤13.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/page.

    - pageBreakAfter (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'left', 'right', 'always', 'avoid', 'recto', 'verso'; optional):
        The **`page-break-after`** CSS property adjusts page breaks
        _after_ the current element.  **Syntax**: `auto | always |
        avoid | left | right | recto | verso`  **Initial value**:
        `auto`  | Chrome | Firefox | Safari  |  Edge  |  IE   | |
        :----: | :-----: | :-----: | :----: | :---: | | **1**  |
        **1**  | **1.2** | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/page-break-after.

    - pageBreakBefore (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'left', 'right', 'always', 'avoid', 'recto', 'verso'; optional):
        The **`page-break-before`** CSS property adjusts page breaks
        _before_ the current element.  **Syntax**: `auto | always |
        avoid | left | right | recto | verso`  **Initial value**:
        `auto`  | Chrome | Firefox | Safari  |  Edge  |  IE   | |
        :----: | :-----: | :-----: | :----: | :---: | | **1**  |
        **1**  | **1.2** | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/page-break-before.

    - pageBreakInside (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'avoid'; optional):
        The **`page-break-inside`** CSS property adjusts page breaks
        _inside_ the current element.  **Syntax**: `auto | avoid`
        **Initial value**: `auto`  | Chrome | Firefox | Safari  |
        Edge  |  IE   | | :----: | :-----: | :-----: | :----: | :---:
        | | **1**  | **19**  | **1.3** | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/page-break-inside.

    - paintOrder (boolean | number | string | dict | list; optional):
        The **`paint-order`** CSS property lets you control the order
        in which the fill and stroke (and painting markers) of text
        content and shapes are drawn.  **Syntax**: `normal | [ fill ||
        stroke || markers ]`  **Initial value**: `normal`  | Chrome |
        Firefox | Safari |  Edge  | IE  | | :----: | :-----: | :----:
        | :----: | :-: | | **35** | **60**  | **8**  | **17** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/paint-order.

    - perspective (string | number; optional):
        The **`perspective`** CSS property determines the distance
        between the z=0 plane and the user in order to give a
        3D-positioned element some perspective.  **Syntax**: `none |
        <length>`  **Initial value**: `none`  |  Chrome  | Firefox |
        Safari  |  Edge  |   IE   | | :------: | :-----: | :-----: |
        :----: | :----: | |  **36**  | **16**  |  **9**  | **12** |
        **10** | | 12 _-x-_ |         | 4 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/perspective.

    - perspectiveOrigin (string | number; optional):
        The **`perspective-origin`** CSS property determines the
        position at which the viewer is looking. It is used as the
        _vanishing point_ by the `perspective` property.  **Syntax**:
        `<position>`  **Initial value**: `50% 50%`  |  Chrome  |
        Firefox | Safari  |  Edge  |   IE   | | :------: | :-----: |
        :-----: | :----: | :----: | |  **36**  | **16**  |  **9**  |
        **12** | **10** | | 12 _-x-_ |         | 4 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/perspective-origin.

    - placeContent (boolean | number | string | dict | list; optional):
        The **`place-content`** CSS shorthand property allows you to
        align content along both the block and inline directions at
        once (i.e. the `align-content` and `justify-content`
        properties) in a relevant layout system such as Grid or
        Flexbox.  **Syntax**: `<'align-content'> <'justify-content'>?`
        | Chrome | Firefox | Safari | Edge | IE  | | :----: | :-----:
        | :----: | :--: | :-: | | **59** | **45**  | **9**  | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/place-content.

    - placeItems (boolean | number | string | dict | list; optional):
        The CSS **`place-items`** shorthand property allows you to
        align items along both the block and inline directions at once
        (i.e. the `align-items` and `justify-items` properties) in a
        relevant layout system such as Grid or Flexbox. If the second
        value is not set, the first value is also used for it.
        **Syntax**: `<'align-items'> <'justify-items'>?`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **59** | **45**  | **11** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/place-items.

    - placeSelf (boolean | number | string | dict | list; optional):
        The **`place-self`** CSS shorthand property allows you to
        align an individual item in both the block and inline
        directions at once (i.e. the `align-self` and `justify-self`
        properties) in a relevant layout system such as Grid or
        Flexbox. If the second value is not present, the first value
        is also used for it.  **Syntax**: `<'align-self'>
        <'justify-self'>?`  | Chrome | Firefox | Safari | Edge | IE  |
        | :----: | :-----: | :----: | :--: | :-: | | **59** | **45**
        | **11** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/place-self.

    - pointerEvents (a value equal to: 'inherit', 'none', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'visible', 'fill', 'stroke', 'painted', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
        The **`pointer-events`** CSS property sets under what
        circumstances (if any) a particular graphic element can become
        the target of pointer events.  **Syntax**: `auto | none |
        visiblePainted | visibleFill | visibleStroke | visible |
        painted | fill | stroke | all | inherit`  **Initial value**:
        `auto`  | Chrome | Firefox | Safari |  Edge  |   IE   | |
        :----: | :-----: | :----: | :----: | :----: | | **1**  |
        **1.5** | **4**  | **12** | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/pointer-events.

    - position (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'fixed', '-webkit-sticky', 'absolute', 'relative', 'static', 'sticky'; optional):
        The **`position`** CSS property sets how an element is
        positioned in a document. The `top`, `right`, `bottom`, and
        `left` properties determine the final location of positioned
        elements.  **Syntax**: `static | relative | absolute | sticky
        | fixed`  **Initial value**: `static`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/position.

    - printColorAdjust (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'economy', 'exact'; optional):
        The **`print-color-adjust`** CSS property sets what, if
        anything, the user agent may do to optimize the appearance of
        the element on the output device. By default, the browser is
        allowed to make any adjustments to the element's appearance it
        determines to be necessary and prudent given the type and
        capabilities of the output device.  **Syntax**: `economy |
        exact`  **Initial value**: `economy`  |    Chrome    |
        Firefox       |  Safari  |     Edge     | IE  | | :----------:
        | :-----------------: | :------: | :----------: | :-: | |
        **17** _-x-_ |       **97**        | **15.4** | **79** _-x-_ |
        No  | |              | 48 _(color-adjust)_ | 6 _-x-_  |
        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/print-color-adjust.

    - quotes (boolean | number | string | dict | list; optional):
        The **`quotes`** CSS property sets how the browser should
        render quotation marks that are added using the `open-quotes`
        or `close-quotes` values of the CSS `content` property.
        **Syntax**: `none | auto | [ <string> <string> ]+`  **Initial
        value**: depends on user agent  | Chrome | Firefox | Safari |
        Edge  |  IE   | | :----: | :-----: | :----: | :----: | :---: |
        | **11** | **1.5** | **9**  | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/quotes.

    - resize (a value equal to: 'vertical', 'horizontal', 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'both', 'block', 'inline'; optional):
        The **`resize`** CSS property sets whether an element is
        resizable, and if so, in which directions.  **Syntax**: `none
        | both | horizontal | vertical | block | inline`  **Initial
        value**: `none`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | | **1**  |  **4**  |
        **3**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/resize.

    - right (string | number; optional):
        The **`right`** CSS property participates in specifying the
        horizontal position of a positioned element. It has no effect
        on non-positioned elements.  **Syntax**: `<length> |
        <percentage> | auto`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari |  Edge  |   IE    | | :----: | :-----: |
        :----: | :----: | :-----: | | **1**  |  **1**  | **1**  |
        **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/right.

    - rotate (boolean | number | string | dict | list; optional):
        The **`rotate`** CSS property allows you to specify rotation
        transforms individually and independently of the `transform`
        property. This maps better to typical user interface usage,
        and saves having to remember the exact order of transform
        functions to specify in the `transform` property.  **Syntax**:
        `none | <angle> | [ x | y | z | <number>{3} ] && <angle>`
        **Initial value**: `none`  | Chrome  | Firefox |  Safari  |
        Edge | IE  | | :-----: | :-----: | :------: | :--: | :-: | |
        **104** | **72**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/rotate.

    - rowGap (string | number; optional):
        The **`row-gap`** CSS property sets the size of the gap
        (gutter) between an element's rows.  **Syntax**: `normal |
        <length-percentage>`  **Initial value**: `normal`  | Chrome |
        Firefox |  Safari  |  Edge  | IE  | | :----: | :-----: |
        :------: | :----: | :-: | | **47** | **52**  | **10.1** |
        **16** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/row-gap.

    - rubyAlign (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'space-around', 'space-between', 'center', 'start'; optional):
        The **`ruby-align`** CSS property defines the distribution of
        the different ruby elements over the base.  **Syntax**: `start
        | center | space-between | space-around`  **Initial value**:
        `space-around`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | |   No   | **38**  |
        No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/ruby-align.

    - rubyMerge (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'collapse', 'separate'; optional):
        **Syntax**: `separate | collapse | auto`  **Initial value**:
        `separate`.

    - rubyPosition (boolean | number | string | dict | list; optional):
        The **`ruby-position`** CSS property defines the position of a
        ruby element relatives to its base element. It can be
        positioned over the element (`over`), under it (`under`), or
        between the characters on their right side
        (`inter-character`).  **Syntax**: `[ alternate || [ over |
        under ] ] | inter-character`  **Initial value**: `alternate`
        | Chrome  | Firefox |   Safari    | Edge  | IE  | | :-----: |
        :-----: | :---------: | :---: | :-: | | **84**  | **38**  |
        **7** _-x-_ | 12-79 | No  | | 1 _-x-_ |         |
        |       |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/ruby-position.

    - scale (boolean | number | string | dict | list; optional):
        The **`scale`** CSS property allows you to specify scale
        transforms individually and independently of the `transform`
        property. This maps better to typical user interface usage,
        and saves having to remember the exact order of transform
        functions to specify in the `transform` value.  **Syntax**:
        `none | <number>{1,3}`  **Initial value**: `none`  | Chrome  |
        Firefox |  Safari  | Edge | IE  | | :-----: | :-----: |
        :------: | :--: | :-: | | **104** | **72**  | **14.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scale.

    - scrollBehavior (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'smooth'; optional):
        The **`scroll-behavior`** CSS property sets the behavior for a
        scrolling box when scrolling is triggered by the navigation or
        CSSOM scrolling APIs.  **Syntax**: `auto | smooth`  **Initial
        value**: `auto`  | Chrome | Firefox |  Safari  | Edge | IE  |
        | :----: | :-----: | :------: | :--: | :-: | | **61** | **36**
        | **15.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-behavior.

    - scrollMargin (string | number; optional):
        The **`scroll-margin`** shorthand property sets all of the
        scroll margins of an element at once, assigning values much
        like the `margin` property does for margins of an element.
        **Syntax**: `<length>{1,4}`  | Chrome | Firefox |
        Safari           | Edge | IE  | | :----: | :-----: |
        :-----------------------: | :--: | :-: | | **69** | **90**  |
        **14.1**          | n/a  | No  | |        |         | 11
        _(scroll-snap-margin)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin.

    - scrollMarginBlock (string | number; optional):
        The `scroll-margin-block` shorthand property sets the scroll
        margins of an element in the block dimension.  **Syntax**:
        `<length>{1,2}`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | | **69** | **68**  |
        **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-block.

    - scrollMarginBlockEnd (string | number; optional):
        The `scroll-margin-block-end` property defines the margin of
        the scroll snap area at the end of the block dimension that is
        used for snapping this box to the snapport. The scroll snap
        area is determined by taking the transformed border box,
        finding its rectangular bounding box (axis-aligned in the
        scroll container's coordinate space), then adding the
        specified outsets.  **Syntax**: `<length>`  **Initial value**:
        `0`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | | **69** | **68**  | **15** |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-block-end.

    - scrollMarginBlockStart (string | number; optional):
        The `scroll-margin-block-start` property defines the margin of
        the scroll snap area at the start of the block dimension that
        is used for snapping this box to the snapport. The scroll snap
        area is determined by taking the transformed border box,
        finding its rectangular bounding box (axis-aligned in the
        scroll container's coordinate space), then adding the
        specified outsets.  **Syntax**: `<length>`  **Initial value**:
        `0`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | | **69** | **68**  | **15** |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-block-start.

    - scrollMarginBottom (string | number; optional):
        The `scroll-margin-bottom` property defines the bottom margin
        of the scroll snap area that is used for snapping this box to
        the snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |
        Safari              | Edge | IE  | | :----: | :-----: |
        :------------------------------: | :--: | :-: | | **69** |
        **68**  |             **14.1**             | n/a  | No  | |
        |         | 11 _(scroll-snap-margin-bottom)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-bottom.

    - scrollMarginInline (string | number; optional):
        The `scroll-margin-inline` shorthand property sets the scroll
        margins of an element in the inline dimension.  **Syntax**:
        `<length>{1,2}`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | | **69** | **68**  |
        **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-inline.

    - scrollMarginInlineEnd (string | number; optional):
        The `scroll-margin-inline-end` property defines the margin of
        the scroll snap area at the end of the inline dimension that
        is used for snapping this box to the snapport. The scroll snap
        area is determined by taking the transformed border box,
        finding its rectangular bounding box (axis-aligned in the
        scroll container's coordinate space), then adding the
        specified outsets.  **Syntax**: `<length>`  **Initial value**:
        `0`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | | **69** | **68**  | **15** |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-inline-end.

    - scrollMarginInlineStart (string | number; optional):
        The `scroll-margin-inline-start` property defines the margin
        of the scroll snap area at the start of the inline dimension
        that is used for snapping this box to the snapport. The scroll
        snap area is determined by taking the transformed border box,
        finding its rectangular bounding box (axis-aligned in the
        scroll container's coordinate space), then adding the
        specified outsets.  **Syntax**: `<length>`  **Initial value**:
        `0`  | Chrome | Firefox | Safari | Edge | IE  | | :----: |
        :-----: | :----: | :--: | :-: | | **69** | **68**  | **15** |
        n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-inline-start.

    - scrollMarginLeft (string | number; optional):
        The `scroll-margin-left` property defines the left margin of
        the scroll snap area that is used for snapping this box to the
        snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |
        Safari             | Edge | IE  | | :----: | :-----: |
        :----------------------------: | :--: | :-: | | **69** |
        **68**  |            **14.1**            | n/a  | No  | |
        |         | 11 _(scroll-snap-margin-left)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-left.

    - scrollMarginRight (string | number; optional):
        The `scroll-margin-right` property defines the right margin of
        the scroll snap area that is used for snapping this box to the
        snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |
        Safari              | Edge | IE  | | :----: | :-----: |
        :-----------------------------: | :--: | :-: | | **69** |
        **68**  |            **14.1**             | n/a  | No  | |
        |         | 11 _(scroll-snap-margin-right)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-right.

    - scrollMarginTop (string | number; optional):
        The `scroll-margin-top` property defines the top margin of the
        scroll snap area that is used for snapping this box to the
        snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |            Safari
        | Edge | IE  | | :----: | :-----: |
        :---------------------------: | :--: | :-: | | **69** | **68**
        |           **14.1**            | n/a  | No  | |        |
        | 11 _(scroll-snap-margin-top)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-top.

    - scrollPadding (string | number; optional):
        The **`scroll-padding`** shorthand property sets scroll
        padding on all sides of an element at once, much like the
        `padding` property does for padding on an element.
        **Syntax**: `[ auto | <length-percentage> ]{1,4}`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **69** | **68**  | **14.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding.

    - scrollPaddingBlock (string | number; optional):
        The `scroll-padding-block` shorthand property sets the scroll
        padding of an element in the block dimension.  **Syntax**: `[
        auto | <length-percentage> ]{1,2}`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | | **69** | **68**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-block.

    - scrollPaddingBlockEnd (string | number; optional):
        The `scroll-padding-block-end` property defines offsets for
        the end edge in the block dimension of the _optimal viewing
        region_ of the scrollport: the region used as the target
        region for placing things in view of the user. This allows the
        author to exclude regions of the scrollport that are obscured
        by other content (such as fixed-positioned toolbars or
        sidebars) or to put more breathing room between a targeted
        element and the edges of the scrollport.  **Syntax**: `auto |
        <length-percentage>`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **69** | **68**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-block-end.

    - scrollPaddingBlockStart (string | number; optional):
        The `scroll-padding-block-start` property defines offsets for
        the start edge in the block dimension of the _optimal viewing
        region_ of the scrollport: the region used as the target
        region for placing things in view of the user. This allows the
        author to exclude regions of the scrollport that are obscured
        by other content (such as fixed-positioned toolbars or
        sidebars) or to put more breathing room between a targeted
        element and the edges of the scrollport.  **Syntax**: `auto |
        <length-percentage>`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **69** | **68**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-block-start.

    - scrollPaddingBottom (string | number; optional):
        The `scroll-padding-bottom` property defines offsets for the
        bottom of the _optimal viewing region_ of the scrollport: the
        region used as the target region for placing things in view of
        the user. This allows the author to exclude regions of the
        scrollport that are obscured by other content (such as
        fixed-positioned toolbars or sidebars) or to put more
        breathing room between a targeted element and the edges of the
        scrollport.  **Syntax**: `auto | <length-percentage>`
        **Initial value**: `auto`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **69** | **68**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-bottom.

    - scrollPaddingInline (string | number; optional):
        The `scroll-padding-inline` shorthand property sets the scroll
        padding of an element in the inline dimension.  **Syntax**: `[
        auto | <length-percentage> ]{1,2}`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | | **69** | **68**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-inline.

    - scrollPaddingInlineEnd (string | number; optional):
        The `scroll-padding-inline-end` property defines offsets for
        the end edge in the inline dimension of the _optimal viewing
        region_ of the scrollport: the region used as the target
        region for placing things in view of the user. This allows the
        author to exclude regions of the scrollport that are obscured
        by other content (such as fixed-positioned toolbars or
        sidebars) or to put more breathing room between a targeted
        element and the edges of the scrollport.  **Syntax**: `auto |
        <length-percentage>`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **69** | **68**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-inline-end.

    - scrollPaddingInlineStart (string | number; optional):
        The `scroll-padding-inline-start` property defines offsets for
        the start edge in the inline dimension of the _optimal viewing
        region_ of the scrollport: the region used as the target
        region for placing things in view of the user. This allows the
        author to exclude regions of the scrollport that are obscured
        by other content (such as fixed-positioned toolbars or
        sidebars) or to put more breathing room between a targeted
        element and the edges of the scrollport.  **Syntax**: `auto |
        <length-percentage>`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **69** | **68**  | **15** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-inline-start.

    - scrollPaddingLeft (string | number; optional):
        The `scroll-padding-left` property defines offsets for the
        left of the _optimal viewing region_ of the scrollport: the
        region used as the target region for placing things in view of
        the user. This allows the author to exclude regions of the
        scrollport that are obscured by other content (such as
        fixed-positioned toolbars or sidebars) or to put more
        breathing room between a targeted element and the edges of the
        scrollport.  **Syntax**: `auto | <length-percentage>`
        **Initial value**: `auto`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **69** | **68**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-left.

    - scrollPaddingRight (string | number; optional):
        The `scroll-padding-right` property defines offsets for the
        right of the _optimal viewing region_ of the scrollport: the
        region used as the target region for placing things in view of
        the user. This allows the author to exclude regions of the
        scrollport that are obscured by other content (such as
        fixed-positioned toolbars or sidebars) or to put more
        breathing room between a targeted element and the edges of the
        scrollport.  **Syntax**: `auto | <length-percentage>`
        **Initial value**: `auto`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **69** | **68**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-right.

    - scrollPaddingTop (string | number; optional):
        The **`scroll-padding-top`** property defines offsets for the
        top of the _optimal viewing region_ of the scrollport: the
        region used as the target region for placing things in view of
        the user. This allows the author to exclude regions of the
        scrollport that are obscured by other content (such as
        fixed-positioned toolbars or sidebars) or to put more
        breathing room between a targeted element and the edges of the
        scrollport.  **Syntax**: `auto | <length-percentage>`
        **Initial value**: `auto`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **69** | **68**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-padding-top.

    - scrollSnapAlign (boolean | number | string | dict | list; optional):
        The `scroll-snap-align` property specifies the box's snap
        position as an alignment of its snap area (as the alignment
        subject) within its snap container's snapport (as the
        alignment container). The two values specify the snapping
        alignment in the block axis and inline axis, respectively. If
        only one value is specified, the second value defaults to the
        same value.  **Syntax**: `[ none | start | end | center
        ]{1,2}`  **Initial value**: `none`  | Chrome | Firefox |
        Safari | Edge | IE  | | :----: | :-----: | :----: | :--: | :-:
        | | **69** | **68**  | **11** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-snap-align.

    - scrollSnapCoordinate (string | number; optional):
        The **`scroll-snap-coordinate`** CSS property defines the x
        and y coordinate positions within an element that will align
        with its nearest ancestor scroll container's
        `scroll-snap-destination` for each respective axis.
        **Syntax**: `none | <position>#`  **Initial value**: `none`
        @,deprecated.

    - scrollSnapDestination (string | number; optional):
        The **`scroll-snap-destination`** CSS property defines the
        position in x and y coordinates within the scroll container's
        visual viewport which element snap points align with.
        **Syntax**: `<position>`  **Initial value**: `0px 0px`
        @,deprecated.

    - scrollSnapMargin (string | number; optional):
        The **`scroll-margin`** shorthand property sets all of the
        scroll margins of an element at once, assigning values much
        like the `margin` property does for margins of an element.
        **Syntax**: `<length>{1,4}`  | Chrome | Firefox |
        Safari           | Edge | IE  | | :----: | :-----: |
        :-----------------------: | :--: | :-: | | **69** |  68-90  |
        **14.1**          | n/a  | No  | |        |         | 11
        _(scroll-snap-margin)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin.

    - scrollSnapMarginBottom (string | number; optional):
        The `scroll-margin-bottom` property defines the bottom margin
        of the scroll snap area that is used for snapping this box to
        the snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |
        Safari              | Edge | IE  | | :----: | :-----: |
        :------------------------------: | :--: | :-: | | **69** |
        **68**  |             **14.1**             | n/a  | No  | |
        |         | 11 _(scroll-snap-margin-bottom)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-bottom.

    - scrollSnapMarginLeft (string | number; optional):
        The `scroll-margin-left` property defines the left margin of
        the scroll snap area that is used for snapping this box to the
        snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |
        Safari             | Edge | IE  | | :----: | :-----: |
        :----------------------------: | :--: | :-: | | **69** |
        **68**  |            **14.1**            | n/a  | No  | |
        |         | 11 _(scroll-snap-margin-left)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-left.

    - scrollSnapMarginRight (string | number; optional):
        The `scroll-margin-right` property defines the right margin of
        the scroll snap area that is used for snapping this box to the
        snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |
        Safari              | Edge | IE  | | :----: | :-----: |
        :-----------------------------: | :--: | :-: | | **69** |
        **68**  |            **14.1**             | n/a  | No  | |
        |         | 11 _(scroll-snap-margin-right)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-right.

    - scrollSnapMarginTop (string | number; optional):
        The `scroll-margin-top` property defines the top margin of the
        scroll snap area that is used for snapping this box to the
        snapport. The scroll snap area is determined by taking the
        transformed border box, finding its rectangular bounding box
        (axis-aligned in the scroll container's coordinate space),
        then adding the specified outsets.  **Syntax**: `<length>`
        **Initial value**: `0`  | Chrome | Firefox |            Safari
        | Edge | IE  | | :----: | :-----: |
        :---------------------------: | :--: | :-: | | **69** | **68**
        |           **14.1**            | n/a  | No  | |        |
        | 11 _(scroll-snap-margin-top)_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-margin-top.

    - scrollSnapPointsX (boolean | number | string | dict | list; optional):
        The **`scroll-snap-points-x`** CSS property defines the
        horizontal positioning of snap points within the content of
        the scroll container they are applied to.  **Syntax**: `none |
        repeat( <length-percentage> )`  **Initial value**: `none`
        @,deprecated.

    - scrollSnapPointsY (boolean | number | string | dict | list; optional):
        The **`scroll-snap-points-y`** CSS property defines the
        vertical positioning of snap points within the content of the
        scroll container they are applied to.  **Syntax**: `none |
        repeat( <length-percentage> )`  **Initial value**: `none`
        @,deprecated.

    - scrollSnapStop (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'always'; optional):
        The **`scroll-snap-stop`** CSS property defines whether or not
        the scroll container is allowed to \"pass over\" possible snap
        positions.  **Syntax**: `normal | always`  **Initial value**:
        `normal`  | Chrome | Firefox | Safari | Edge | IE  | | :----:
        | :-----: | :----: | :--: | :-: | | **75** | **103** | **15**
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-snap-stop.

    - scrollSnapType (boolean | number | string | dict | list; optional):
        The **`scroll-snap-type`** CSS property sets how strictly snap
        points are enforced on the scroll container in case there is
        one.  **Syntax**: `none | [ x | y | block | inline | both ] [
        mandatory | proximity ]?`  **Initial value**: `none`  | Chrome
        | Firefox | Safari  |  Edge  |      IE      | | :----: |
        :-----: | :-----: | :----: | :----------: | | **69** |  39-68
        | **11**  | **79** | **10** _-x-_ | |        |         | 9
        _-x-_ |        |              |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-snap-type.

    - scrollSnapTypeX (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'mandatory', 'proximity'; optional):
        The **`scroll-snap-type-x`** CSS property defines how strictly
        snap points are enforced on the horizontal axis of the scroll
        container in case there is one.  **Syntax**: `none | mandatory
        | proximity`  **Initial value**: `none` @,deprecated.

    - scrollSnapTypeY (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'mandatory', 'proximity'; optional):
        The **`scroll-snap-type-y`** CSS property defines how strictly
        snap points are enforced on the vertical axis of the scroll
        container in case there is one.  **Syntax**: `none | mandatory
        | proximity`  **Initial value**: `none` @,deprecated.

    - scrollTimeline (boolean | number | string | dict | list; optional):
        The **`scroll-timeline`** CSS shorthand property defines a
        name that can be used to identify the source element of a
        scroll timeline, along with the scrollbar axis that should
        provide the timeline.  **Syntax**: `[ <'scroll-timeline-name'>
        <'scroll-timeline-axis'>? ]#`  | Chrome  | Firefox | Safari |
        Edge | IE  | | :-----: | :-----: | :----: | :--: | :-: | |
        **115** |   n/a   |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-timeline.

    - scrollTimelineAxis (boolean | number | string | dict | list; optional):
        The **`scroll-timeline-axis`** CSS property can be used to
        specify the scrollbar that will be used to provide the
        timeline for a scroll-timeline animation.  **Syntax**: `[
        block | inline | x | y ]#`  **Initial value**: `block`  |
        Chrome  | Firefox | Safari | Edge | IE  | | :-----: | :-----:
        | :----: | :--: | :-: | | **115** |   n/a   |   No   | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-timeline-axis.

    - scrollTimelineName (boolean | number | string | dict | list; optional):
        The **`scroll-timeline-name`** CSS property defines a name
        that can be used to identify an element as the source of a
        scroll timeline for an animation.  **Syntax**: `none |
        <dashed-ident>#`  **Initial value**: `none`  | Chrome  |
        Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----: |
        :--: | :-: | | **115** |   n/a   |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scroll-timeline-name.

    - scrollbarColor (boolean | number | string | dict | list; optional):
        The **`scrollbar-color`** CSS property sets the color of the
        scrollbar track and thumb.  **Syntax**: `auto | <color>{2}`
        **Initial value**: `auto`  | Chrome  | Firefox | Safari | Edge
        | IE  | | :-----: | :-----: | :----: | :--: | :-: | | **121**
        | **64**  |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scrollbar-color.

    - scrollbarGutter (boolean | number | string | dict | list; optional):
        The **`scrollbar-gutter`** CSS property allows authors to
        reserve space for the scrollbar, preventing unwanted layout
        changes as the content grows while also avoiding unnecessary
        visuals when scrolling isn't needed.  **Syntax**: `auto |
        stable && both-edges?`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **94** | **97**  |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scrollbar-gutter.

    - scrollbarWidth (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'thin'; optional):
        The **`scrollbar-width`** property allows the author to set
        the maximum thickness of an element's scrollbars when they are
        shown.  **Syntax**: `auto | thin | none`  **Initial value**:
        `auto`  | Chrome  | Firefox | Safari | Edge | IE  | | :-----:
        | :-----: | :----: | :--: | :-: | | **121** | **64**  |   No
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/scrollbar-width.

    - shapeImageThreshold (boolean | number | string | dict | list; optional):
        The **`shape-image-threshold`** CSS property sets the alpha
        channel threshold used to extract the shape using an image as
        the value for `shape-outside`.  **Syntax**: `<alpha-value>`
        **Initial value**: `0.0`  | Chrome | Firefox |  Safari  | Edge
        | IE  | | :----: | :-----: | :------: | :--: | :-: | | **37**
        | **62**  | **10.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/shape-image-threshold.

    - shapeMargin (string | number; optional):
        The **`shape-margin`** CSS property sets a margin for a CSS
        shape created using `shape-outside`.  **Syntax**:
        `<length-percentage>`  **Initial value**: `0`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | **37** | **62**  | **10.1** | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/shape-margin.

    - shapeOutside (boolean | number | string | dict | list; optional):
        The **`shape-outside`** CSS property defines a shape—which may
        be non-rectangular—around which adjacent inline content should
        wrap. By default, inline content wraps around its margin box;
        `shape-outside` provides a way to customize this wrapping,
        making it possible to wrap text around complex objects rather
        than simple boxes.  **Syntax**: `none | [ <shape-box> ||
        <basic-shape> ] | <image>`  **Initial value**: `none`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **37** | **62**  | **10.1** | n/a
        | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/shape-outside.

    - shapeRendering (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'geometricPrecision', 'optimizeSpeed', 'crispEdges'; optional)

    - stopColor (boolean | number | string | dict | list; optional)

    - stopOpacity (boolean | number | string | dict | list; optional)

    - stroke (boolean | number | string | dict | list; optional)

    - strokeDasharray (string | number; optional)

    - strokeDashoffset (string | number; optional)

    - strokeLinecap (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'round', 'butt', 'square'; optional)

    - strokeLinejoin (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'round', 'bevel', 'miter'; optional)

    - strokeMiterlimit (boolean | number | string | dict | list; optional)

    - strokeOpacity (boolean | number | string | dict | list; optional)

    - strokeWidth (string | number; optional)

    - tabSize (string | number; optional):
        The **`tab-size`** CSS property is used to customize the width
        of tab characters (U+0009).  **Syntax**: `<integer> |
        <length>`  **Initial value**: `8`  | Chrome | Firefox | Safari
        | Edge | IE  | | :----: | :-----: | :----: | :--: | :-: | |
        **21** | **91**  | **7**  | n/a  | No  | |        | 4 _-x-_ |
        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/tab-size.

    - tableLayout (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'fixed'; optional):
        The **`table-layout`** CSS property sets the algorithm used to
        lay out `<table>` cells, rows, and columns.  **Syntax**: `auto
        | fixed`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **14** |  **1**  | **1**  | **12** | **5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/table-layout.

    - textAlign (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'left', 'right', '-webkit-match-parent', 'justify', 'match-parent'; optional):
        The **`text-align`** CSS property sets the horizontal
        alignment of the inline-level content inside a block element
        or table-cell box. This means it works like `vertical-align`
        but in the horizontal direction.  **Syntax**: `start | end |
        left | right | center | justify | match-parent`  **Initial
        value**: `start`, or a nameless value that acts as `left` if
        _direction_ is `ltr`, `right` if _direction_ is `rtl` if
        `start` is not supported by the browser.  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-align.

    - textAlignLast (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'center', 'end', 'start', 'left', 'right', 'justify'; optional):
        The **`text-align-last`** CSS property sets how the last line
        of a block or a line, right before a forced line break, is
        aligned.  **Syntax**: `auto | start | end | left | right |
        center | justify`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari |  Edge  |   IE    | | :----: | :-----: |
        :----: | :----: | :-----: | | **47** | **49**  | **16** |
        **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-align-last.

    - textAnchor (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'end', 'start', 'middle'; optional)

    - textCombineUpright (boolean | number | string | dict | list; optional):
        The **`text-combine-upright`** CSS property sets the
        combination of characters into the space of a single
        character. If the combined text is wider than 1em, the user
        agent must fit the contents within 1em. The resulting
        composition is treated as a single upright glyph for layout
        and decoration. This property only has an effect in vertical
        writing modes.  **Syntax**: `none | all | [ digits <integer>?
        ]`  **Initial value**: `none`  |           Chrome           |
        Firefox |            Safari            |  Edge  |
        IE                   | | :------------------------: | :-----:
        | :--------------------------: | :----: |
        :------------------------------------: | |           **48**
        | **48**  |           **15.4**           | **79** | **11**
        _(-ms-text-combine-horizontal)_ | | 9 _(-webkit-text-combine)_
        |         | 5.1 _(-webkit-text-combine)_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-combine-upright.

    - textDecoration (string | number; optional):
        The **`text-decoration`** shorthand CSS property sets the
        appearance of decorative lines on text. It is a shorthand for
        `text-decoration-line`, `text-decoration-color`,
        `text-decoration-style`, and the newer
        `text-decoration-thickness` property.  **Syntax**:
        `<'text-decoration-line'> || <'text-decoration-style'> ||
        <'text-decoration-color'> || <'text-decoration-thickness'>`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration.

    - textDecorationColor (boolean | number | string | dict | list; optional):
        The **`text-decoration-color`** CSS property sets the color of
        decorations added to text by `text-decoration-line`.
        **Syntax**: `<color>`  **Initial value**: `currentcolor`  |
        Chrome | Firefox |  Safari  | Edge | IE  | | :----: | :-----:
        | :------: | :--: | :-: | | **57** | **36**  | **12.1** | n/a
        | No  | |        |         | 8 _-x-_  |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration-color.

    - textDecorationLine (boolean | number | string | dict | list; optional):
        The **`text-decoration-line`** CSS property sets the kind of
        decoration that is used on text in an element, such as an
        underline or overline.  **Syntax**: `none | [ underline ||
        overline || line-through || blink ] | spelling-error |
        grammar-error`  **Initial value**: `none`  | Chrome | Firefox
        |  Safari  | Edge | IE  | | :----: | :-----: | :------: | :--:
        | :-: | | **57** | **36**  | **12.1** | n/a  | No  | |
        |         | 8 _-x-_  |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration-line.

    - textDecorationSkip (boolean | number | string | dict | list; optional):
        The **`text-decoration-skip`** CSS property sets what parts of
        an element's content any text decoration affecting the element
        must skip over. It controls all text decoration lines drawn by
        the element and also any text decoration lines drawn by its
        ancestors.  **Syntax**: `none | [ objects || [ spaces | [
        leading-spaces || trailing-spaces ] ] || edges ||
        box-decoration ]`  **Initial value**: `objects`  | Chrome |
        Firefox |  Safari  | Edge | IE  | | :----: | :-----: |
        :------: | :--: | :-: | | 57-64  |   No    | **12.1** | n/a  |
        No  | |        |         | 7 _-x-_  |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration-skip.

    - textDecorationSkipInk (a value equal to: 'inherit', 'none', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset'; optional):
        The **`text-decoration-skip-ink`** CSS property specifies how
        overlines and underlines are drawn when they pass over glyph
        ascenders and descenders.  **Syntax**: `auto | all | none`
        **Initial value**: `auto`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **64** | **70**  | **15.4** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration-skip-ink.

    - textDecorationStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'dashed', 'dotted', 'double', 'solid', 'wavy'; optional):
        The **`text-decoration-style`** CSS property sets the style of
        the lines specified by `text-decoration-line`. The style
        applies to all lines that are set with `text-decoration-line`.
        **Syntax**: `solid | double | dotted | dashed | wavy`
        **Initial value**: `solid`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **57** | **36**  | **12.1** | n/a  | No  | |        |
        | 8 _-x-_  |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration-style.

    - textDecorationThickness (string | number; optional):
        The **`text-decoration-thickness`** CSS property sets the
        stroke thickness of the decoration line that is used on text
        in an element, such as a line-through, underline, or overline.
        **Syntax**: `auto | from-font | <length> | <percentage> `
        **Initial value**: `auto`  | Chrome | Firefox |  Safari  |
        Edge | IE  | | :----: | :-----: | :------: | :--: | :-: | |
        **89** | **70**  | **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-decoration-thickness.

    - textEmphasis (boolean | number | string | dict | list; optional):
        The **`text-emphasis`** CSS property applies emphasis marks to
        text (except spaces and control characters). It is a shorthand
        for `text-emphasis-style` and `text-emphasis-color`.
        **Syntax**: `<'text-emphasis-style'> ||
        <'text-emphasis-color'>`  |  Chrome  | Firefox | Safari | Edge
        | IE  | | :------: | :-----: | :----: | :--: | :-: | |  **99**
        | **46**  | **7**  | n/a  | No  | | 25 _-x-_ |         |
        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-emphasis.

    - textEmphasisColor (boolean | number | string | dict | list; optional):
        The **`text-emphasis-color`** CSS property sets the color of
        emphasis marks. This value can also be set using the
        `text-emphasis` shorthand.  **Syntax**: `<color>`  **Initial
        value**: `currentcolor`  |  Chrome  | Firefox | Safari | Edge
        | IE  | | :------: | :-----: | :----: | :--: | :-: | |  **99**
        | **46**  | **7**  | n/a  | No  | | 25 _-x-_ |         |
        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-emphasis-color.

    - textEmphasisPosition (boolean | number | string | dict | list; optional):
        The **`text-emphasis-position`** CSS property sets where
        emphasis marks are drawn. Like ruby text, if there isn't
        enough room for emphasis marks, the line height is increased.
        **Syntax**: `[ over | under ] && [ right | left ]`  **Initial
        value**: `over right`  |  Chrome  | Firefox | Safari | Edge |
        IE  | | :------: | :-----: | :----: | :--: | :-: | |  **99**
        | **46**  | **7**  | n/a  | No  | | 25 _-x-_ |         |
        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-emphasis-position.

    - textEmphasisStyle (boolean | number | string | dict | list; optional):
        The **`text-emphasis-style`** CSS property sets the appearance
        of emphasis marks. It can also be set, and reset, using the
        `text-emphasis` shorthand.  **Syntax**: `none | [ [ filled |
        open ] || [ dot | circle | double-circle | triangle | sesame ]
        ] | <string>`  **Initial value**: `none`  |  Chrome  | Firefox
        | Safari | Edge | IE  | | :------: | :-----: | :----: | :--: |
        :-: | |  **99**  | **46**  | **7**  | n/a  | No  | | 25 _-x-_
        |         |        |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-emphasis-style.

    - textIndent (string | number; optional):
        The **`text-indent`** CSS property sets the length of empty
        space (indentation) that is put before lines of text in a
        block.  **Syntax**: `<length-percentage> && hanging? &&
        each-line?`  **Initial value**: `0`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **3** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-indent.

    - textJustify (a value equal to: 'inherit', 'none', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'inter-character', 'inter-word'; optional):
        The **`text-justify`** CSS property sets what type of
        justification should be applied to text when `text-align``:
        justify;` is set on an element.  **Syntax**: `auto |
        inter-character | inter-word | none`  **Initial value**:
        `auto`  | Chrome | Firefox | Safari | Edge  |   IE   | |
        :----: | :-----: | :----: | :---: | :----: | |  n/a   | **55**
        |   No   | 12-79 | **11** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-justify.

    - textOrientation (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'mixed', 'sideways', 'upright'; optional):
        The **`text-orientation`** CSS property sets the orientation
        of the text characters in a line. It only affects text in
        vertical mode (when `writing-mode` is not `horizontal-tb`). It
        is useful for controlling the display of languages that use
        vertical script, and also for making vertical table headers.
        **Syntax**: `mixed | upright | sideways`  **Initial value**:
        `mixed`  |  Chrome  | Firefox |  Safari   | Edge | IE  | |
        :------: | :-----: | :-------: | :--: | :-: | |  **48**  |
        **41**  |  **14**   | n/a  | No  | | 11 _-x-_ |         | 5.1
        _-x-_ |      |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-orientation.

    - textOverflow (boolean | number | string | dict | list; optional):
        The **`text-overflow`** CSS property sets how hidden overflow
        content is signaled to users. It can be clipped, display an
        ellipsis ('`…`'), or display a custom string.  **Syntax**: `[
        clip | ellipsis | <string> ]{1,2}`  **Initial value**: `clip`
        | Chrome | Firefox | Safari  |  Edge  |  IE   | | :----: |
        :-----: | :-----: | :----: | :---: | | **1**  |  **7**  |
        **1.3** | **12** | **6** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-overflow.

    - textRendering (a value equal to: 'inherit', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'geometricPrecision', 'optimizeLegibility', 'optimizeSpeed'; optional):
        The **`text-rendering`** CSS property provides information to
        the rendering engine about what to optimize for when rendering
        text.  **Syntax**: `auto | optimizeSpeed | optimizeLegibility
        | geometricPrecision`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari | Edge | IE  | | :----: | :-----: | :----: |
        :--: | :-: | | **4**  |  **1**  | **5**  | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-rendering.

    - textShadow (boolean | number | string | dict | list; optional):
        The **`text-shadow`** CSS property adds shadows to text. It
        accepts a comma-separated list of shadows to be applied to the
        text and any of its `decorations`. Each shadow is described by
        some combination of X and Y offsets from the element, blur
        radius, and color.  **Syntax**: `none | <shadow-t>#`
        **Initial value**: `none`  | Chrome | Firefox | Safari  |
        Edge  |   IE   | | :----: | :-----: | :-----: | :----: |
        :----: | | **2**  | **3.5** | **1.1** | **12** | **10** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-shadow.

    - textSizeAdjust (boolean | number | string | dict | list; optional):
        The **`text-size-adjust`** CSS property controls the text
        inflation algorithm used on some smartphones and tablets.
        Other browsers will ignore this property.  **Syntax**: `none |
        auto | <percentage>`  **Initial value**: `auto` for smartphone
        browsers supporting inflation, `none` in other cases (and then
        not modifiable).  | Chrome | Firefox | Safari |  Edge  | IE  |
        | :----: | :-----: | :----: | :----: | :-: | | **54** |   No
        |   No   | **79** | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-size-adjust.

    - textTransform (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'full-width', 'capitalize', 'full-size-kana', 'lowercase', 'uppercase'; optional):
        The **`text-transform`** CSS property specifies how to
        capitalize an element's text. It can be used to make text
        appear in all-uppercase or all-lowercase, or with each word
        capitalized. It also can help improve legibility for ruby.
        **Syntax**: `none | capitalize | uppercase | lowercase |
        full-width | full-size-kana`  **Initial value**: `none`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-transform.

    - textUnderlineOffset (string | number; optional):
        The **`text-underline-offset`** CSS property sets the offset
        distance of an underline text decoration line (applied using
        `text-decoration`) from its original position.  **Syntax**:
        `auto | <length> | <percentage> `  **Initial value**: `auto`
        | Chrome | Firefox |  Safari  | Edge | IE  | | :----: |
        :-----: | :------: | :--: | :-: | | **87** | **70**  |
        **12.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-underline-offset.

    - textUnderlinePosition (boolean | number | string | dict | list; optional):
        The **`text-underline-position`** CSS property specifies the
        position of the underline which is set using the
        `text-decoration` property's `underline` value.  **Syntax**:
        `auto | from-font | [ under || [ left | right ] ]`  **Initial
        value**: `auto`  | Chrome | Firefox |  Safari  |  Edge  |  IE
        | | :----: | :-----: | :------: | :----: | :---: | | **33** |
        **74**  | **12.1** | **12** | **6** | |        |         | 9
        _-x-_  |        |       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-underline-position.

    - textWrap (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'balance', 'nowrap', 'wrap', 'stable', 'pretty'; optional):
        The **`text-wrap`** CSS property controls how text inside an
        element is wrapped. The different values provide:  **Syntax**:
        `wrap | nowrap | balance | stable | pretty`  **Initial
        value**: `wrap`  | Chrome  | Firefox | Safari | Edge | IE  | |
        :-----: | :-----: | :----: | :--: | :-: | | **114** | **121**
        |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/text-wrap.

    - timelineScope (boolean | number | string | dict | list; optional):
        The **`timeline-scope`** CSS property modifies the scope of a
        named animation timeline.  **Syntax**: `none |
        <dashed-ident>#`  **Initial value**: `none`  | Chrome  |
        Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----: |
        :--: | :-: | | **116** |   No    |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/timeline-scope.

    - top (string | number; optional):
        The **`top`** CSS property participates in specifying the
        vertical position of a positioned element. It has no effect on
        non-positioned elements.  **Syntax**: `<length> | <percentage>
        | auto`  **Initial value**: `auto`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/top.

    - touchAction (boolean | number | string | dict | list; optional):
        The **`touch-action`** CSS property sets how an element's
        region can be manipulated by a touchscreen user (for example,
        by zooming features built into the browser).  **Syntax**:
        `auto | none | [ [ pan-x | pan-left | pan-right ] || [ pan-y |
        pan-up | pan-down ] || pinch-zoom ] | manipulation`  **Initial
        value**: `auto`  | Chrome | Firefox | Safari |  Edge  |    IE
        | | :----: | :-----: | :----: | :----: | :------: | | **36** |
        **52**  | **13** | **12** |  **11**  | |        |         |
        |        | 10 _-x-_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/touch-action.

    - transform (boolean | number | string | dict | list; optional):
        The **`transform`** CSS property lets you rotate, scale, skew,
        or translate an element. It modifies the coordinate space of
        the CSS visual formatting model.  **Syntax**: `none |
        <transform-list>`  **Initial value**: `none`  | Chrome  |
        Firefox |  Safari   |  Edge  |   IE    | | :-----: | :-----: |
        :-------: | :----: | :-----: | | **36**  | **16**  |   **9**
        | **12** | **10**  | | 1 _-x-_ |         | 3.1 _-x-_ |
        | 9 _-x-_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transform.

    - transformBox (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'border-box', 'content-box', 'fill-box', 'stroke-box', 'view-box'; optional):
        The **`transform-box`** CSS property defines the layout box to
        which the `transform`, individual transform properties
        `translate`,`scale`, and `rotate`, and `transform-origin`
        properties relate.  **Syntax**: `content-box | border-box |
        fill-box | stroke-box | view-box`  **Initial value**:
        `view-box`  | Chrome | Firefox | Safari | Edge | IE  | |
        :----: | :-----: | :----: | :--: | :-: | | **64** | **55**  |
        **11** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transform-box.

    - transformOrigin (string | number; optional):
        The **`transform-origin`** CSS property sets the origin for an
        element's transformations.  **Syntax**: `[ <length-percentage>
        | left | center | right | top | bottom ] | [ [
        <length-percentage> | left | center | right ] && [
        <length-percentage> | top | center | bottom ] ] <length>?`
        **Initial value**: `50% 50% 0`  | Chrome  | Firefox | Safari
        |  Edge  |   IE    | | :-----: | :-----: | :-----: | :----: |
        :-----: | | **36**  | **16**  |  **9**  | **12** | **10**  | |
        1 _-x-_ |         | 2 _-x-_ |        | 9 _-x-_ |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transform-origin.

    - transformStyle (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'flat', 'preserve-3d'; optional):
        The **`transform-style`** CSS property sets whether children
        of an element are positioned in the 3D space or are flattened
        in the plane of the element.  **Syntax**: `flat | preserve-3d`
        **Initial value**: `flat`  |  Chrome  | Firefox | Safari  |
        Edge  | IE  | | :------: | :-----: | :-----: | :----: | :-: |
        |  **36**  | **16**  |  **9**  | **12** | No  | | 12 _-x-_ |
        | 4 _-x-_ |        |     |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transform-style.

    - transition (boolean | number | string | dict | list; optional):
        The **`transition`** CSS property is a shorthand property for
        `transition-property`, `transition-duration`,
        `transition-timing-function`, and `transition-delay`.
        **Syntax**: `<single-transition>#`  | Chrome  | Firefox |
        Safari   |  Edge  |   IE   | | :-----: | :-----: | :-------: |
        :----: | :----: | | **26**  | **16**  |   **9**   | **12** |
        **10** | | 1 _-x-_ |         | 3.1 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transition.

    - transitionBehavior (boolean | number | string | dict | list; optional):
        The **`transition-behavior`** CSS property specifies whether
        transitions will be started for properties whose animation
        behavior is discrete.  **Syntax**:
        `<transition-behavior-value>#`  **Initial value**: `normal`  |
        Chrome  | Firefox | Safari | Edge | IE  | | :-----: | :-----:
        | :----: | :--: | :-: | | **117** |   No    |   No   | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transition-behavior.

    - transitionDelay (boolean | number | string | dict | list; optional):
        The **`transition-delay`** CSS property specifies the duration
        to wait before starting a property's transition effect when
        its value changes.  **Syntax**: `<time>#`  **Initial value**:
        `0s`  | Chrome  | Firefox | Safari  |  Edge  |   IE   | |
        :-----: | :-----: | :-----: | :----: | :----: | | **26**  |
        **16**  |  **9**  | **12** | **10** | | 1 _-x-_ |         | 4
        _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transition-delay.

    - transitionDuration (boolean | number | string | dict | list; optional):
        The **`transition-duration`** CSS property sets the length of
        time a transition animation should take to complete. By
        default, the value is `0s`, meaning that no animation will
        occur.  **Syntax**: `<time>#`  **Initial value**: `0s`  |
        Chrome  | Firefox |  Safari   |  Edge  |   IE   | | :-----: |
        :-----: | :-------: | :----: | :----: | | **26**  | **16**  |
        **9**   | **12** | **10** | | 1 _-x-_ |         | 3.1 _-x-_ |
        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transition-duration.

    - transitionProperty (boolean | number | string | dict | list; optional):
        The **`transition-property`** CSS property sets the CSS
        properties to which a transition effect should be applied.
        **Syntax**: `none | <single-transition-property>#`  **Initial
        value**: all  | Chrome  | Firefox |  Safari   |  Edge  |   IE
        | | :-----: | :-----: | :-------: | :----: | :----: | | **26**
        | **16**  |   **9**   | **12** | **10** | | 1 _-x-_ |
        | 3.1 _-x-_ |        |        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transition-property.

    - transitionTimingFunction (boolean | number | string | dict | list; optional):
        The **`transition-timing-function`** CSS property sets how
        intermediate values are calculated for CSS properties being
        affected by a transition effect.  **Syntax**:
        `<easing-function>#`  **Initial value**: `ease`  | Chrome  |
        Firefox |  Safari   |  Edge  |   IE   | | :-----: | :-----: |
        :-------: | :----: | :----: | | **26**  | **16**  |   **9**
        | **12** | **10** | | 1 _-x-_ |         | 3.1 _-x-_ |        |
        |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/transition-timing-function.

    - translate (string | number; optional):
        The **`translate`** CSS property allows you to specify
        translation transforms individually and independently of the
        `transform` property. This maps better to typical user
        interface usage, and saves having to remember the exact order
        of transform functions to specify in the `transform` value.
        **Syntax**: `none | <length-percentage> [ <length-percentage>
        <length>? ]?`  **Initial value**: `none`  | Chrome  | Firefox
        |  Safari  | Edge | IE  | | :-----: | :-----: | :------: |
        :--: | :-: | | **104** | **72**  | **14.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/translate.

    - unicodeBidi (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'isolate', '-moz-isolate', '-moz-isolate-override', '-moz-plaintext', '-webkit-isolate', '-webkit-isolate-override', '-webkit-plaintext', 'bidi-override', 'embed', 'isolate-override', 'plaintext'; optional):
        The **`unicode-bidi`** CSS property, together with the
        `direction` property, determines how bidirectional text in a
        document is handled. For example, if a block of content
        contains both left-to-right and right-to-left text, the
        user-agent uses a complex Unicode algorithm to decide how to
        display the text. The `unicode-bidi` property overrides this
        algorithm and allows the developer to control the text
        embedding.  **Syntax**: `normal | embed | isolate |
        bidi-override | isolate-override | plaintext`  **Initial
        value**: `normal`  | Chrome | Firefox | Safari  |  Edge  |
        IE    | | :----: | :-----: | :-----: | :----: | :-----: | |
        **2**  |  **1**  | **1.3** | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/unicode-bidi.

    - userSelect (a value equal to: 'text', 'inherit', 'none', 'all', 'auto', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'contain', '-moz-none', 'element'; optional):
        The **`user-select`** CSS property controls whether the user
        can select text. This doesn't have any effect on content
        loaded as part of a browser's user interface (its chrome),
        except in textboxes.  **Syntax**: `auto | text | none |
        contain | all`  **Initial value**: `auto`  | Chrome  | Firefox
        |   Safari    |   Edge   |      IE      | | :-----: | :-----:
        | :---------: | :------: | :----------: | | **54**  | **69**
        | **3** _-x-_ |  **79**  | **10** _-x-_ | | 1 _-x-_ | 1 _-x-_
        |             | 12 _-x-_ |              |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/user-select.

    - vectorEffect (a value equal to: 'inherit', 'none', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'non-scaling-stroke'; optional)

    - verticalAlign (string | number; optional):
        The **`vertical-align`** CSS property sets vertical alignment
        of an inline, inline-block or table-cell box.  **Syntax**:
        `baseline | sub | super | text-top | text-bottom | middle |
        top | bottom | <percentage> | <length>`  **Initial value**:
        `baseline`  | Chrome | Firefox | Safari |  Edge  |  IE   | |
        :----: | :-----: | :----: | :----: | :---: | | **1**  |  **1**
        | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/vertical-align.

    - viewTimeline (boolean | number | string | dict | list; optional):
        The **`view-timeline`** CSS shorthand property is used to
        define a _named view progress timeline_, which is progressed
        through based on the change in visibility of an element (known
        as the _subject_) inside a scrollable element (_scroller_).
        `view-timeline` is set on the subject.  **Syntax**: `[
        <'view-timeline-name'> <'view-timeline-axis'>? ]#`  | Chrome
        | Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----:
        | :--: | :-: | | **115** |   n/a   |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/view-timeline.

    - viewTimelineAxis (boolean | number | string | dict | list; optional):
        The **`view-timeline-axis`** CSS property is used to specify
        the scrollbar direction that will be used to provide the
        timeline for a _named view progress timeline_ animation, which
        is progressed through based on the change in visibility of an
        element (known as the _subject_) inside a scrollable element
        (_scroller_). `view-timeline-axis` is set on the subject. See
        CSS scroll-driven animations for more details.  **Syntax**: `[
        block | inline | x | y ]#`  **Initial value**: `block`  |
        Chrome  | Firefox | Safari | Edge | IE  | | :-----: | :-----:
        | :----: | :--: | :-: | | **115** |   n/a   |   No   | n/a  |
        No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/view-timeline-axis.

    - viewTimelineInset (string | number; optional):
        The **`view-timeline-inset`** CSS property is used to specify
        one or two values representing an adjustment to the position
        of the scrollport (see Scroll container for more details) in
        which the subject element of a _named view progress timeline_
        animation is deemed to be visible. Put another way, this
        allows you to specify start and/or end inset (or outset)
        values that offset the position of the timeline.  **Syntax**:
        `[ [ auto | <length-percentage> ]{1,2} ]#`  **Initial value**:
        `auto`  | Chrome  | Firefox | Safari | Edge | IE  | | :-----:
        | :-----: | :----: | :--: | :-: | | **115** |   No    |   No
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/view-timeline-inset.

    - viewTimelineName (boolean | number | string | dict | list; optional):
        The **`view-timeline-name`** CSS property is used to define
        the name of a _named view progress timeline_, which is
        progressed through based on the change in visibility of an
        element (known as the _subject_) inside a scrollable element
        (_scroller_). `view-timeline` is set on the subject.
        **Syntax**: `none | <dashed-ident>#`  **Initial value**:
        `none`  | Chrome  | Firefox | Safari | Edge | IE  | | :-----:
        | :-----: | :----: | :--: | :-: | | **115** |   n/a   |   No
        | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/view-timeline-name.

    - viewTransitionName (boolean | number | string | dict | list; optional):
        The **`view-transition-name`** CSS property provides the
        selected element with a distinct identifying name (a
        `<custom-ident>`) and causes it to participate in a separate
        view transition from the root view transition — or no view
        transition if the `none` value is specified.  **Syntax**:
        `none | <custom-ident>`  **Initial value**: `none`  | Chrome
        | Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----:
        | :--: | :-: | | **111** |   No    |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/view-transition-name.

    - visibility (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'hidden', 'visible', 'collapse'; optional):
        The **`visibility`** CSS property shows or hides an element
        without changing the layout of a document. The property can
        also hide rows or columns in a `<table>`.  **Syntax**:
        `visible | hidden | collapse`  **Initial value**: `visible`  |
        Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/visibility.

    - whiteSpace (boolean | number | string | dict | list; optional):
        The **`white-space`** CSS property sets how white space inside
        an element is handled.  **Syntax**: `normal | pre | nowrap |
        pre-wrap | pre-line | break-spaces | [
        <'white-space-collapse'> || <'text-wrap'> ||
        <'white-space-trim'> ]`  **Initial value**: `normal`  | Chrome
        | Firefox | Safari |  Edge  |   IE    | | :----: | :-----: |
        :----: | :----: | :-----: | | **1**  |  **1**  | **1**  |
        **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/white-space.

    - whiteSpaceCollapse (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'collapse', 'break-spaces', 'discard', 'preserve', 'preserve-breaks', 'preserve-spaces'; optional):
        The **`white-space-collapse`** CSS property controls how white
        space inside an element is collapsed.  **Syntax**: `collapse |
        discard | preserve | preserve-breaks | preserve-spaces |
        break-spaces`  **Initial value**: `collapse`  | Chrome  |
        Firefox | Safari | Edge | IE  | | :-----: | :-----: | :----: |
        :--: | :-: | | **114** |   No    |   No   | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/white-space-collapse.

    - whiteSpaceTrim (boolean | number | string | dict | list; optional):
        **Syntax**: `none | discard-before || discard-after ||
        discard-inner`  **Initial value**: `none`.

    - widows (boolean | number | string | dict | list; optional):
        The **`widows`** CSS property sets the minimum number of lines
        in a block container that must be shown at the _top_ of a
        page, region, or column.  **Syntax**: `<integer>`  **Initial
        value**: `2`  | Chrome | Firefox | Safari  |  Edge  |  IE   |
        | :----: | :-----: | :-----: | :----: | :---: | | **25** |
        No    | **1.3** | **12** | **8** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/widows.

    - width (string | number; optional):
        The **`width`** CSS property sets an element's width. By
        default, it sets the width of the content area, but if
        `box-sizing` is set to `border-box`, it sets the width of the
        border area.  **Syntax**: `auto | <length> | <percentage> |
        min-content | max-content | fit-content |
        fit-content(<length-percentage>)`  **Initial value**: `auto`
        | Chrome | Firefox | Safari |  Edge  |  IE   | | :----: |
        :-----: | :----: | :----: | :---: | | **1**  |  **1**  | **1**
        | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/width.

    - willChange (boolean | number | string | dict | list; optional):
        The **`will-change`** CSS property hints to browsers how an
        element is expected to change. Browsers may set up
        optimizations before an element is actually changed. These
        kinds of optimizations can increase the responsiveness of a
        page by doing potentially expensive work before they are
        actually required.  **Syntax**: `auto |
        <animateable-feature>#`  **Initial value**: `auto`  | Chrome |
        Firefox | Safari  | Edge | IE  | | :----: | :-----: | :-----:
        | :--: | :-: | | **36** | **36**  | **9.1** | n/a  | No  |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/will-change.

    - wordBreak (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'break-word', 'break-all', 'keep-all'; optional):
        The **`word-break`** CSS property sets whether line breaks
        appear wherever the text would otherwise overflow its content
        box.  **Syntax**: `normal | break-all | keep-all | break-word`
        **Initial value**: `normal`  | Chrome | Firefox | Safari |
        Edge  |   IE    | | :----: | :-----: | :----: | :----: |
        :-----: | | **1**  | **15**  | **3**  | **12** | **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/word-break.

    - wordSpacing (string | number; optional):
        The **`word-spacing`** CSS property sets the length of space
        between words and between tags.  **Syntax**: `normal |
        <length>`  **Initial value**: `normal`  | Chrome | Firefox |
        Safari |  Edge  |  IE   | | :----: | :-----: | :----: | :----:
        | :---: | | **1**  |  **1**  | **1**  | **12** | **6** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/word-spacing.

    - wordWrap (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'normal', 'break-word'; optional):
        The **`overflow-wrap`** CSS property applies to inline
        elements, setting whether the browser should insert line
        breaks within an otherwise unbreakable string to prevent text
        from overflowing its line box.  **Syntax**: `normal |
        break-word`  **Initial value**: `normal`  | Chrome  | Firefox
        |  Safari   |  Edge   | IE  | | :-----: | :-----: | :-------:
        | :-----: | :-: | | **≤80** | **≤72** | **≤13.1** | **≤80** |
        No  |.

    - writingMode (a value equal to: 'inherit', '-moz-initial', 'initial', 'revert', 'revert-layer', 'unset', 'horizontal-tb', 'sideways-lr', 'sideways-rl', 'vertical-lr', 'vertical-rl'; optional):
        The **`writing-mode`** CSS property sets whether lines of text
        are laid out horizontally or vertically, as well as the
        direction in which blocks progress. When set for an entire
        document, it should be set on the root element (`html` element
        for HTML documents).  **Syntax**: `horizontal-tb | vertical-rl
        | vertical-lr | sideways-rl | sideways-lr`  **Initial value**:
        `horizontal-tb`  | Chrome  | Firefox |  Safari   |  Edge  |
        IE   | | :-----: | :-----: | :-------: | :----: | :---: | |
        **48**  | **41**  | **10.1**  | **12** | **9** | | 8 _-x-_ |
        | 5.1 _-x-_ |        |       |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/writing-mode.

    - zIndex (boolean | number | string | dict | list; optional):
        The **`z-index`** CSS property sets the z-order of a
        positioned element and its descendants or flex items.
        Overlapping elements with a larger z-index cover those with a
        smaller one.  **Syntax**: `auto | <integer>`  **Initial
        value**: `auto`  | Chrome | Firefox | Safari |  Edge  |  IE
        | | :----: | :-----: | :----: | :----: | :---: | | **1**  |
        **1**  | **1**  | **12** | **4** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/z-index.

    - zoom (boolean | number | string | dict | list; optional):
        The non-standard **`zoom`** CSS property can be used to
        control the magnification level of an element. `transform:
        scale()` should be used instead of this property, if possible.
        However, unlike CSS Transforms, `zoom` affects the layout size
        of the element.  **Syntax**: `normal | reset | <number> |
        <percentage>`  **Initial value**: `normal`  | Chrome | Firefox
        | Safari  |  Edge  |   IE    | | :----: | :-----: | :-----: |
        :----: | :-----: | | **1**  |   n/a   | **3.1** | **12** |
        **5.5** |
        @,see,https,://developer.mozilla.org/docs/Web/CSS/zoom.

- tabMoves (dict; optional)

    `tabMoves` is a dict with keys:

    - col (number; required)

    - row (number; required)

- tabNavigation (boolean; optional)

- tableClassName (string | list of strings; optional)

- title (string; optional)

- trimDropdown (boolean; optional)

- trimRows (list of numbers; optional)

- trimWhitespace (boolean; optional)

- type (string; optional)

- uncheckedTemplate (string | number; optional)

- undo (boolean; optional)

- validator (string; optional)

- viewportColumnRenderingOffset (number; optional)

- viewportRowRenderingOffset (number; optional)

- visibleRows (number; optional)

- width (string | number; optional)

- wordWrap (boolean; optional)

Note: due to the large number of props for this component,
not all of them appear in the constructor signature, but
they may still be used as keyword arguments."""
    _children_props = ['settings.datePickerConfig.field.offsetParent', 'settings.datePickerConfig.field.attributes{}.ownerElement', 'settings.datePickerConfig.field.nextElementSibling', 'settings.datePickerConfig.field.previousElementSibling', 'settings.datePickerConfig.field.children{}', 'settings.datePickerConfig.field.firstElementChild', 'settings.datePickerConfig.field.lastElementChild', 'settings.datePickerConfig.field.assignedSlot.offsetParent', 'settings.datePickerConfig.field.assignedSlot.attributes{}.ownerElement', 'settings.datePickerConfig.field.assignedSlot.nextElementSibling', 'settings.datePickerConfig.field.assignedSlot.previousElementSibling', 'settings.datePickerConfig.field.assignedSlot.children{}', 'settings.datePickerConfig.field.assignedSlot.firstElementChild', 'settings.datePickerConfig.field.assignedSlot.lastElementChild', 'settings.datePickerConfig.trigger.offsetParent', 'settings.datePickerConfig.trigger.attributes{}.ownerElement', 'settings.datePickerConfig.trigger.nextElementSibling', 'settings.datePickerConfig.trigger.previousElementSibling', 'settings.datePickerConfig.trigger.children{}', 'settings.datePickerConfig.trigger.firstElementChild', 'settings.datePickerConfig.trigger.lastElementChild', 'settings.datePickerConfig.trigger.assignedSlot.offsetParent', 'settings.datePickerConfig.trigger.assignedSlot.attributes{}.ownerElement', 'settings.datePickerConfig.trigger.assignedSlot.nextElementSibling', 'settings.datePickerConfig.trigger.assignedSlot.previousElementSibling', 'settings.datePickerConfig.trigger.assignedSlot.children{}', 'settings.datePickerConfig.trigger.assignedSlot.firstElementChild', 'settings.datePickerConfig.trigger.assignedSlot.lastElementChild', 'settings.datePickerConfig.container.offsetParent', 'settings.datePickerConfig.container.attributes{}.ownerElement', 'settings.datePickerConfig.container.nextElementSibling', 'settings.datePickerConfig.container.previousElementSibling', 'settings.datePickerConfig.container.children{}', 'settings.datePickerConfig.container.firstElementChild', 'settings.datePickerConfig.container.lastElementChild', 'settings.datePickerConfig.container.assignedSlot.offsetParent', 'settings.datePickerConfig.container.assignedSlot.attributes{}.ownerElement', 'settings.datePickerConfig.container.assignedSlot.nextElementSibling', 'settings.datePickerConfig.container.assignedSlot.previousElementSibling', 'settings.datePickerConfig.container.assignedSlot.children{}', 'settings.datePickerConfig.container.assignedSlot.firstElementChild', 'settings.datePickerConfig.container.assignedSlot.lastElementChild', 'datePickerConfig.field.offsetParent', 'datePickerConfig.field.attributes{}.ownerElement', 'datePickerConfig.field.nextElementSibling', 'datePickerConfig.field.previousElementSibling', 'datePickerConfig.field.children{}', 'datePickerConfig.field.firstElementChild', 'datePickerConfig.field.lastElementChild', 'datePickerConfig.field.assignedSlot.offsetParent', 'datePickerConfig.field.assignedSlot.attributes{}.ownerElement', 'datePickerConfig.field.assignedSlot.nextElementSibling', 'datePickerConfig.field.assignedSlot.previousElementSibling', 'datePickerConfig.field.assignedSlot.children{}', 'datePickerConfig.field.assignedSlot.firstElementChild', 'datePickerConfig.field.assignedSlot.lastElementChild', 'datePickerConfig.trigger.offsetParent', 'datePickerConfig.trigger.attributes{}.ownerElement', 'datePickerConfig.trigger.nextElementSibling', 'datePickerConfig.trigger.previousElementSibling', 'datePickerConfig.trigger.children{}', 'datePickerConfig.trigger.firstElementChild', 'datePickerConfig.trigger.lastElementChild', 'datePickerConfig.trigger.assignedSlot.offsetParent', 'datePickerConfig.trigger.assignedSlot.attributes{}.ownerElement', 'datePickerConfig.trigger.assignedSlot.nextElementSibling', 'datePickerConfig.trigger.assignedSlot.previousElementSibling', 'datePickerConfig.trigger.assignedSlot.children{}', 'datePickerConfig.trigger.assignedSlot.firstElementChild', 'datePickerConfig.trigger.assignedSlot.lastElementChild', 'datePickerConfig.container.offsetParent', 'datePickerConfig.container.attributes{}.ownerElement', 'datePickerConfig.container.nextElementSibling', 'datePickerConfig.container.previousElementSibling', 'datePickerConfig.container.children{}', 'datePickerConfig.container.firstElementChild', 'datePickerConfig.container.lastElementChild', 'datePickerConfig.container.assignedSlot.offsetParent', 'datePickerConfig.container.assignedSlot.attributes{}.ownerElement', 'datePickerConfig.container.assignedSlot.nextElementSibling', 'datePickerConfig.container.assignedSlot.previousElementSibling', 'datePickerConfig.container.assignedSlot.children{}', 'datePickerConfig.container.assignedSlot.firstElementChild', 'datePickerConfig.container.assignedSlot.lastElementChild']
    _base_nodes = ['children']
    _namespace = 'dash_handsontable'
    _type = 'HotTable'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, settings=Component.UNDEFINED, activeHeaderClassName=Component.UNDEFINED, allowEmpty=Component.UNDEFINED, allowHtml=Component.UNDEFINED, allowInsertColumn=Component.UNDEFINED, allowInsertRow=Component.UNDEFINED, allowInvalid=Component.UNDEFINED, allowRemoveColumn=Component.UNDEFINED, allowRemoveRow=Component.UNDEFINED, ariaTags=Component.UNDEFINED, autoColumnSize=Component.UNDEFINED, autoRowSize=Component.UNDEFINED, autoWrapCol=Component.UNDEFINED, autoWrapRow=Component.UNDEFINED, bindRowsWithHeaders=Component.UNDEFINED, cell=Component.UNDEFINED, cells=Component.UNDEFINED, checkedTemplate=Component.UNDEFINED, colHeaders=Component.UNDEFINED, collapsibleColumns=Component.UNDEFINED, columnHeaderHeight=Component.UNDEFINED, columns=Component.UNDEFINED, columnSorting=Component.UNDEFINED, columnSummary=Component.UNDEFINED, colWidths=Component.UNDEFINED, commentedCellClassName=Component.UNDEFINED, comments=Component.UNDEFINED, contextMenu=Component.UNDEFINED, copyable=Component.UNDEFINED, copyPaste=Component.UNDEFINED, correctFormat=Component.UNDEFINED, currentColClassName=Component.UNDEFINED, currentHeaderClassName=Component.UNDEFINED, currentRowClassName=Component.UNDEFINED, customBorders=Component.UNDEFINED, data=Component.UNDEFINED, dataSchema=Component.UNDEFINED, dateFormat=Component.UNDEFINED, datePickerConfig=Component.UNDEFINED, defaultDate=Component.UNDEFINED, tabNavigation=Component.UNDEFINED, disableVisualSelection=Component.UNDEFINED, dragToScroll=Component.UNDEFINED, dropdownMenu=Component.UNDEFINED, editor=Component.UNDEFINED, enterBeginsEditing=Component.UNDEFINED, enterMoves=Component.UNDEFINED, fillHandle=Component.UNDEFINED, filter=Component.UNDEFINED, filteringCaseSensitive=Component.UNDEFINED, filters=Component.UNDEFINED, fixedColumnsLeft=Component.UNDEFINED, fixedColumnsStart=Component.UNDEFINED, fixedRowsBottom=Component.UNDEFINED, fixedRowsTop=Component.UNDEFINED, formulas=Component.UNDEFINED, fragmentSelection=Component.UNDEFINED, height=Component.UNDEFINED, hiddenColumns=Component.UNDEFINED, hiddenRows=Component.UNDEFINED, invalidCellClassName=Component.UNDEFINED, imeFastEdit=Component.UNDEFINED, isEmptyCol=Component.UNDEFINED, isEmptyRow=Component.UNDEFINED, label=Component.UNDEFINED, language=Component.UNDEFINED, locale=Component.UNDEFINED, layoutDirection=Component.UNDEFINED, licenseKey=Component.UNDEFINED, manualColumnFreeze=Component.UNDEFINED, manualColumnMove=Component.UNDEFINED, manualColumnResize=Component.UNDEFINED, manualRowMove=Component.UNDEFINED, manualRowResize=Component.UNDEFINED, maxCols=Component.UNDEFINED, maxRows=Component.UNDEFINED, mergeCells=Component.UNDEFINED, minCols=Component.UNDEFINED, minRows=Component.UNDEFINED, minSpareCols=Component.UNDEFINED, minSpareRows=Component.UNDEFINED, multiColumnSorting=Component.UNDEFINED, navigableHeaders=Component.UNDEFINED, nestedHeaders=Component.UNDEFINED, nestedRows=Component.UNDEFINED, noWordWrapClassName=Component.UNDEFINED, numericFormat=Component.UNDEFINED, observeDOMVisibility=Component.UNDEFINED, outsideClickDeselects=Component.UNDEFINED, persistentState=Component.UNDEFINED, placeholder=Component.UNDEFINED, placeholderCellClassName=Component.UNDEFINED, preventOverflow=Component.UNDEFINED, preventWheel=Component.UNDEFINED, readOnly=Component.UNDEFINED, readOnlyCellClassName=Component.UNDEFINED, renderAllColumns=Component.UNDEFINED, renderAllRows=Component.UNDEFINED, renderer=Component.UNDEFINED, rowHeaders=Component.UNDEFINED, rowHeaderWidth=Component.UNDEFINED, rowHeights=Component.UNDEFINED, search=Component.UNDEFINED, selectionMode=Component.UNDEFINED, selectOptions=Component.UNDEFINED, skipColumnOnPaste=Component.UNDEFINED, skipRowOnPaste=Component.UNDEFINED, sortByRelevance=Component.UNDEFINED, source=Component.UNDEFINED, startCols=Component.UNDEFINED, startRows=Component.UNDEFINED, stretchH=Component.UNDEFINED, strict=Component.UNDEFINED, tableClassName=Component.UNDEFINED, tabMoves=Component.UNDEFINED, title=Component.UNDEFINED, trimDropdown=Component.UNDEFINED, trimRows=Component.UNDEFINED, trimWhitespace=Component.UNDEFINED, type=Component.UNDEFINED, uncheckedTemplate=Component.UNDEFINED, undo=Component.UNDEFINED, validator=Component.UNDEFINED, viewportColumnRenderingOffset=Component.UNDEFINED, viewportRowRenderingOffset=Component.UNDEFINED, visibleRows=Component.UNDEFINED, width=Component.UNDEFINED, wordWrap=Component.UNDEFINED, afterAddChild=Component.UNDEFINED, afterAutofill=Component.UNDEFINED, afterBeginEditing=Component.UNDEFINED, afterCellMetaReset=Component.UNDEFINED, afterChange=Component.UNDEFINED, afterChangesObserved=Component.UNDEFINED, afterColumnCollapse=Component.UNDEFINED, afterColumnExpand=Component.UNDEFINED, afterColumnFreeze=Component.UNDEFINED, afterColumnMove=Component.UNDEFINED, afterColumnResize=Component.UNDEFINED, afterColumnSequenceChange=Component.UNDEFINED, afterColumnSort=Component.UNDEFINED, afterColumnUnfreeze=Component.UNDEFINED, afterContextMenuDefaultOptions=Component.UNDEFINED, afterContextMenuHide=Component.UNDEFINED, afterContextMenuShow=Component.UNDEFINED, afterCopy=Component.UNDEFINED, afterCopyLimit=Component.UNDEFINED, afterCreateCol=Component.UNDEFINED, afterCreateRow=Component.UNDEFINED, afterCut=Component.UNDEFINED, afterDeselect=Component.UNDEFINED, afterDestroy=Component.UNDEFINED, afterDetachChild=Component.UNDEFINED, afterDocumentKeyDown=Component.UNDEFINED, afterDrawSelection=Component.UNDEFINED, afterDropdownMenuDefaultOptions=Component.UNDEFINED, afterDropdownMenuHide=Component.UNDEFINED, afterDropdownMenuShow=Component.UNDEFINED, afterFilter=Component.UNDEFINED, afterFormulasValuesUpdate=Component.UNDEFINED, afterGetCellMeta=Component.UNDEFINED, afterGetColHeader=Component.UNDEFINED, afterGetColumnHeaderRenderers=Component.UNDEFINED, afterGetRowHeader=Component.UNDEFINED, afterGetRowHeaderRenderers=Component.UNDEFINED, afterHideColumns=Component.UNDEFINED, afterHideRows=Component.UNDEFINED, afterInit=Component.UNDEFINED, afterLanguageChange=Component.UNDEFINED, afterListen=Component.UNDEFINED, afterLoadData=Component.UNDEFINED, afterMergeCells=Component.UNDEFINED, afterModifyTransformEnd=Component.UNDEFINED, afterModifyTransformFocus=Component.UNDEFINED, afterModifyTransformStart=Component.UNDEFINED, afterMomentumScroll=Component.UNDEFINED, afterNamedExpressionAdded=Component.UNDEFINED, afterNamedExpressionRemoved=Component.UNDEFINED, afterOnCellContextMenu=Component.UNDEFINED, afterOnCellCornerDblClick=Component.UNDEFINED, afterOnCellCornerMouseDown=Component.UNDEFINED, afterOnCellMouseDown=Component.UNDEFINED, afterOnCellMouseOut=Component.UNDEFINED, afterOnCellMouseOver=Component.UNDEFINED, afterOnCellMouseUp=Component.UNDEFINED, afterPaste=Component.UNDEFINED, afterPluginsInitialized=Component.UNDEFINED, afterRedo=Component.UNDEFINED, afterRedoStackChange=Component.UNDEFINED, afterRefreshDimensions=Component.UNDEFINED, afterRemoveCellMeta=Component.UNDEFINED, afterRemoveCol=Component.UNDEFINED, afterRemoveRow=Component.UNDEFINED, afterRender=Component.UNDEFINED, afterRenderer=Component.UNDEFINED, afterRowMove=Component.UNDEFINED, afterRowResize=Component.UNDEFINED, afterRowSequenceChange=Component.UNDEFINED, afterScrollHorizontally=Component.UNDEFINED, afterScrollVertically=Component.UNDEFINED, afterScroll=Component.UNDEFINED, afterSelectColumns=Component.UNDEFINED, afterSelection=Component.UNDEFINED, afterSelectionByProp=Component.UNDEFINED, afterSelectionEnd=Component.UNDEFINED, afterSelectionEndByProp=Component.UNDEFINED, afterSelectionFocusSet=Component.UNDEFINED, afterSelectRows=Component.UNDEFINED, afterSetCellMeta=Component.UNDEFINED, afterSetDataAtCell=Component.UNDEFINED, afterSetDataAtRowProp=Component.UNDEFINED, afterSetSourceDataAtCell=Component.UNDEFINED, afterSheetAdded=Component.UNDEFINED, afterSheetRemoved=Component.UNDEFINED, afterSheetRenamed=Component.UNDEFINED, afterTrimRow=Component.UNDEFINED, afterUndo=Component.UNDEFINED, afterUndoStackChange=Component.UNDEFINED, afterUnhideColumns=Component.UNDEFINED, afterUnhideRows=Component.UNDEFINED, afterUnlisten=Component.UNDEFINED, afterUnmergeCells=Component.UNDEFINED, afterUntrimRow=Component.UNDEFINED, afterUpdateData=Component.UNDEFINED, afterUpdateSettings=Component.UNDEFINED, afterValidate=Component.UNDEFINED, afterViewportColumnCalculatorOverride=Component.UNDEFINED, afterViewportRowCalculatorOverride=Component.UNDEFINED, afterViewRender=Component.UNDEFINED, beforeAddChild=Component.UNDEFINED, beforeAutofill=Component.UNDEFINED, beforeBeginEditing=Component.UNDEFINED, beforeCellAlignment=Component.UNDEFINED, beforeChange=Component.UNDEFINED, beforeChangeRender=Component.UNDEFINED, beforeColumnCollapse=Component.UNDEFINED, beforeColumnExpand=Component.UNDEFINED, beforeColumnFreeze=Component.UNDEFINED, beforeColumnMove=Component.UNDEFINED, beforeColumnResize=Component.UNDEFINED, beforeColumnSort=Component.UNDEFINED, beforeColumnWrap=Component.UNDEFINED, beforeColumnUnfreeze=Component.UNDEFINED, beforeContextMenuSetItems=Component.UNDEFINED, beforeContextMenuShow=Component.UNDEFINED, beforeCopy=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'activeHeaderClassName', 'allowEmpty', 'allowHtml', 'allowInsertColumn', 'allowInsertRow', 'allowInvalid', 'allowRemoveColumn', 'allowRemoveRow', 'ariaTags', 'autoColumnSize', 'autoRowSize', 'autoWrapCol', 'autoWrapRow', 'bindRowsWithHeaders', 'cell', 'checkedTemplate', 'className', 'colHeaders', 'colWidths', 'collapsibleColumns', 'columnHeaderHeight', 'columnSorting', 'columnSummary', 'columns', 'commentedCellClassName', 'comments', 'contextMenu', 'copyPaste', 'copyable', 'correctFormat', 'currentColClassName', 'currentHeaderClassName', 'currentRowClassName', 'customBorders', 'data', 'dataSchema', 'dateFormat', 'datePickerConfig', 'defaultDate', 'disableVisualSelection', 'dragToScroll', 'dropdownMenu', 'editor', 'enterBeginsEditing', 'enterMoves', 'exportData', 'exportDataParams', 'fillHandle', 'filter', 'filteringCaseSensitive', 'filters', 'fixedColumnsLeft', 'fixedColumnsStart', 'fixedRowsBottom', 'fixedRowsTop', 'formulas', 'fragmentSelection', 'height', 'hiddenColumns', 'hiddenRows', 'imeFastEdit', 'invalidCellClassName', 'label', 'language', 'layoutDirection', 'licenseKey', 'locale', 'manualColumnFreeze', 'manualColumnMove', 'manualColumnResize', 'manualRowMove', 'manualRowResize', 'maxCols', 'maxRows', 'mergeCells', 'minCols', 'minRows', 'minSpareCols', 'minSpareRows', 'multiColumnSorting', 'navigableHeaders', 'nestedHeaders', 'nestedRows', 'noWordWrapClassName', 'numericFormat', 'observeDOMVisibility', 'outsideClickDeselects', 'persistentState', 'placeholder', 'placeholderCellClassName', 'preventOverflow', 'preventWheel', 'readOnly', 'readOnlyCellClassName', 'renderAllColumns', 'renderAllRows', 'renderer', 'rowHeaderWidth', 'rowHeaders', 'rowHeights', 'search', 'selectOptions', 'selectionMode', 'settings', 'skipColumnOnPaste', 'skipRowOnPaste', 'sortByRelevance', 'source', 'startCols', 'startRows', 'stretchH', 'strict', 'style', 'tabMoves', 'tabNavigation', 'tableClassName', 'title', 'trimDropdown', 'trimRows', 'trimWhitespace', 'type', 'uncheckedTemplate', 'undo', 'validator', 'viewportColumnRenderingOffset', 'viewportRowRenderingOffset', 'visibleRows', 'width', 'wordWrap']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'activeHeaderClassName', 'allowEmpty', 'allowHtml', 'allowInsertColumn', 'allowInsertRow', 'allowInvalid', 'allowRemoveColumn', 'allowRemoveRow', 'ariaTags', 'autoColumnSize', 'autoRowSize', 'autoWrapCol', 'autoWrapRow', 'bindRowsWithHeaders', 'cell', 'checkedTemplate', 'className', 'colHeaders', 'colWidths', 'collapsibleColumns', 'columnHeaderHeight', 'columnSorting', 'columnSummary', 'columns', 'commentedCellClassName', 'comments', 'contextMenu', 'copyPaste', 'copyable', 'correctFormat', 'currentColClassName', 'currentHeaderClassName', 'currentRowClassName', 'customBorders', 'data', 'dataSchema', 'dateFormat', 'datePickerConfig', 'defaultDate', 'disableVisualSelection', 'dragToScroll', 'dropdownMenu', 'editor', 'enterBeginsEditing', 'enterMoves', 'exportData', 'exportDataParams', 'fillHandle', 'filter', 'filteringCaseSensitive', 'filters', 'fixedColumnsLeft', 'fixedColumnsStart', 'fixedRowsBottom', 'fixedRowsTop', 'formulas', 'fragmentSelection', 'height', 'hiddenColumns', 'hiddenRows', 'imeFastEdit', 'invalidCellClassName', 'label', 'language', 'layoutDirection', 'licenseKey', 'locale', 'manualColumnFreeze', 'manualColumnMove', 'manualColumnResize', 'manualRowMove', 'manualRowResize', 'maxCols', 'maxRows', 'mergeCells', 'minCols', 'minRows', 'minSpareCols', 'minSpareRows', 'multiColumnSorting', 'navigableHeaders', 'nestedHeaders', 'nestedRows', 'noWordWrapClassName', 'numericFormat', 'observeDOMVisibility', 'outsideClickDeselects', 'persistentState', 'placeholder', 'placeholderCellClassName', 'preventOverflow', 'preventWheel', 'readOnly', 'readOnlyCellClassName', 'renderAllColumns', 'renderAllRows', 'renderer', 'rowHeaderWidth', 'rowHeaders', 'rowHeights', 'search', 'selectOptions', 'selectionMode', 'settings', 'skipColumnOnPaste', 'skipRowOnPaste', 'sortByRelevance', 'source', 'startCols', 'startRows', 'stretchH', 'strict', 'style', 'tabMoves', 'tabNavigation', 'tableClassName', 'title', 'trimDropdown', 'trimRows', 'trimWhitespace', 'type', 'uncheckedTemplate', 'undo', 'validator', 'viewportColumnRenderingOffset', 'viewportRowRenderingOffset', 'visibleRows', 'width', 'wordWrap']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(HotTable, self).__init__(children=children, **args)