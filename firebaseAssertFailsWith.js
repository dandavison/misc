// based on https://github.com/firebase/firebase-js-sdk/blob/5a880c666377b14aa7d68fe5e8db42a1b5aaf218/packages/testing/src/api/index.ts#L279
function assertFailsWith(promise, regexp) {
  return promise.then(
    v =>
      Promise.reject(new Error("Expected request to fail, but it succeeded.")),
    err => {
      if (!regexp.match(err.message)) {
        Promise.reject(
          new Error(
            "Error message does not match expected pattern: " + err.message
          )
        );
      }
    }
  );
}

// firebase.prototype.assertFailsWith = assertFailsWith;

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
let myFirstPromise = new Promise((resolve, reject) => {
  // We call resolve(...) when what we were doing asynchronously was successful, and reject(...) when it failed.
  // In this example, we use setTimeout(...) to simulate async code.
  // In reality, you will probably be using something like XHR or an HTML5 API.
  setTimeout(function() {
    resolve("Success!"); // Yay! Everything went well!
  }, 250);
});

// Test: create a promise that raises an error asynchronously
let promise = new Promise((resolve, reject) => {
  setTimeout(function() {
    reject(new Error("AAA"));
  }, 250);
});

assertFailsWith(promise, "/AAA/");
