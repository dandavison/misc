function f(edits) {
    //   if (edits.changes.length >= 0) {
    //     const [a, b, c] = edits.changes[0];
    //     console.log(a, b);
    //   }
    var _a = edits.changes[0], a = _a[0], b = _a[1], c = _a[2];
    console.log(a, b);
}
// const edits: EditorChanges = { changes: [["remove", 1, 1]], newIndex: 1 };
// f(edits)
