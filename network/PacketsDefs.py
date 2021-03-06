

class PacketsDefs:

    @staticmethod
    def getLenght(packet_id):
        LENGTH = { 0 : 104, 1 : 5, 2 : 7, 3 : False, 4 : 2, 5 : 5, 6 : 5,
                    7 : 7, 8 : 15, 9 : 5, 10 : 11, 11 : 266, 12 : False, 13 : 3,
                    14 : False, 15 : 61, 16 : 215, 17 : False, 18 : False, 19 : 10, 20 : 6,
                    21 : 9, 22 : 1, 23 : False, 24 : False, 25 : False, 26 : False, 27 : 37,
                    28 : False, 29 : 5, 30 : 4, 30 : 8, 32 : 19, 33 : 8, 34 : 3,
                    35 : 26, 36 : 7, 37 : 21, 38 : 5, 39 : 2, 40 : 5, 41 : 1,
                    42 : 5, 43 : 2, 44 : 2, 45 : 17, 46 : 15, 47 : 10, 48 : 5,
                    49 : 1, 50 : 2, 51 : 2, 52 : 10, 53 : 653, 54 : False, 55 : 8,
                    56 : 7, 57 : 9, 58 : False, 59 : False, 60 : False, 61 : 2, 62 : 37,
                    63 : False, 64 : 201, 65 : False, 66 : False, 67 : 553, 68 : 713, 69 : 5,
                    70 : False, 71 : 11, 72 : 73, 73 : 93, 74 : 5, 75 : 9, 76 : False,
                    77 : False, 78 : 6, 79 : 2, 80 : False, 81 : False, 82 : False, 83 : 2,
                    84 : 12, 85 : 1, 86 : 11, 87 : 110, 88 : 106, 89 : False, 90 : False,
                    91 : 4, 92 : 2, 93 : 73, 94 : False, 95 : 49, 96 : 5, 97 : 9,
                    98 : 15, 99 : 13, 100 : 1, 101 : 4, 102 : False, 103 : 21, 104 : False,
                    105 : False, 106 : 3, 107 : 9, 108 : 19, 109 : 3, 110 : 14, 111 : False,
                    112 : 28, 113 : False, 114 : 5, 115 : 2, 116 : False, 117 : 35, 118 : 16,
                    119 : 17, 120 : False, 121 : 9, 122 : False, 123 : 2, 124 : False, 125 : 13,
                    126 : 2, 127 : False, 128 : 62, 129 : False, 130 : 2, 131 : 39, 132 : 69,
                    133 : 2, 134 : False, 135 : False, 136 : 66, 137 : False, 138 : False, 139 : False,
                    140 : 11, 141 : False, 142 : False, 143 : False, 144 : 19, 145 : 65, 146 : False,
                    147 : 99, 148 : False, 149 : 9, 150 : False, 151 : 2, 152 : -1, 153 : 26,
                    154 : False, 155 : 258, 156 : 309, 157 : 51, 158 : False, 159 : False, 160 : 3,
                    161 : 9, 162 : 9, 163 : 9, 164 : 149, 165 : False, 166 : False, 167 : 4,
                    168 : False, 169 : False, 170 : 5, 171 : False, 172 : False, 173 : False, 174 : False,
                    175 : 13, 176 : False, 177 : False, 178 : False, 179 : False, 180 : False, 181 : 64,
                    182 : 9, 183 : False, 184 : False, 185 : 3, 186 : 6, 187 : 9, 188 : 3,
                    189 : -1, 190 : False, 191 : -1, 192 : 36, 193 : False, 194 : False, 195 : False,
                    196 : 6, 197 : 203, 198 : 1, 199 : 49, 200 : 2, 201 : 6, 202 : 6,
                    203 : 7, 204 : False, 205 : 1, 206 : False, 207 : 78, 208 : False, 209 : 2,
                    210 : 25, 211 : False, 212 : False, 213 : False, 214 : False, 215 : False, 216 : False,
                    217 : 268, 218 : False, 219 : False, 220 : 9, 221 : 65535, 222 : 1, 223 : 1,
                    224 : 1, 225 : 9, 226 : 10, 227 : 77, 236 : 1, 237 : 1, 239 : 21,
                    240 : -1, 241 : False, 243 : 24, 245 : 21, 248 : 106 }

        return LENGTH[packet_id]