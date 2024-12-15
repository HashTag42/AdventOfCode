// See https://aka.ms/new-console-template for more information

using System.Collections.Generic;
using System.Drawing;
using System.Text.RegularExpressions;

bool DEBUG = true;

string filename;
// filename = "input.txt";
filename = @".\inputTest.txt";
printDebug(filename);

List<int> list1 = [];
List<int> list2 = [];
Dictionary<int, int> dict1 = [];
Dictionary<int, int> dict2 = [];

foreach(string line in File.ReadLines(filename))
{
    string pattern = @"\d+";
    MatchCollection matches = Regex.Matches(line, pattern);
    List<int> numbers = [];
    foreach (Match match in matches)
    {
        numbers.Add(int.Parse(match.Value));
    }
    list1.Add(numbers[0]);
    list2.Add(numbers[1]);

    increaseDictCount(dict1, numbers[0]);
    increaseDictCount(dict2, numbers[1]);
}

void increaseDictCount(Dictionary<int,int> dict, int number)
{
    var p = 0;
    try
    {
        p = dict[number];
    }
    catch
    {
        dict[number] = 0;
    }
    finally
    {
        dict[number] = p+1;
    }
}

void printDebug(string text)
{
    if(DEBUG)
    {
        Console.WriteLine($"[DEBUG] {text}");
    }
    return;
}