module SquareSum where

squareSum :: [Integer] -> Integer

squareSum [] = 0
squareSum (n:arr) = n^2 + squareSum arr