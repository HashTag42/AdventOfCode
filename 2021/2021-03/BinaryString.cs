using System;

public class BinaryString
{
    public string strValue { get; set; }

    public int ToInt()
    {
        double value = 0;
        for(int x = 0; x < strValue.Length; x++) {
            int cValue = int.Parse(strValue[x].ToString());
            int power = strValue.Length - x - 1;
            value += cValue * Math.Pow(2, power);
        }
        return (int) value;
    }

    public BinaryString(string inStr) {
        strValue = inStr;
    }
}