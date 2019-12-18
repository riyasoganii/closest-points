"""
CSE101: Introduction to Programming
Assignment 3

Name        : Riya Sogani
Roll-no     : 2019442
"""
import math
import random

def dist(p1, p2):
    d=((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
    return d

def sort_points_by_X(points):
    points=sorted(points, key=lambda i:[i[0],i[1]])
    return(points)

def sort_points_by_Y(points):
    points=sorted(points, key=lambda j:[j[1],j[0]])
    return(points)

def naive_closest_pair(plane):
    least_distance=dist(plane[0],plane[1])
    list = [least_distance, plane[0], plane[1]]
    for i in range (len(plane)):
        for j in range (len(plane)):
            if j!=i:
                dist_bw_p1_p2=dist(plane[i],plane[j])
                if dist_bw_p1_p2<least_distance:
                    least_distance=dist_bw_p1_p2
                    p1=plane[i]
                    p2=plane[j]
                    list=[least_distance,p1,p2]
    return list

def closest_pair_in_strip(points, d):
    d_min=d
    return_list=[]
    for i in range (len(points)):
        for j in range (i+1,i+6):
            if j == len(points):
                break
            else:
                new_dist=dist(points[i],points[j])
                if new_dist<d_min:
                    d_min=new_dist
                    p1=points[i]
                    p2=points[j]
                    return_list=[d_min,p1,p2]
    return return_list

def efficient_closest_pair_routine(points):
    return_list = []
    if len(points)==1:
        return return_list
    elif len(points)==2:
        dist_bw_p1_p2=dist(points[0],points[1])
        p1=points[0]
        p2=points[1]
        return_list=[dist_bw_p1_p2,p1,p2]
        return return_list
    else:
        mid_index=len(points)//2
        list_1=points[:mid_index]
        list_2=points[mid_index:]
        return_val_1=efficient_closest_pair_routine(list_1)
        return_val_2=efficient_closest_pair_routine(list_2)

        if (len(return_val_1)!=0) and (len(return_val_2)!=0):
            if (return_val_1[0]) <= (return_val_2[0]):
                d_min = return_val_1[0]
                p1 = return_val_1[1]
                p2 = return_val_1[2]
                return_list = [d_min, p1, p2]
            else:
                d_min = return_val_2[0]
                p1 = return_val_2[1]
                p2 = return_val_2[2]
                return_list = [d_min, p1, p2]
        elif (len(return_val_1)==0):
            return_list= return_val_2
        elif (len(return_val_2)==0):
            return_list= return_val_1

        l=list_2[0]
        x_max=l[0]+return_list[0]
        x_min=l[0]-return_list[0]
        strip_points=[]

        for i in range (len(list_1)):
            if x_min<list_1[i][0]:
                strip_points.append(list_1[i])
        for i in range (len(list_2)):
            if list_2[i][0]<x_max:
                strip_points.append(list_2[i])
        if len(strip_points)==0:
            return return_list
        else:
            strip_points=sort_points_by_Y(strip_points)
            new_closest_pair= closest_pair_in_strip(strip_points,return_list[0])
            if (len(new_closest_pair)!=0):
                return_list=new_closest_pair
            return return_list

def efficient_closest_pair(points):
    sorted_points=sort_points_by_X(points)
    return efficient_closest_pair_routine(sorted_points)

def generate_plane(plane_size, num_pts):
    gen = random.sample(range(plane_size[0] * plane_size[1]), num_pts)
    random_points = [(i % plane_size[0] + 1, i // plane_size[1] + 1) for i in gen]

    return random_points

if __name__ == "__main__":
    num_pts = 10
    plane_size = (10, 10)
    plane = generate_plane(plane_size, num_pts)
    #naive_closest_pair(plane)

points=[(86,65),(44,33),(26,38),(86,67),(94,42),(63,69)]
print(efficient_closest_pair(points))




