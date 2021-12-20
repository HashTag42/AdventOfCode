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

    public Polymer(string FilePath, int Steps)
    {
        this.Instructions = new PolymerInstructions(File.ReadAllLines(FilePath));
        this.PairBuckets = new ulong[constElementRange, constElementRange];
        this.ElementBuckets = new ulong[constElementRange];

        InitializeBuckets(Instructions.Template);
        Debug.WriteLine(PairBucketsToString());
        Debug.WriteLine(ElementBucketsToString());

        for(int step = 1; step <= Steps; step++)
        {
            Step();
            Debug.WriteLine(PairBucketsToString());
            Debug.WriteLine(ElementBucketsToString());
        }

        Console.WriteLine("Using {0} && {1} steps: Answer = {2}", FilePath, Steps, this.GetAnswer());
    }

    private void InitializeBuckets(string Template)
    {
        // Create all possible PairBuckets
        for(int i = 0; i < constElementRange; i++)
        {
            for(int j = 0; j < constElementRange; j++)
            {
                char firstElement  = (char) (i + constElementOffset);
                char secondElement = (char) (j + constElementOffset);
            }
        }

        // Index of the last character in the Template.
        int lastChar = Template.Length - 1;

        // Parse the Template string to find the pairs
        for(int i = 0; i < lastChar; i++)
        {
            ElementPair currentPair = new ElementPair(Template[i], Template[i+1]);

            // Increment the corresponding pair bucket
            this.PairBuckets[Template[i]-constElementOffset, Template[i+1]-constElementOffset]++;

            // Increment the bucket for the first element in the pair
            this.ElementBuckets[Template[i]-constElementOffset]++;
        }

        // Increment the element bucket for the second element in the last pair
        this.ElementBuckets[Template[lastChar]-constElementOffset]++;
    }

    private void Step()
    {
        ulong[,] copyPairBuckets = new ulong[constElementRange,constElementRange];
        Array.Copy(this.PairBuckets, copyPairBuckets, constElementRange * constElementRange);
        for(int i = 0; i < constElementRange; i++)
        {
            for(int j = 0; j < constElementRange; j++)
            {
                foreach(InsertionRule rule in this.Instructions.InsertionRules)
                {
                    // Evaluate if current pair matches a rule
                    char first  = (char)(i+constElementOffset);
                    char second = (char)(j+constElementOffset);
                    ElementPair currentPair = new ElementPair(first, second);
                    if(currentPair == rule.Pair && this.PairBuckets[i,j] > 0)
                    {
                        Debug.WriteLine("Eureka! currentPair=" + currentPair + ", rule=" + rule);

                        // Substracting the existing pair
                        copyPairBuckets[i,j] -= this.PairBuckets[i,j];

                        // Incrementing the count for the first pair created by the rule
                        ElementPair firstPair = new ElementPair(currentPair.First, rule.Element);
                        copyPairBuckets[firstPair.First-constElementOffset,
                                        firstPair.Second-constElementOffset] += this.PairBuckets[i,j];

                        // Incrementing the count for the secodn pair created by the rule
                        ElementPair secondPair = new ElementPair(rule.Element, currentPair.Second);
                        copyPairBuckets[secondPair.First-constElementOffset,
                                        secondPair.Second-constElementOffset] += this.PairBuckets[i,j];

                        // Increment the bucket for the inserted element
                        this.ElementBuckets[rule.Element-constElementOffset] += this.PairBuckets[i,j];

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
                    char first  = (char)(i+constElementOffset);
                    char second = (char)(j+constElementOffset);
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
                output += (char)(i + constElementOffset) + ":" + ElementBuckets[i] + " ";
            }
        }

        return output;
    }

}
