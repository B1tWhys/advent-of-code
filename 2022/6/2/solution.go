package main

func naive(dat []byte) int {
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
