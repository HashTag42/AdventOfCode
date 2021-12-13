// using System;
// using System.Collections.Generic;

// class TransparencyInstructions
// {
//     public List<Dot> Dots { get; init; }
//     public List<FoldInstruction> FoldInstructions { get; init; }

//     public int MaxX { get; init; }
//     public int MaxY { get; init; }

//     public TransparencyInstructions(string[] Lines)
//     {
//         Dots= new List<Dot>();
//         FoldInstructions = new List<FoldInstruction>();

//         MaxX= 0;
//         MaxY= 0;
//         ReadingMode readingMode= ReadingMode.ReadingDots;
//         foreach(string line in Lines)
//         {
//             switch(readingMode)
//             {
//                 case ReadingMode.ReadingDots:
//                     if(line != "")
//                     {
//                         string[] XY= line.Split(',');
//                         int X= int.Parse(XY[0]);
//                         if(X > MaxX) { MaxX= X; }
//                         int Y= int.Parse(XY[1]);
//                         if(Y > MaxY) { MaxY= Y; }
//                         Dot Dot= new Dot(X,Y);
//                         Dots.Add(Dot);
//                     }
//                     else
//                     {
//                         readingMode= ReadingMode.ReadingFoldInstructions;
//                     }
//                     break;

//                 case ReadingMode.ReadingFoldInstructions:
//                     string[] parts= line.Split("fold along ");
//                     string[] parts2= parts[1].Split('=');
//                     string Axis= parts2[0];
//                     int Amount= int.Parse(parts2[1]);
//                     FoldInstruction foldInstruction= new FoldInstruction(Axis, Amount);
//                     FoldInstructions.Add(foldInstruction);
//                     break;
//             }
//         }

//         this.Dots= Dots;
//         this.FoldInstructions= FoldInstructions;
//     }

//     enum ReadingMode { ReadingDots, ReadingFoldInstructions }
// }

// class FoldInstruction
// {
//     public DirectionEnum Direction { get; init; }
//     public int Line { get; init; }

//     public FoldInstruction(string Axis, int Line)
//     {
//         this.Direction= (Axis == "x") ? DirectionEnum.Left: DirectionEnum.Up;
//         this.Line= Line;
//     }

//     public override string ToString()
//     {
//         return (Direction + "=" + Line);
//     }

//     public enum DirectionEnum { Up, Left }
// }

// class Dot
// {
//     public int X { get; init; }
//     public int Y { get; init; }

//     public Dot(int X, int Y)
//     {
//         this.X= X;
//         this.Y= Y;
//     }

//     public override string ToString()
//     {
//         return (X + "," + Y);
//     }
// }