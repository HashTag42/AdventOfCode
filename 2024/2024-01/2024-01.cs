// Puzzle: https://adventofcode.com/2024/day/1

using System.Text.RegularExpressions;

// UNCOMMENT ONE OF THE FOLLOWING LINES
var DEBUG = true;
// var DEBUG = false;

// UNCOMMENT ONE OF THE FOLLOWING LINES
// var filename = "input.txt";
var filename = "inputTest.txt";

///////////////////////////////////////////////////////////////////////////////
void main() {
    printDebug(filename);

    List<int> list1 = [], list2 = [];
    Dictionary<int, int> dict1 = [], dict2 = [];

    foreach(string line in File.ReadLines(filename)) {
        // Parse each line into two numbers
        // The regular expression '\d+' matches one or more digits.
        MatchCollection matches = Regex.Matches(line, @"\d+");
        List<int> numbers = [];
        foreach (Match match in matches) {
            numbers.Add(int.Parse(match.Value));
        }
        list1.Add(numbers[0]);
        list2.Add(numbers[1]);
        increaseDictCount(dict1, numbers[0]);
        increaseDictCount(dict2, numbers[1]);
    }

    list1.Sort();
    list2.Sort();
	printDebug(string.Join(", ", list1));
	printDebug(string.Join(", ", list2));
    printDebug(string.Join(", ", dict1));
    printDebug(string.Join(", ", dict2));

    var dif = 0;
    var similarity_score = 0;
    for (var i = 0; i < list1.Count; i++) {
        dif += Math.Abs(list1[i] - list2[i]);
        var factor = 0;
        try {
            factor = dict2[list1[i]];
        }
        catch {
            factor = 0;
        }
        finally {
            similarity_score += list1[i] * factor;
        }
    }

    Console.WriteLine($"Part 1 result: {dif}");
    Console.WriteLine($"Part 2 result: {similarity_score}");
}
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
void increaseDictCount(Dictionary<int,int> dict, int key) {
    var p = 0;
    try {
        p = dict[key];
    }
    catch (KeyNotFoundException) {
        dict[key] = 0;
    }
    finally {
        dict[key] = p+1;
    }
}
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
void printDebug(string text) {
    if(DEBUG) {
        Console.WriteLine($"[DEBUG] {text}");
    }
}
///////////////////////////////////////////////////////////////////////////////

main();