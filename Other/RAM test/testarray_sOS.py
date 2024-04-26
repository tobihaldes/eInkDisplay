buffer_black = bytearray(48000)
buffer_red = bytearray(48000)

import gc

mem = gc.mem_free()
import time
print("mem taken by iport time: "+ str(mem-gc.mem_free()))

mem = gc.mem_free()
import micropython
print("mem taken by iport micropython: "+ str(mem-gc.mem_free()))

micropython.mem_info(1)

mem = gc.mem_free()
import framebuf
print("mem taken by iport framebuf: "+ str(mem-gc.mem_free()))

mem = gc.mem_free()
import driver
print("mem taken by iport driver: "+ str(mem-gc.mem_free()))

mem = gc.mem_free()
import tiles
print("mem taken by iport tiles: "+ str(mem-gc.mem_free()))

mem = gc.mem_free()
gc.collect()
print("mem taken by gc.collect: "+ str(mem-gc.mem_free()))

micropython.mem_info(1)

"""
Standard OS
MPY: soft reboot
mem taken by iport time: 16
mem taken by iport micropython: 16
stack: 572 out of 7936
GC: total: 192000, used: 105840, free: 86160
 No. of 1-blocks: 61, 2-blocks: 16, max blk sz: 3000, max free sz: 4996
GC memory layout; from 20011200:
00000000: h=MLhhhhBDhhBTTDBBBBBDhTh===BDBDh====B=BBBBBBTB=BTB=BBBTB=TBTB=B
00000400: h===TB=h===========B=hSShh===================h========h=========
00000800: ========h=======================================================
00000c00: ========h=======================================================
00001000: ========h=h=BAAh=hh=hSSSh==Sh====S...h==........................
00001400: h=======h========.............Sh=.................h===........h=
00001800: =======....................h=................Sh=................
00001c00: .....Sh=.................h===============.......................
       (3 lines all free)
00002c00: ...................................h============================
00003000: ================================================================
00003400: ================================================================
00003800: ================================================================
00003c00: ============================================h===================
00004000: ================================================================
00004400: ================================================================
00004800: ================================================================
00004c00: ================================================================
00005000: ================================================================
00005400: ================================================================
00005800: ================================================================
00005c00: ================================================================
00006000: ================================================================
00006400: ================================================================
00006800: ================================================================
00006c00: ================================================================
00007000: ================================================================
00007400: ================================================================
00007800: ================================================================
00007c00: ================================================================
00008000: ================================================================
00008400: ================================================================
00008800: ================================================================
00008c00: ================================================================
00009000: ================================================================
00009400: ================================================================
00009800: ================================================================
00009c00: ================================================================
0000a000: ================================================================
0000a400: ================================================================
0000a800: ================================================================
0000ac00: ================================================================
0000b000: ================================================================
0000b400: ================================================================
0000b800: ================================================================
0000bc00: ================================================================
0000c000: ================================================================
0000c400: ================================================================
0000c800: ================================================================
0000cc00: ================================================================
0000d000: ================================================================
0000d400: ================================================================
0000d800: ================================================================
0000dc00: ================================================================
0000e000: ================================================================
0000e400: ================================================================
0000e800: ================================================================
0000ec00: ================================================================
0000f000: ================================================================
0000f400: ================================================================
0000f800: ====================================h===========================
0000fc00: ================================================================
00010000: ================================================================
00010400: ================================================================
00010800: ================================================================
00010c00: ================================================================
00011000: ================================================================
00011400: ================================================================
00011800: ================================================================
00011c00: ================================================================
00012000: ================================================================
00012400: ================================================================
00012800: ================================================================
00012c00: ================================================================
00013000: ================================================================
00013400: ================================================================
00013800: ================================================================
00013c00: ================================================================
00014000: ================================================================
00014400: ================================================================
00014800: ================================================================
00014c00: ================================================================
00015000: ================================================================
00015400: ================================================================
00015800: ================================================================
00015c00: ================================================================
00016000: ================================================================
00016400: ================================================================
00016800: ================================================================
00016c00: ================================================================
00017000: ================================================================
00017400: ================================================================
00017800: ================================================================
00017c00: ================================================================
00018000: ================================================================
00018400: ================================================================
00018800: ================================================================
00018c00: ================================================================
00019000: ================================================================
00019400: ================================================================
00019800: ================================================================
00019c00: ================================================================
0001a000: ================================================================
0001a400: ================================================================
0001a800: ================================================================
0001ac00: ================================================================
0001b000: ================================================================
0001b400: ============================....................................
       (77 lines all free)
0002ec00: ................................
"""

    