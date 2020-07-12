# ParselScript

### _A programming language for snakes (and Parselmouths)_

<img width=350 src="peluca.jpg">

## How does it work

The language is derived from <a href="https://en.wikipedia.org/wiki/Brainfuck">brainfuck</a>. You have a memory buffer and a pointer. You also have 8 operators to manipulate the values of the memory pointer:

| Operator | BF equivalent   |      What the fuck does it do?
|----------|----------       |-------------
|sss       | > |  increment the data pointer
|sha       | < |    decrement the data pointer 
|sas       | + | increment (increase by one) the byte at the data pointer.
|shs       | - | decrement (decrease by one) the byte at the data pointer.
|saa       | . | output the byte at the data pointer. | |
|ssh       | , | accept one byte of input, storing its value in the byte at the data pointer. | |
|sah       | [ | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching 'shh' command. | |
|shh       | ] | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching 'sah' command. | |

### Examples:

```
@ Prints "hola"

sassassassassassassassassassassahssssassassassassassassasssssassassassassassassassassassasssssassassassassassassassassassassasssssassassasssssasshashashashashashsshhssssassassaasssssssassaashsshsshssaashashsshsshssaasssssssassassaashasassaasassassassassassassassassaashsshsshsshsshsshsshssaashasassassassaassssassaassssassaassssaa
```

```
@ (Pseudo) Random number generator

ssssssssssassassah
    shasassassassassassassassassah
        shasahshasassassssshsshhsssssssahssssssshhsassssssssassah
            shssahshssssssssasshashashasahshasahshashashhshasassssshhssssahssssahssssssshhshhshh
            shasahsssssssahshsshhshhssssahssssahshsshashashhssssahshasasshashhshhsasshasha
        shhshasahssssasshashsshhssssssshs
    shhshasaasahshsshhssssss
shh
```

<a href="https://fatiherikli.github.io/brainfuck-visualizer/">If you want to visualize the execution of a brainfuck program I recommend you to check out this awesome visualizer.</a>

## How to use?

- On this repo you have an interpreter (written in Python, obviously)
- Clone the repo
- Run `python3 parsel.py <inputProgram.ps>`
- There are also a couple examples written in parselScript on this repo.

## Building and testing

<img src="iso-certificate.png">

## License

Honestly, do what the fuck you want

<a href="LICENSE"> WTFPL </a>

## Future plans

Fuck I hope I never get so much bored to come here again.