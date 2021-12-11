using System;
using System.IO;
using System.Collections;   // Needed to use the Stack class.
using System.Diagnostics;   // Needed to use the Debug class.

/* --- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10

You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3= 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137= 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?
*/

namespace _2021_10
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine(SolvePuzzle(@".\inputTestValidChunks.txt"));
            // Console.WriteLine(SolvePuzzle(@".\inputTestCorruptedChunks.txt"));
            // Console.WriteLine(SolvePuzzle(@".\inputTest.txt")); // Expected: ?
            Console.WriteLine(SolvePuzzle(@".\input.txt"));     // Expected: ?
        }

        static string SolvePuzzle(string FilePath)
        {
            string[] input= File.ReadAllLines(FilePath);
            string message= null;
            message+= "Using file: " + FilePath + "\n";
            message+= "\t Part 1 answer: " + SolvePart1(input) + "\n";
            message+= "\t Part 2 answer: " + SolvePart2(input) + "\n";
            return message;
        }

        // Part 1: What is the total syntax error score for those errors?

        static string SolvePart1(string[] Input)
        {
            int syntaxErrorScore= 0;
            string analysisResult= null;
            bool isLineAnalyzed= false;
            foreach(string line in Input)
            {
                Debug.Write(line);
                isLineAnalyzed= false;
                Stack myStack= new Stack();
                foreach(char c in line)
                {
                    if(!isLineAnalyzed)
                    {
                        switch(c)
                        {
                            case '(': case '[': case '{': case '<':
                                myStack.Push(c);
                                break;

                            case ')': case ']': case '}': case '>':
                                char top= (char) myStack.Peek();

                                if(!IsCloseValid(top, c)) {
                                    analysisResult= "corrupted";
                                    isLineAnalyzed= true;
                                    syntaxErrorScore+= Score(c);
                                }
                                myStack.Pop();
                                break;
                        }
                    }
                }

                if(!isLineAnalyzed)
                {
                    analysisResult= (myStack.Count > 0) ? "incomplete" : "valid";
                }

                Debug.Write(" : " + analysisResult + '\n');
            }

            return syntaxErrorScore.ToString();
        }

        static bool IsCloseValid(char Top, char C)
        {
            bool result= false;
            if((Top == '(') && (C == ')')) { result = true; }
            if((Top == '[') && (C == ']')) { result = true; }
            if((Top == '{') && (C == '}')) { result = true; }
            if((Top == '<') && (C == '>')) { result = true; }
            return result;
        }

        static int Score(char C)
        {
            int score= 0;
            switch(C)
            {
                case ')': score=     3; break;
                case ']': score=    57; break;
                case '}': score=  1197; break;
                case '>': score= 25137; break;
            }
            return score;
        }

        static string SolvePart2(string[] Input)
        {
            string result= "Answer 2";
            return result;
        }
    }

    public class ChunkPair
    {
        public char OpensWith { get; init; }
        public char ClosesWith { get; init; }

        public bool IsValidClose(char inClosing)
        {
            return (ClosesWith == inClosing ? true: false);
        }

        public ChunkPair(char inOpensWith, char inClosesWith)
        {
            OpensWith= inOpensWith;
            ClosesWith= inClosesWith;
        }
    }
}
