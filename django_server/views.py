from django.shortcuts import render
from django_server import models
from django_server.models import Land1029
# from django_server.models import DjangoServerLand1029
from django.http import HttpResponse
# from django.contrib.gis.db.models.functions import AsGeoJSON
# from django.contrib.gis.geos import GEOSGeometry
import json
import geopandas as gpd
from shapely.geometry import Point, MultiPoint, MultiPolygon, LineString, Polygon
import random
import geojson
# Create your views here.
def getLand(request):
    if request.method=='POST':
        # print("reques",request.body)
        res = json.loads(request.body)
        # coords = request.POST['coords']
        # gid = request.POST['gid']
        # print(coords,gid)
        # 步骤一：从前端发送的文件中提取出有效的信息：包括有gid和对应的polygon信息
        # 步骤二：利用geopandas提取polygon中的边界点，同时利用边界点画线与从发送的gid中提取出的
        #        的地块的polygon结合成为一个完整的图形后打包成为geojason的文件
        # 步骤三：利用httpresponse对打包的geojason文件进行传
        
        gid = res['gid']
        point_list = res['coords'][0]

        print(gid,point_list)
        # str_from_web = {
        #                 "type": "Feature",
        #                 "properties": {"gid":1},
        #                 "geometry": {
        #                 "type": "Polygon",
        #                 "coordinates": [
        #                 [
        #                     [114.0715722415178, 22.560747605481993],
        #                     [114.0715722415178, 22.539166743670606],
        #                     [114.04333394500827, 22.539166743670606],
        #                     [114.04333394500827, 22.560747605481993],
        #                     [114.0715722415178, 22.560747605481993]
        #                 ]
        #                 ]
        #                 }
        #                 }
        # gid = str_from_web['properties']['gid']
        # point_list = str_from_web['geometry']['coordinates'][0]

        # 任意找两个点画线
        one_line = LineString([point_list[random.randint(0,len(point_list)-1)], point_list[random.randint(0,len(point_list)-1)]])
        # print(one_line)
        one_line_geo = gpd.GeoSeries(one_line)
        one_line_geo.crs = 'EPSG:4326'
        one_line_geo = one_line_geo.to_crs('EPSG:2381')
        # one_line_geo.plot()
        one_line_buffer = one_line_geo.buffer(8)
        one_line_buffer.crs = 'EPSG:2381'
        one_line_buffer = one_line_buffer.to_crs('EPSG:4326')
        # one_line_buffer = Polygon(one_line_buffer[0])
        # one_line_geo.plot()
        # one_line_buffer.plot()
        select_land = Land1029.objects.get(gid=gid)
        select_land_polygon = Polygon(select_land.geom[0])
        # print(select_land_polygon)

        # 提取出了结果
        result_polygon = gpd.GeoSeries(select_land_polygon).difference(one_line_buffer)
        # print(result_polygon)

        properties = {'gid':gid, 'block_name':select_land.block_name, 'block_use':select_land.block_use}
        final_result = geojson.Feature(geometry=result_polygon[0], properties=properties)

        return HttpResponse(json.dumps(final_result,ensure_ascii=False))