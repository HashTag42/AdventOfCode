using System;

public class BinaryString
{
    private string strValue {
        set {
            intValue = 0;
            for(int x = 0; x < value.Length; x++) {
                int cValue = int.Parse(value[x].ToString());
                int power = value.Length - x - 1;
                intValue += cValue * (int) Math.Pow(2, power);
            }
        }
    }

    private int intValue;

    public int ToInt() {
        return intValue;
    }

    public BinaryString(string inStr) {
        strValue = inStr;
    }
}