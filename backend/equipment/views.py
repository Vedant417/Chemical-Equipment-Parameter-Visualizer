from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EquipmentDataset
from .utils import analyze_equipment_csv


class UploadCSVAPIView(APIView):
    """
    API to upload CSV file and return analysis
    """

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "CSV file is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            summary = analyze_equipment_csv(file)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Keep only last 5 uploads
        if EquipmentDataset.objects.count() >= 5:
            EquipmentDataset.objects.first().delete()

        # Save summary in database
        EquipmentDataset.objects.create(
            filename=file.name,
            total_equipment=summary["total_equipment"],
            avg_flowrate=summary["avg_flowrate"],
            avg_pressure=summary["avg_pressure"],
            avg_temperature=summary["avg_temperature"],
        )

        return Response(
            {
                "message": "CSV uploaded and analyzed successfully",
                "summary": summary,
            },
            status=status.HTTP_201_CREATED
        )
    
from .serializers import EquipmentDatasetSerializer


class DatasetHistoryAPIView(APIView):
    """
    API to fetch last 5 uploaded datasets
    """

    def get(self, request):
        datasets = EquipmentDataset.objects.order_by('-uploaded_at')[:5]
        serializer = EquipmentDatasetSerializer(datasets, many=True)
        return Response(serializer.data)
