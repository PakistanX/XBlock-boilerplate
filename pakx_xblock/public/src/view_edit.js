/* Javascript for PakXFeedbackXBlockEdit. */
function PakXFeedbackXBlockEdit(runtime, element, params) {
    var _PakXFeedbackXBlockEdit = this, USAGE_ID = $(element).attr("data-usage-id") || $(element).data("usage");
    _PakXFeedbackXBlockEdit.runtime = runtime;
    _PakXFeedbackXBlockEdit.element = element;
    _PakXFeedbackXBlockEdit.params = params

    _PakXFeedbackXBlockEdit.URL = {
        SAVE: runtime.handlerUrl(element, 'studio_submit'),
        GET_STATE: runtime.handlerUrl(element, 'get_state')
    }
    _PakXFeedbackXBlockEdit.SELECTOR = {
        TITLE_ID: '#edit_display_name',
        CANCEL_BUTTON: '.cancel-button',
        SAVE_BUTTON: USAGE_ID + '-form',
    }

    _PakXFeedbackXBlockEdit.VIEW = {
        TITLE_ELEMENT: $(_PakXFeedbackXBlockEdit.SELECTOR.TITLE_ID, element),
        CANCEL_BUTTON: $(_PakXFeedbackXBlockEdit.SELECTOR.CANCEL_BUTTON, element),
        SAVE_BUTTON: $(document.getElementById(_PakXFeedbackXBlockEdit.SELECTOR.SAVE_BUTTON)),
    }

    $(function ($) {
        /* Here's where you'd do things on page load. */

        $(_PakXFeedbackXBlockEdit.VIEW.SAVE_BUTTON).submit(function (e) {
            e.preventDefault();
            _PakXFeedbackXBlockEdit.submit(this);
        });

        $(_PakXFeedbackXBlockEdit.VIEW.CANCEL_BUTTON).click(function (e) {
            e.preventDefault();
            _PakXFeedbackXBlockEdit.cancel(this);
        });

       _PakXFeedbackXBlockEdit.updateView(function (response) {
        //TODO: populate data here as per Requirements
        });
    });
}

PakXFeedbackXBlockEdit.prototype.updateView = function (cb) {
    var _PakXFeedbackXBlockEdit = this;

    $.get(_PakXFeedbackXBlockEdit.URL.GET_STATE, function (res) {
        if (cb) {
            cb(res);
        }
    });
}

PakXFeedbackXBlockEdit.prototype.cancel = function (element) {
    var _PakXFeedbackXBlockEdit = this;
    _PakXFeedbackXBlockEdit.runtime.notify('cancel', {});
}

PakXFeedbackXBlockEdit.prototype.submit = function (form) {
    var _PakXFeedbackXBlockEdit = this;
    var payload = _PakXFeedbackXBlockEdit.toJSON(form);
//    _PakXFeedbackXBlockEdit.runtime.notify("save", {state: 'start', message: 'saving'})
    var config = {
        success: function (response) {
//            _PakXFeedbackXBlockEdit.runtime.notify('save', {state: 'end'});
        },
        error: function () {
            _PakXFeedbackXBlockEdit.runtime.notify("error", {"title": "Error saving data",
                            "message": "Failed to save data"});
        }

    }
    _PakXFeedbackXBlockEdit.post(_PakXFeedbackXBlockEdit.URL.SAVE, payload, config);
}

PakXFeedbackXBlockEdit.prototype.toJSON = function (form) {
    var _PakXFeedbackXBlockEdit = this;
//    TODO: Convert XBlock data to JSON here and add in the dict below
    var title = _PakXFeedbackXBlockEdit.VIEW.TITLE_ELEMENT.val();
    return {title: title}
}

PakXFeedbackXBlockEdit.prototype.post = function (url, payload, config = undefined) {
    var _config = {
        url: url,
        type: "POST",
        contentType: false,
        cache: false,
        processData: false,
        data: JSON.stringify(payload)
    };
    _config = $.extend({}, _config, config);
    $.ajax(_config);
}
