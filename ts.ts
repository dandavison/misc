interface EditorChanges {
  changes: [string, number, string | number][];
  newIndex: number;
}

function f(edits: EditorChanges): void {
  //   if (edits.changes.length >= 0) {
  //     const [a, b, c] = edits.changes[0];
  //     console.log(a, b);
  //   }
  const [a, b, c] = edits.changes[0];
  console.log(a, b);
}

// const edits: EditorChanges = { changes: [["remove", 1, 1]], newIndex: 1 };
// f(edits)
