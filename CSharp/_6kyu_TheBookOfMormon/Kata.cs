using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6kyu_TheBookOfMormon
{
    public class Kata
    {
        public static long Mormons(long startingNumber, long reach, long target)
        {
            if (startingNumber > target)
                return 0;

            int missionCount = 0;
            long mormonCount = startingNumber;
            while (mormonCount < target)
            {
                mormonCount += mormonCount * reach;
                missionCount++;
            }
            return missionCount;
        }

        public static long MormonsAlt(long startingNumber, long reach, long target)
        {
            if (startingNumber >= target)
                return 0;

            return 1 + MormonsAlt(startingNumber - startingNumber * reach, reach, target);
        }
    }
}
