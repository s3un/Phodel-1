# from django.shortcuts import render, HttpResponse, redirect
# from . models import News, Comment
# from django import forms
# from news.forms import myComment 


# def news(request):
# 	news = News.objects.all()
# 	args = {'x' : news }
# 	return render(request, 'news/home.html', args)


# def details(request, id):
# 	news = News.objects.get(id=id)

# 	if request.method == "POST" :
# 		form = myComment(request.POST)
# 		if form.is_valid():
# 			model_instance = form.save(commit = False)
# 			# model_instance.timestamp = timezone.now()
# 			Name=form.cleaned_data['Name']
# 			TextField=form.cleaned_data['TextField']
# 			News_Id =form.cleaned_data['News_Id']
# 			model_instance.save()
# 			return redirect('/')

# 	else :
# 		form = myComment()
# 		comment=Comment.objects.filter(News_Id=news.pk)
# 		context={
# 		'form':form,
# 		'new':news, 
# 		# 'comment':comment
# 		}
# 		return render(request, ('news/details.html'), context)

# 	return render(request, 'news/details.html', context)


