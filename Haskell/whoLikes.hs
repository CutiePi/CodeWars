module Likes where

likes :: [String] -> String
-- TODO

likes [] = "no one likes this"
likes (x:[]) = x ++ " likes this"
likes (x:(y:[])) = x ++ " and " ++ y ++ " like this"
likes (x:(y:(z:[]))) = x ++ ", " ++ y ++ " and " ++ z ++ " like this"
likes (x:(y:names)) = x ++ ", " ++ y ++ " and " ++ show (length names) ++ " others like this"