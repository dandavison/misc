// Change text color
document.querySelectorAll('*').forEach(el => el.style.color = 'black')

// Regex replace
function replaceRegex(regex, replacement) {
    document.body.innerHTML = document.body.innerHTML.replace(new RegExp(regex, 'gi'), replacement);
}

replaceRegex('what is \(?:an|a|the \)?\([^?]+\)\\?', '$1')


// ChatGPT increase code block widths
document.querySelectorAll('.mx-auto, .m-auto').forEach(el => {
    el.style.marginLeft = '0';
    el.style.marginRight = '0';
    el.style.maxWidth = '100%';
});
document.querySelectorAll('.px-3, .md\\:px-4, .lg\\:px-1, .xl\\:px-5, .md\\:px-5').forEach(el => {
    el.style.paddingLeft = '0';
    el.style.paddingRight = '0';
});
document.querySelectorAll('.md\\:max-w-3xl, .lg\\:max-w-\\[40rem\\], .xl\\:max-w-\\[48rem\\]').forEach(el => {
    el.style.maxWidth = '100%';
});

// Facebook make chat window bigger
// Use "javascript:<code>" in a bookmark
function facebookBiggerChatWindow() {
    var els = document.getElementsByClassName('fbDockChatTabFlyout');
    for (var i = 0; i < els.length; i++) { els[i].setAttribute("style", "height:2000px; width:500px") }
}
