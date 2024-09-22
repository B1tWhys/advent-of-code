package main

import (
	"fmt"
	"math/bits"
	"os"
)

func loadInput() []byte {
	dat, err := os.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	return dat
}

func naive(i []byte) int {
	for idx := 0; idx <= len(i)-14; idx++ {
		window := i[idx : idx+14]
		unique := make(map[byte]struct{})

		for _, b := range window {
			unique[b] = struct{}{}
		}

		if len(unique) == 14 {
			return idx + 14
		}
	}
	return -1
}

func stopEarly(dat []byte) int {
	for i := 0; i < len(dat); i++ {
		seen := make(map[byte]bool)
		for j := i; j < i+14; j++ {
			if _, s := seen[dat[j]]; s {
				break
			} else {
				seen[dat[j]] = true
			}
		}
		if len(seen) == 14 {
			return i + 14
		}
	}
	return -1
}

func slidingWindowArr(dat []byte) int {
	left, right, n := 0, 0, len(dat)
	var arr [26]bool
	for right < n-1 {
		right += 1
		var newChar int = int(dat[right] - 'a' - 1)
		for arr[newChar] {
			arr[int(dat[left])-'a'-1] = false
			left += 1
		}
		arr[newChar] = true
		if right-left+1 == 14 {
			return right + 1
		}
	}
	return -1
}

func asMask1(b byte) int32 {
	return 1 << (b - 'a')
}

func slidingWindowBitmap(dat []byte) int {
	left, right, n := 0, 0, len(dat)
	var bitmap int32 = 0
	for right < n-1 {
		right += 1
		newChar := asMask1(dat[right])
		for bitmap&newChar != 0 {
			bitmap &= ^asMask1(dat[left])
			left += 1
		}
		bitmap |= newChar
		if right-left+1 == 14 {
			return right + 1
		}
	}
	return -1
}

func asMask2(b byte) int32 {
	return 1 << (b % 32)
}

func slidingWindowBitmapFancyMask(dat []byte) int {
	left, right, n := 0, 0, len(dat)
	var bitmap int32 = 0
	for right < n-1 {
		right += 1
		newChar := asMask2(dat[right])
		for bitmap&newChar != 0 {
			bitmap &= ^asMask2(dat[left])
			left += 1
		}
		bitmap |= newChar
		if right-left+1 == 14 {
			return right + 1
		}
	}
	return -1
}

func asMask3(b byte) uint32 {
	return 1 << (b % 32)
}

func benny(dat []byte) int {
	var filter uint32 = 0
	for i := 0; i < 13; i++ {
		filter ^= asMask3(dat[i])
	}
	n := len(dat)
	for i := 0; i < n-14; i++ {
		last := asMask3(dat[i+13])
		filter ^= last
		if bits.OnesCount32(filter) == 14 {
			return i + 14
		}
		first := asMask3(dat[i])
		filter ^= first
	}
	return -1
}

func main() {
	slidingWindowBitmap([]byte{1, 2, 3, 4})
	fmt.Printf("Found match at: %v\n", slidingWindowBitmap(loadInput()))
}
