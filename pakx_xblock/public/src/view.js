/* eslint-disable no-unused-vars */
/**
 * Initialize the ImageModal student view
 * @param {Object} runtime - The XBlock JS Runtime
 * @param {Object} element - The containing DOM element for this instance of the XBlock
* @param {Object} params - The params passed by XBlock
 * @returns {undefined} nothing
 */
function ModalView(runtime, element, params) {
    /* eslint-enable no-unused-vars */

    _ModalView = this;
    _ModalView.params = params;
    _ModalView.runtime = runtime;
    _ModalView.element = $(element);

    _ModalView.SELECTOR = {
        COUNTER: '.count',
        DEFAULT_PARAGRAPH: 'p',
        LOADING_BAR: '.transparent-bg',
    }

    _ModalView.VIEW = {
        COUNTER: $(_ModalView.SELECTOR.COUNTER, element),
        LOADING_BAR: $(_ModalView.SELECTOR.LOADING_BAR, element),
        DEFAULT_PARAGRAPH: $(_ModalView.SELECTOR.DEFAULT_PARAGRAPH, element)
    }

    _ModalView.URL = {
        GET_STATE: runtime.handlerUrl(element, 'get_state'),
        HANDLE: runtime.handlerUrl(element, 'increment_count')
    }

    $(function ($) {
        /* Here's where you'd do things on page load. */
        _ModalView.init(function(result) {
            if (result) {
                _ModalView.loadUserState(result);
            }
        });

        $(_ModalView.VIEW.DEFAULT_PARAGRAPH).click(function(event) {
            _ModalView.postResults(_ModalView.URL.HANDLE, {hello: 'world'}, function(result){
                _ModalView.updateCounter(result);
            })
        });
    });
}

ModalView.prototype.updateCounter = function(result) {
    _ModalView = this;
    console.log("updating counter")
    _ModalView.VIEW.COUNTER.text(result.count)
}

ModalView.prototype.postResults = function(handlerUrl, data, successCB = null, failureCB = null) {
    _ModalView = this;
    $.ajax({
        type: "POST",
        url: handlerUrl,
        data: JSON.stringify(data),
        success: successCB,
        error: failureCB
    });
}

/**
 * Is student view being displyed in Studio
 * @returns {boolean} False to stop event bubbling
 */
ModalView.prototype.isStudioMode = function() {
    // data-runtime-class is loaded when XBlock has loaded, doesn't work when studio page is refreshed
    return typeof $(".nav-item.nav-course-tools")[0] !== 'undefined'
}

/**
 * Prevent the default event from bubbling up
 * @returns {boolean} False to stop event bubbling
 */
ModalView.prototype.preventDefault = function() {
    return false;
}

ModalView.prototype.init = function(callBack){
    _ModalView = this;
    _ModalView.showLoader();
    $.get(_ModalView.URL.GET_STATE, function (result) {
        if (callBack) {
            callBack(result);
        }
    });
}

ModalView.prototype.loadUserState = function(user_state) {
    /**
    * Load user_state from params Data
    */
    var _ModalView = this;
    console.log("TODO: Update UI as per user state", user_state)
    // Load user state here
    _ModalView.hideLoader();
}


ModalView.prototype.showLoader = function() {
    _ModalView = this;
    _ModalView.VIEW.LOADING_BAR.removeClass('hide');
}

ModalView.prototype.hideLoader = function() {
    _ModalView = this;
    _ModalView.VIEW.LOADING_BAR.addClass('hide');
}
