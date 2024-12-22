/* tooltip */
$(function () {
    $('[data-bs-toggle="tooltip"]').tooltip()
});

// refresh page
function refresh() {
    window.location.reload()
}
$("#refresh").on('click', function (event) {
    refresh();
});

function showToken() {
    var text = document.getElementById('token');
    text.style.textShadow = '0 0 0 #000';
    this.innerHTML = "Hidden";
    this.setAttribute('onclick','hiddenToken.call(this)')
}

function hiddenToken() {
    var text = document.getElementById('token');
    text.style.textShadow = '0 0 10px #000';
    this.innerHTML = "Visible";
    this.setAttribute('onclick','showToken.call(this)')
}

function pwdView() {
    var x = document.getElementById("new-password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
};

function passwordStrengthCheck() {
  var strength = document.getElementById('strength');
  var strongRegex = new RegExp("^(?=.{14,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
  var mediumRegex = new RegExp("^(?=.{10,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
  var enoughRegex = new RegExp("(?=.{8,}).*", "g");
  var pwd = document.getElementById("new-password");
  if (pwd.value.length == 0) {
    strength.innerHTML = 'Type Password';
  } else if (false == enoughRegex.test(pwd.value)) {
    strength.innerHTML = '<span style="color:green;font-size:12px">Need More Characters</span>';
    $("#updatePassword").attr("disabled", true);
  } else if (strongRegex.test(pwd.value)) {
    strength.innerHTML = '<span style="color:green;font-size:12px">Strong!</span>';
    $("#updatePassword").attr("disabled", false);
  } else if (mediumRegex.test(pwd.value)) {
    strength.innerHTML = '<span style="color:orange;font-size:12px">Medium!</span>';
    $("#updatePassword").attr("disabled", false);
  } else {
    strength.innerHTML = '<span style="color:red;font-size:12px">Weak!</span>';
    $("#updatePassword").attr("disabled", true);
  }
}

$('body').on('click', '#copyBtn', function() {
    var textToCopy = $(this).data('clipboard-text');
    var $tempInput = $('<input>').val(textToCopy);
    $('body').append($tempInput);
    $tempInput.select();
    try {
        document.execCommand("copy");
        var $tips = $(this).siblings('#tips');
        $tips.text("Copied").fadeToggle(300, function() {
            $tips.text("");
        });
    } catch (err) {
        console.error("Unable to copy: ", err);
        $tips.text("Copy error").fadeToggle(300, function() {
            $tips.text("");
        });
    }
    $tempInput.remove();
});

function hasEmpty(jsonObject){
  let flag = true;
  for (var prop in jsonObject) {
    if (prop === "comment") continue;
    let value = jsonObject[prop];
    if (value == ""){
      console.log(prop, ":", value, " <- false");
      let flag = false;
      return flag;
    }
  }
  return flag;
}

// ajax common fn
function showFeedback(element, className, text) {
    element.text(text);
    element.removeClass("d-none text-success text-warning text-danger");
    element.addClass(className);
}

function beforeRequest(messageElement, buttonSelector) {
    messageElement.addClass("d-none");
    $(buttonSelector).attr("disabled", true);
}

function afterRequest(buttonSelector) {
    $(buttonSelector).attr("disabled", false);
}

function handleExtendConfigSwitch(selector, options) {
  $(selector).on("click", function () {
    if ($(this).is(":checked")) {
      $(options.containerId).html(options.configText);
    } else {
      $(options.containerId).empty();
    }
  });
}

function enableSearchButton(enable = true) {
    $("#search").attr("disabled", !enable);
}

function clearSearchMessage() {
    $("#searchMessage").text("").removeClass("text-warning d-none");
}

function displaySearchResults(items) {
    $("table tbody").html(items);
}

function handleError(jqXHR, textStatus, errorThrown) {
    console.error("An error occurred during the search request:", textStatus, errorThrown);
    alert("An error occurred while searching. Please try again later.");
}

function displayEmptyFieldWarning() {
    $("#searchMessage")
        .text("Required field is empty")
        .addClass("text-warning")
        .removeClass("d-none");
}

function addNewInputField() {
    let newItemAdd = `
        <div class="input-group mb-3" id="newItem">
            <input type="text" class="form-control" placeholder='example: push "route 192.168.1.0 255.255.255.0"' name="pushItems[]">
            <span class="input-group-text" id="itemRevoke">
                <i class="bi bi-file-earmark-minus-fill link-danger" style="font-size: 13px; cursor: pointer;"></i>
            </span>
        </div>`;
    $('#newItems').append(newItemAdd);
}

function removeInputField(item) {
    item.parents("#newItem").remove();
}

function showMessage(message, type, content) {
    message.html(`
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${content}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `);
}

function handleSelectChange() {
    $('#allocateIPPos').empty();
    $('#genStaticIPRes').empty();
    var checkbox = $('#allocateIPSwitch');
    if (checkbox.is(':checked')) {
        checkbox.prop('checked', false);
    }
}

$(document).ready(function() {
    var textarea = $('#auto-resize');
    textarea.trigger('input');

    textarea.on('input', function() {
        var scrollHeight = this.scrollHeight;
        if (scrollHeight > parseInt(textarea.css('height'))) {
            textarea.height(scrollHeight);
        }
    });
});

function genRandomStr(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}
