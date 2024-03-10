import {makeScene2D} from '@motion-canvas/2d';
import {createRef, all, waitFor, DEFAULT} from '@motion-canvas/core';
import {CodeBlock, insert, remove, edit, lines, word} from '@motion-canvas/2d/lib/components/CodeBlock'


export default makeScene2D(function* (view) {
  // Create your animations here

  const codeRef = createRef<CodeBlock>();

  yield view.add(
    <CodeBlock 
      ref={codeRef} 
      language='cpp'
      code={`#include <iostream>

int main()
{
    int a = 0;
    while (a < 10) {
        std::cout << a;
        if (a % 2 == 0) {
            std::cout << " is even\\n";
        } else {
            std::cout << " is odd\\n";
        }
        a += 1;
    }
    return 0;
}`} 
    />,
  );
  yield* waitFor(0.6);

  yield* codeRef().selection([...word(0, 1, 7), ...word(5, 4, 5), ...word(7, 8, 2), ...word(9, 10, 4), ...word(14, 4, 6)], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection([...lines(6, 6), ...lines(8, 8), ...lines(10, 10), ], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection([...lines(5, 5), ...lines(7, 7), ...lines(9, 9), ...lines(12, 12)], 1);
  yield* waitFor(0.6);

  yield* codeRef().selection(DEFAULT, 1);
  yield* waitFor(1.0);
});
