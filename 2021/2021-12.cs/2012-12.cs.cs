// Day 12: Passage Pathing
// https://adventofcode.com/2021/day/12
// Expected answer for part 1: 4241
// Expected answer for part 2: 122134

// var inFile = @".\inputTest1.txt";
// var inFile = @".\inputTest2.txt";
// var inFile = @".\inputTest3.txt";
var inFile = @".\input.txt";

DefaultDict<string,string> neighbours = new DefaultDict<string,string>();

foreach(string line in File.ReadAllLines(inFile)) {
    string[] substrings = line.Split('-');
    string A = substrings[0];
    string B = substrings[1];
    neighbours.Add(A, B);
    neighbours.Add(B, A);
}

int Count(int Part, List<string> Seen, string Cave = "start") {
    string s = String.Join(", ", Seen);
    if(Cave == "end") { return 1; }
    if(Seen.Contains(Cave)) {
        if(Cave == "start") { return 0; }
        if(Cave == Cave.ToLower()) {
            if(Part == 1) { return 0; }
            else { Part = 1; }
        }
    }
    Seen.Add(Cave);
    int sum = 0;
    foreach(string n in neighbours.GetValues(Cave)) {
        sum += Count(Part, Seen.ToList(), n);
    }
    return sum;
}

Console.WriteLine("using: " + inFile);
Console.WriteLine(Count(1, new List<string>()));
Console.WriteLine(Count(2, new List<string>()));
