// Default Dictionary
var dlookup = new DefaultDictionary<int, int>(() => -1);
Console.WriteLine($"Lookup 5 returns {dlookup[5]}");
// returns -1
dlookup[5] = 10;
Console.WriteLine($"Assigning to 5 OK - now returns {dlookup[5]}");
// returns 10