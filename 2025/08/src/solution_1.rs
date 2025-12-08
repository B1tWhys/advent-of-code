use std::{collections::{BinaryHeap, HashSet}, fs::read_to_string, path::PathBuf, str::FromStr};

use ordered_float::OrderedFloat;

#[derive(Debug, PartialEq, Eq, Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
    z: i64
}


#[derive(PartialEq, Eq)]
struct UnionFind {
    parents: Vec<usize>,
    sizes: Vec<usize>,
    positions: Vec<Point>
}


impl Point {
    fn dist(&self, other: &Point) -> OrderedFloat<f32> {
        let sq_dist = (self.x - other.x).pow(2) + (self.y - other.y).pow(2) + (self.z - other.z).pow(2);
        OrderedFloat((sq_dist as f32).sqrt())
    }
}

#[derive(Debug, PartialEq, Eq)]
struct PointParseError;

impl FromStr for Point {
    type Err = PointParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let coords: Vec<i64> = s.trim().splitn(3, ',').map(|i| i.parse().unwrap()).collect();
        let [x, y, z] = coords.try_into().unwrap();
        Ok(Point {x, y, z})
    }
}

impl UnionFind {
    fn from_points(points: &[Point]) -> Self {
        let n = points.len();
        UnionFind { 
            parents: (0..n).collect(), 
            sizes: vec![1; n],
            positions: Vec::from(points)
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parents[x] != x {
            self.parents[x] = self.find(self.parents[x]);
        }

        return self.parents[x];
    }

    fn union(&mut self, x: usize, y: usize) {
        let x = self.find(x);
        let y = self.find(y);
        if x == y {
            return
        }
        let size_x = self.sizes[x];
        let size_y = self.sizes[y];

        if size_x < size_y {
            self.parents[x] = self.parents[y];
            self.sizes[y] += self.sizes[x];
        } else {
            self.parents[y] = self.parents[x];
            self.sizes[x] += self.sizes[y];
        }
    }
}

pub fn solution1(file_path: &PathBuf) {
    let input = read_to_string(file_path).unwrap().trim().to_string();
    let n = input.lines().count();
    let points: Vec<Point> = input.lines().map(|p| p.parse().unwrap()).collect();
    
    let mut distances: BinaryHeap<(OrderedFloat<f32>, (usize, usize))> = BinaryHeap::new();
    for i in 0..n {
        for j in (i+1)..n {
            let dist = points[i].dist(&points[j]);
            distances.push((-dist, (i, j)));
        }
    }

    let mut uf = UnionFind::from_points(&points);
    for _ in 0..1000 {
        if let Some((_, (x, y))) = distances.pop() {
            uf.union(x, y);
        } else {
            break;
        }
    }

    let roots: HashSet<usize> = (0..n).map(|c| uf.find(c)).collect();
    let mut roots = Vec::from_iter(roots.iter().copied());
    roots.sort_by_key(|&c| uf.sizes[c]);
    let ans: usize = roots.iter().rev().take(3).map(|&c| uf.sizes[c]).product();
    println!("The answer is... {ans}");
}
