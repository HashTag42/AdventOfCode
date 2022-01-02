// See https://aka.ms/new-console-template for more information

DefaultDict<string, string> dic = new DefaultDict<string, string>();

dic.Add("A", "A1");
dic.Add("C", "C1");
dic.Add("B", "B2");
dic.Add("B", "B1");
dic.Add("A", "A1");
dic.Add("A", "A2");
dic.Add("B", "B1");

Console.WriteLine(dic);

// Expected output
// A: A1 A2
// C: C1
// B: B2 B1
