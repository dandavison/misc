// Change text color
document.querySelectorAll('*').forEach(el => el.style.color = 'black')

// Regex replace
function replaceRegex(regex, replacement) {
    document.body.innerHTML = document.body.innerHTML.replace(new RegExp(regex, 'gi'), replacement);
}

replaceRegex('what is \(?:a|an|the \)?\([^?]+\)\\?', '$1')


// ChatGPT increase code block widths
document.querySelectorAll(".flex .items-start").forEach((el) => el.style.width = "1000px")