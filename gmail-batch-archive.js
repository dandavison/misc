function myFunction() {
  var batchSize = 100;
  var threads = GmailApp.search('label:inbox older_than:100d');
  for (var j = 0; j < threads.length; j+=batchSize) {
    GmailApp.moveThreadsToArchive(threads.slice(j, j+batchSize));
  }
}
