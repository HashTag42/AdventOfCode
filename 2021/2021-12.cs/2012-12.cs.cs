#nullable disable

// var inFile = @".\inputTest1.txt";
// var inFile = @".\inputTest2.txt";
// var inFile = @".\inputTest3.txt";
var inFile = @".\input.txt";

DefaultDict neighbours = new DefaultDict();
int sum = 0;

foreach(string line in File.ReadAllLines(inFile)) {
    string[] substrings = line.Split('-');
    string A = substrings[0];
    string B = substrings[1];
    neighbours.Add(A, B);
    neighbours.Add(B, A);
}

int Count(int Part, List<string> Seen, string Cave) {
    if(Cave == "end") { return 1; }
    if(Seen.Contains(Cave)) {
        if(Cave == "start") { return 0; }
        if(Cave == Cave.ToLower()) {
            if(Part == 1) { return 0; }
            else { Part = 1; }
        }
    }
    Seen.Add(Cave);
    // int sum = 0;
    List<string> theNeighbours = neighbours.GetValues(Cave);
    foreach(string n in theNeighbours) {
        sum += Count(Part, Seen, n);
    }
    return sum;
}

Console.WriteLine($"Using {inFile}:");

List <string> Seen = new List<string>();

Seen.Clear(); sum = 0;
Console.WriteLine(Count(1, Seen, "start"));

Seen.Clear(); sum = 0;
Console.WriteLine(Count(2, Seen, "start"));

