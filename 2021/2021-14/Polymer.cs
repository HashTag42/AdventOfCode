using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

public class Polymer
{
    private PolymerInstructions Instructions { get; init; }

    private ulong[,] PairBuckets { get; set; }

    private ulong[] ElementBuckets { get; set; }

    // The first possible element is 'A' (ASCII 65)
    private const int constElementOffset = 65;

    // The range of elements is from A-Z
    private const int constElementRange = 26;

    public Polymer(string FilePath)
    {
        this.Instructions = new PolymerInstructions(File.ReadAllLines(FilePath));
        this.PairBuckets = new ulong[constElementRange, constElementRange];
        this.ElementBuckets = new ulong[constElementRange];

        InitializeBuckets(Instructions.Template);
        Debug.WriteLine(PairBucketsToString());
        Debug.WriteLine(ElementBucketsToString());
    }

    public void TakeSteps(int Steps)
    {
        for(int step = 1; step <= Steps; step++)
        {
            Step();
            Debug.WriteLine(PairBucketsToString());
            Debug.WriteLine(ElementBucketsToString());
        }
    }

    private void InitializeBuckets(string Template)
    {
        // Create all possible PairBuckets
        for(int i = 0; i < constElementRange; i++)
        {
            for(int j = 0; j < constElementRange; j++)
            {
                char firstElement  = IndexToElement(i);
                char secondElement = IndexToElement(j);
            }
        }

        // Index of the last character in the Template.
        int lastChar = Template.Length - 1;

        // Parse the Template string to find the pairs
        for(int i = 0; i < lastChar; i++)
        {
            ElementPair currentPair = new ElementPair(Template[i], Template[i+1]);

            // Increment the corresponding pair bucket
            this.PairBuckets[ElementToIndex(Template[i]), ElementToIndex(Template[i+1])]++;

            // Increment the bucket for the first element in the pair
            this.ElementBuckets[ElementToIndex(Template[i])]++;
        }

        // Increment the element bucket for the second element in the last pair
        this.ElementBuckets[ElementToIndex(Template[lastChar])]++;
    }

    private void Step()
    {
        // Create a duplicate bucket of pairs on where to take actions according to each rule
        ulong[,] copyPairBuckets = new ulong[constElementRange,constElementRange];
        Array.Copy(this.PairBuckets, copyPairBuckets, constElementRange * constElementRange);

        for(int i = 0; i < constElementRange; i++)
        {
            for(int j = 0; j < constElementRange; j++)
            {
                foreach(InsertionRule rule in this.Instructions.InsertionRules)
                {
                    // Evaluate if current pair matches a rule
                    char first  = IndexToElement(i);
                    char second = IndexToElement(j);
                    ElementPair currentPair = new ElementPair(first, second);

                    // It's important that we use the original PairBuckets
                    if(currentPair == rule.Pair && this.PairBuckets[i,j] > 0)
                    {
                        Debug.WriteLine("Eureka! currentPair=" + currentPair + ", rule=" + rule);

                        ulong currentCount = this.PairBuckets[i,j];

                        // Substracting the existing pair
                        copyPairBuckets[i,j] -= currentCount;

                        // Incrementing the count for the first pair created by the rule
                        ElementPair firstPair = new ElementPair(currentPair.First, rule.Element);
                        copyPairBuckets[ElementToIndex(firstPair.First), ElementToIndex(firstPair.Second)] += currentCount;

                        // Incrementing the count for the secodn pair created by the rule
                        ElementPair secondPair = new ElementPair(rule.Element, currentPair.Second);
                        copyPairBuckets[ElementToIndex(secondPair.First), ElementToIndex(secondPair.Second)] += currentCount;

                        // Increment the bucket for the inserted element
                        this.ElementBuckets[ElementToIndex(rule.Element)] += currentCount;

                        // If a rule was found, no need to keep looking for other rules
                        break;
                    }
                }
            }
        }
        this.PairBuckets = copyPairBuckets;
    }

    public ulong GetAnswer()
    {
        Array.Sort(this.ElementBuckets);
        Array.Reverse(this.ElementBuckets);

        ulong most  = this.ElementBuckets[0];

        ulong least = 0;
        for(int i = 1; i < constElementRange; i++)
        {
            if(0 != this.ElementBuckets[i])
            {
                least = this.ElementBuckets[i];
            }
        }

        return (most - least);
    }

    public string PairBucketsToString()
    {
        string output = null;

        for(int i = 0; i < constElementRange; i++)
        {
            for(int j = 0; j < constElementRange; j++)
            {
                if(this.PairBuckets[i,j] > 0)
                {
                    char first  = IndexToElement(i);
                    char second = IndexToElement(j);
                    ElementPair pair = new ElementPair(first, second);
                    output += pair + ":" + this.PairBuckets[i,j] + " ";
                }
            }
        }

        return output;
    }

    public string ElementBucketsToString()
    {
        string output = null;

        for(int i = 0; i < constElementRange; i++)
        {
            if(ElementBuckets[i] > 0)
            {
                output += IndexToElement(i) + ":" + ElementBuckets[i] + " ";
            }
        }

        return output;
    }

    private int ElementToIndex(char Element) => (Element - constElementOffset);

    private char IndexToElement(int Index) => ((char)(Index + constElementOffset));
}
