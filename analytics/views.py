# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from products.models import Product
# from orders.models import Order
# from django.db.models import Sum, Count
# from django.utils import timezone
# from datetime import timedelta
# from products.serializers import ProductSerializer

# class SalesAnalyticsView(viewsets.ViewSet):
#     def list(self, request):
#         supplier = request.user
#         products = Product.objects.filter(supplier=supplier)
#         product_ids = products.values_list('id', flat=True)

#         total_sales = Order.objects.filter(product__in=product_ids).aggregate(Sum('total_price'))['total_price__sum'] or 0
#         total_orders = Order.objects.filter(product__in=product_ids).count()

#         product_sales = []
#         for product in products:
#             product_total = Order.objects.filter(product=product).aggregate(Sum('total_price'))['total_price__sum'] or 0
#             units_sold = Order.objects.filter(product=product).aggregate(Sum('quantity'))['quantity__sum'] or 0
#             product_sales.append({
#                 'product_id': product.id,
#                 'product_name': product.name,
#                 'total_sales': product_total,
#                 'units_sold': units_sold
#             })

#         last_30_days = timezone.now() - timedelta(days=30)
#         monthly_sales = Order.objects.filter(
#             product__in=product_ids,
#             created_at__gte=last_30_days
#         ).values('day_created'=timezone.now() - timedelta(days=30)
#         ).annotate(
#             daily_sales=Sum('total_price'),
#             daily_orders=Count('id')
#         ).order_by('day_created')

#         return Response({
#             'total_sales': total_sales,
#             'total_orders': total_orders,
#             'product_sales': product_sales,
#             'monthly_sales': list(monthly_sales)
#         })

# class InventoryAnalyticsView(viewsets.ViewSet):
#     def list(self, request):
#         supplier = request.user
#         products = Product.objects.filter(supplier=supplier)

#         total_inventory_value = sum(product.stock * product.price for product in products)
#         low_stock_products = Product.objects.filter(supplier=supplier, stock__lt=10)

#         return Response({
#             'total_inventory_value': total_inventory_value,
#             'low_stock_products': ProductSerializer(low_stock_products, many=True).data
#         })

