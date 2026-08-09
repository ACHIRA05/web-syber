from pathlib import Path
import sys
text = Path('index.html').read_text(encoding='utf-8')
start = text.find('<script type="text/babel">')
if start == -1:
    sys.exit('script not found')
start = text.find('const { useState } = React;', start)
end = text.find('</script>', start)
if end == -1:
    sys.exit('end script not found')
script = text[start:end]
for ch in '{}()[]':
    print(ch, script.count(ch))
stack=[]
expected_map = {'}':'{', ')':'(', ']':'['}
for i,ch in enumerate(script):
    if ch in '{([':
        stack.append((ch,i))
    elif ch in '})]':
        if not stack or stack[-1][0] != expected_map[ch]:
            print('mismatch at', i, ch, 'stack last', stack[-1] if stack else None)
            break
        stack.pop()
else:
    print('stack length', len(stack))
