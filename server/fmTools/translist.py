# -*- coding: ISO-8859-1 -*-
## translist.py                                           Frank L�beck
## a translation to simplify text strings for searching
##
import string

showtranslation = [
[0, '\x00', ' '] , #  
[1, '\x01', ' '] , #  `
[2, '\x02', ' '] , #  a
[3, '\x03', ' '] , #  b
[4, '\x04', ' '] , #  c
[5, '\x05', ' '] , #  
[6, '\x06', ' '] , #  e
[7, '\x07', ' '] , #  
[8, '\x08', ' '] , #  
[9, '\t', ' '] , #  
[10, '\n', ' '] , #  
[11, '\x0b', ' '] , #  
[12, '\x0c', ' '] , #  
[13, '\r', ' '] , #  
[14, '\x0e', ' '] , #  
[15, '\x0f', ' '] , #  
[16, '\x10', ' '] , #  o
[17, '\x11', ' '] , #  p
[18, '\x12', ' '] , #  q
[19, '\x13', ' '] , #  r
[20, '\x14', ' '] , #  s
[21, '\x15', ' '] , #  t
[22, '\x16', ' '] , #  u
[23, '\x17', ' '] , #  v
[24, '\x18', ' '] , #  w
[25, '\x19', ' '] , #  x
[26, '\x1a', ' '] , #  y
[27, '\x1b', ' '] , #  
[28, '\x1c', ' '] , #  {
[29, '\x1d', ' '] , #  |
[30, '\x1e', ' '] , #  #
[31, '\x1f', ' '] , #  ~
[32, ' ', ' '] , #   
[33, '!', ' '] , #  !
[34, '"', ' '] , #  "
[35, '#', ' '] , #  #
[36, '$', ' '] , #  $
[37, '%', ' '] , #  %
[38, '&', ' '] , #  &
[39, "'", ' '] , #  '
[40, '(', ' '] , #  (
[41, ')', ' '] , #  )
[42, '*', ' '] , #  *
[43, '+', ' '] , #  +
[44, ',', ' '] , #  ,
[45, '-', ' '] , #  -
[46, '.', ' '] , #  .
[47, '/', ' '] , #  /
[48, '0', '0'] , #  0
[49, '1', '1'] , #  1
[50, '2', '2'] , #  2
[51, '3', '3'] , #  3
[52, '4', '4'] , #  4
[53, '5', '5'] , #  5
[54, '6', '6'] , #  6
[55, '7', '7'] , #  7
[56, '8', '8'] , #  8
[57, '9', '9'] , #  9
[58, ':', ' '] , #  :
[59, ';', ' '] , #  ;
[60, '<', ' '] , #  <
[61, '=', ' '] , #  =
[62, '>', ' '] , #  >
[63, '?', ' '] , #  ?
[64, '@', ' '] , #  @
[65, 'A', 'a'] , #  A
[66, 'B', 'b'] , #  B
[67, 'C', 'c'] , #  C
[68, 'D', 'd'] , #  D
[69, 'E', 'e'] , #  E
[70, 'F', 'f'] , #  F
[71, 'G', 'g'] , #  G
[72, 'H', 'h'] , #  H
[73, 'I', 'i'] , #  I
[74, 'J', 'j'] , #  J
[75, 'K', 'k'] , #  K
[76, 'L', 'l'] , #  L
[77, 'M', 'm'] , #  M
[78, 'N', 'n'] , #  N
[79, 'O', 'o'] , #  O
[80, 'P', 'p'] , #  P
[81, 'Q', 'q'] , #  Q
[82, 'R', 'r'] , #  R
[83, 'S', 's'] , #  S
[84, 'T', 't'] , #  T
[85, 'U', 'u'] , #  U
[86, 'V', 'v'] , #  V
[87, 'W', 'w'] , #  W
[88, 'X', 'x'] , #  X
[89, 'Y', 'y'] , #  Y
[90, 'Z', 'z'] , #  Z
[91, '[', ' '] , #  [
[92, '\\', ' '] , #  \
[93, ']', ' '] , #  ]
[94, '^', ' '] , #  ^
[95, '_', ' '] , #  _
[96, '`', ' '] , #  `
[97, 'a', 'a'] , #  a
[98, 'b', 'b'] , #  b
[99, 'c', 'c'] , #  c
[100, 'd', 'd'] , #  d
[101, 'e', 'e'] , #  e
[102, 'f', 'f'] , #  f
[103, 'g', 'g'] , #  g
[104, 'h', 'h'] , #  h
[105, 'i', 'i'] , #  i
[106, 'j', 'j'] , #  j
[107, 'k', 'k'] , #  k
[108, 'l', 'l'] , #  l
[109, 'm', 'm'] , #  m
[110, 'n', 'n'] , #  n
[111, 'o', 'o'] , #  o
[112, 'p', 'p'] , #  p
[113, 'q', 'q'] , #  q
[114, 'r', 'r'] , #  r
[115, 's', 's'] , #  s
[116, 't', 't'] , #  t
[117, 'u', 'u'] , #  u
[118, 'v', 'v'] , #  v
[119, 'w', 'w'] , #  w
[120, 'x', 'x'] , #  x
[121, 'y', 'y'] , #  y
[122, 'z', 'z'] , #  z
[123, '{', ' '] , #  {
[124, '|', ' '] , #  |
[125, '}', ' '] , #  }
[126, '~', ' '] , #  ~
[127, '\x7f', ' '] , #  
[128, '\x80', ' '] , #  �
[129, '\x81', ' '] , #  �
[130, '\x82', ' '] , #  �
[131, '\x83', ' '] , #  �
[132, '\x84', ' '] , #  
[133, '\x85', ' '] , #  
[134, '\x86', ' '] , #  �
[135, '\x87', ' '] , #  �
[136, '\x88', ' '] , #  
[137, '\x89', ' '] , #  �
[138, '\x8a', ' '] , #  �
[139, '\x8b', ' '] , #  �
[140, '\x8c', ' '] , #  �
[142, '\x8e', ' '] , #  
[143, '\x8f', ' '] , #  
[144, '\x90', ' '] , #  
[145, '\x91', ' '] , #  �
[146, '\x92', ' '] , #  �
[147, '\x93', ' '] , #  �
[148, '\x94', ' '] , #  �
[149, '\x95', ' '] , #  �
[150, '\x96', ' '] , #  
[151, '\x97', ' '] , #  
[152, '\x98', ' '] , #  
[153, '\x99', ' '] , #  �
[154, '\x9a', ' '] , #  
[155, '\x9b', ' '] , #  
[156, '\x9c', ' '] , #  
[157, '\x9d', ' '] , #  
[158, '\x9e', ' '] , #  
[159, '\x9f', ' '] , #  
[160, '\xa0', ' '] , #  �
[161, '\xa1', ' '] , #  �
[162, '\xa2', 'c'] , #  �
[163, '\xa3', 'l'] , #  �
[164, '\xa4', 'e'] , #  �
[165, '\xa5', 'y'] , #  �
[166, '\xa6', 's'] , #  �
[167, '\xa7', ' '] , #  �
[168, '\xa8', 's'] , #  �
[169, '\xa9', 'c'] , #  �
[170, '\xaa', 'a'] , #  �
[171, '\xab', ' '] , #  �
[172, '\xac', ' '] , #  �
[173, '\xad', ' '] , #  �
[174, '\xae', ' '] , #  �
[175, '\xaf', ' '] , #  �
[176, '\xb0', ' '] , #  �
[177, '\xb1', ' '] , #  �
[178, '\xb2', ' '] , #  �
[179, '\xb3', ' '] , #  �
[180, '\xb4', 'z'] , #  �
[181, '\xb5', 'm'] , #  �
[182, '\xb6', 'p'] , #  �
[183, '\xb7', ' '] , #  �
[184, '\xb8', 'z'] , #  �
[185, '\xb9', ' '] , #  �
[186, '\xba', 'o'] , #  �
[187, '\xbb', ' '] , #  �
[188, '\xbc', 'o'] , #  �
[189, '\xbd', 'o'] , #  �
[190, '\xbe', 'y'] , #  �
[191, '\xbf', ' '] , #  �
[192, '\xc0', 'a'] , #  �
[193, '\xc1', 'a'] , #  �
[194, '\xc2', 'a'] , #  �
[195, '\xc3', 'a'] , #  �
[196, '\xc4', 'a'] , #  �
[197, '\xc5', 'a'] , #  �
[198, '\xc6', 'a'] , #  �
[199, '\xc7', 'c'] , #  �
[200, '\xc8', 'e'] , #  �
[201, '\xc9', 'e'] , #  �
[202, '\xca', 'e'] , #  �
[203, '\xcb', 'e'] , #  �
[204, '\xcc', 'i'] , #  �
[205, '\xcd', 'i'] , #  �
[206, '\xce', 'i'] , #  �
[207, '\xcf', 'i'] , #  �
[208, '\xd0', 'd'] , #  �
[209, '\xd1', 'n'] , #  �
[210, '\xd2', 'o'] , #  �
[211, '\xd3', 'o'] , #  �
[212, '\xd4', 'o'] , #  �
[213, '\xd5', 'o'] , #  �
[214, '\xd6', 'o'] , #  �
[215, '\xd7', 'x'] , #  �
[216, '\xd8', 'o'] , #  �
[217, '\xd9', 'u'] , #  �
[218, '\xda', 'u'] , #  �
[219, '\xdb', 'u'] , #  �
[220, '\xdc', 'u'] , #  �
[221, '\xdd', 'y'] , #  �
[222, '\xde', 'p'] , #  �
[223, '\xdf', 's'] , #  �
[224, '\xe0', 'a'] , #  �
[225, '\xe1', 'a'] , #  �
[226, '\xe2', 'a'] , #  �
[227, '\xe3', 'a'] , #  �
[228, '\xe4', 'a'] , #  �
[229, '\xe5', 'a'] , #  �
[230, '\xe6', 'a'] , #  �
[231, '\xe7', 'c'] , #  �
[232, '\xe8', 'e'] , #  �
[233, '\xe9', 'e'] , #  �
[234, '\xea', 'e'] , #  �
[235, '\xeb', 'e'] , #  �
[236, '\xec', 'i'] , #  �
[237, '\xed', 'i'] , #  �
[238, '\xee', 'i'] , #  �
[239, '\xef', 'i'] , #  �
[240, '\xf0', 'd'] , #  �
[241, '\xf1', 'n'] , #  �
[242, '\xf2', 'o'] , #  �
[243, '\xf3', 'o'] , #  �
[244, '\xf4', 'o'] , #  �
[245, '\xf5', 'o'] , #  �
[246, '\xf6', 'o'] , #  �
[247, '\xf7', ' '] , #  �
[248, '\xf8', 'o'] , #  �
[249, '\xf9', 'u'] , #  �
[250, '\xfa', 'u'] , #  �
[251, '\xfb', 'u'] , #  �
[252, '\xfc', 'u'] , #  �
[253, '\xfd', 'y'] , #  �
[254, '\xfe', 'p'] , #  �
[255, '\xff', 'y']  #  �
]
translist = string.join(map(lambda x: x[2], showtranslation),'')

