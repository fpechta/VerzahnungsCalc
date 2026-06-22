from django.shortcuts import render, redirect, get_object_or_404
from .models import Gear
from .gear_calculator import calculate_gear


def gear_calculator(request):
    if request.method == 'POST':
        module = float(request.POST.get('module'))
        tooth_count = int(request.POST.get('tooth_count'))
        tooth_count_driven = request.POST.get('tooth_count_driven')
        material = request.POST.get('material')

        tooth_count_driven = int(tooth_count_driven) if tooth_count_driven else None

        gear = Gear(
            module=module,
            tooth_count=tooth_count,
            tooth_count_driven=tooth_count_driven,
            material=material
        )
        gear.save()

        return redirect(f'/?result={gear.id}')

    result = None
    result_gear = None
    result_id = request.GET.get('result')
    if result_id:
        result_gear = Gear.objects.filter(id=result_id).first()
        if result_gear:
            result = calculate_gear(result_gear.module, result_gear.tooth_count)

    gears = Gear.objects.all().order_by('-created_at')

    context = {
        'result': result,
        'result_gear': result_gear,
        'gears': gears,
        'materials': Gear.MATERIAL_CHOICES,
    }
    return render(request, 'gears/calculator.html', context)


def delete_gear(request, gear_id):
    if request.method == 'POST':
        gear = get_object_or_404(Gear, id=gear_id)
        gear.delete()
    return redirect('/')