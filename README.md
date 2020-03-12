# lexical-analyzer
Using Regex

# Usage
python main.py 'test.c'

```c
//test.c
bool isPowerOfTwo(int x)
{
    // First x in the below expression is
    // for the case when x is 0
    return x && (!(x & (x - 1)));
}
```

Output

```c
<BOOL> : bool
<ID> : isPowerOfTwo
<LEFT_ROUND_B> : (
<INT> : int 
<ID> : x
<RIGHT_ROUND_B> : )
<LEFT_CURLY_B> : {
<SINGLE_COMMENT> : // First x in the below expression is
<SINGLE_COMMENT> : // for the case when x is 0
<RETURN> : return
<ID> : x
<AND> : &&
<LEFT_ROUND_B> : (
<NOT> : !
<LEFT_ROUND_B> : (
<ID> : x
<BITWISE_AND> : &
<LEFT_ROUND_B> : (
<ID> : x
<MINUS> : -
<INTEGRAL_LITERAL> : 1
<RIGHT_ROUND_B> : )
<RIGHT_ROUND_B> : )
<RIGHT_ROUND_B> : )
<SEMICOLON> : ;
<RIGHT_CURLY_B> : }
```