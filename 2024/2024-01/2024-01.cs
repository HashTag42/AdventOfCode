// Puzzle: https://adventofcode.com/2024/day/1

using System.Text.RegularExpressions;

bool DEBUG = true;

///////////////////////////////////////////////////////////////////////////////
void main() {
    string filename;
    filename = @".\input.txt";
    // filename = @".\inputTest.txt";
    printDebug(filename);

    List<int> list1 = [];
    List<int> list2 = [];
    Dictionary<int, int> dict1 = [];
    Dictionary<int, int> dict2 = [];

    foreach(string line in File.ReadLines(filename)) {
        string pattern = @"\d+";
        MatchCollection matches = Regex.Matches(line, pattern);
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
    for (int i = 0; i < list1.Count; i++) {
        dif += Math.Abs(list1[i] - list2[i]);
        var factor = 0;
        try {
            factor = dict2[list1[i]];
        }
        catch {
            factor = 0;
        }
        finally {
            similarity_score += factor * list1[i];
        }
    }

    Console.WriteLine($"Part 1 result: {dif}");
    Console.WriteLine($"Part 2 result: {similarity_score}");
}
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
void increaseDictCount(Dictionary<int,int> dict, int number) {
    var p = 0;
    try {
        p = dict[number];
    }
    catch (KeyNotFoundException) {
        dict[number] = 0;
    }
    finally {
        dict[number] = p+1;
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