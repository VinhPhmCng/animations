import {makeScene2D} from '@motion-canvas/2d';
import {createRef, all, waitFor, DEFAULT} from '@motion-canvas/core';
import {CodeBlock, insert, remove, edit, lines, word} from '@motion-canvas/2d/lib/components/CodeBlock'


export default makeScene2D(function* (view) {
  // Create your animations here

  const codeRef = createRef<CodeBlock>();

  yield view.add(
    <CodeBlock 
      ref={codeRef} 
      language='python'
      code={`a = 0
while a < 10:
    print(a, end=" ")
    if a % 2 == 0:
        print("is even")
    else:
        print("is odd")
    a += 1`} 
    />,
  );
  yield* waitFor(0.6);

  yield* codeRef().selection([...word(1, 0, 5), ...word(2, 13, 3), ...word(3, 4, 2), ...word(5, 4, 4)], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection([...word(2, 4, 5), ...word(4, 8, 5), ...word(6, 8, 5)], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection(DEFAULT, 1);
  yield* waitFor(1.0);

  yield* codeRef().selection([...lines(2, 2), ...lines(4, 4), ...lines(6, 6), ], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection([...lines(1, 1), ...lines(3, 3), ...lines(5, 5), ...lines(7, 7)], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection(DEFAULT, 1);
  yield* waitFor(1.0);
});
