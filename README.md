# SemaWal Semantic network resolver
SemaWal is a semantic network resolver in python

<!--![arrand logo](doc/arrand_header.png  "arrand logo")-->
<!--![PyPI - Downloads](https://img.shields.io/pypi/dm/arrand)-->

  Developpers:  Ali AOUF

Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/40uf411/SemaWal/master/AUTHORS.md)
Release  | 0.1
License  |[Apache 2.0](https://github.com/40uf411/SemaWal/master/LICENSE)
Tracker  |[40uf411/arrand/Issues](https://github.com/40uf411/SemaWal/issues)
Source  |[Github](http://github.com/40uf411/SemaWal)
Feedbacks  |[Comments](https://github.com/40uf411/SemaWal/)
Accounts  |[@Twitter](https://twitter.com/40uf411))

## Description

SemaWal Is a semantic network resolver developed as a python library. It allows the creation of networks through manual coding or a CSV file. It supports many types of connections between nodes.
In addition to extracting knowledge (mainly relations) between two or more nodes in a network, it can find paths between nodes in a given network.




###  مزايا:
* Support for multi-relations(connections between nodes).
* Support for three types of relations: Strict, regular, extend(inheritance).
* Support for CSV files.
* Support for Sub-networks.
* Node functions:
	* Fetch all the related nodes and all the relations that a given node has. 
	* Fetch nodes that are related to a given node.	
	* Fetch relations that relate two given nodes has.
	* Fetch all the relations that a network contains.
	* Fetch all the relations you can get starting from a given node until reaching a given depth.
	* Check if two given nodes are directly connected by a given relation.
	* Check if two given nodes are connected through a path of nodes.
	* Check if two given nodes are connected through a path of nodes by a given relation.
	* Draw a path between two given nodes.

### Usage
<!--
### install
```shell
pip install arrand
```
#### [requirement]
```
pyarabic>=0.6.8
```
-->
#### import
```python
>>> import arrand.arrandom
```
## Examples

Detailed examples and features in [Features](doc/features.md) 



*  Random text
```python
... arrand.arrandom.select()
'هم القوم إن قالوا أصابوا وإن دعوا ... أجابوا وإن أعطوا أطابوا وأجزلوا'
```
*  Select Hadith
```python
... arrand.arrandom.hadith()
'قلت : أرأيت إن تيمم رجل فيمم وجهه في موضع ويمم يديه في موضع آخر ؟ قال : إن تباعد ذلك فليبتدئ التيمم وإن لم يتطاول ذلك وإنما ضرب لوجهه في موضع ثم قام إلى موضع آخر قريب من ذلك فضرب ليديه أيضا وأتم تيممه فإنه يجزئه .'
```
*  Select Aya
```python
... arrand.arrandom.aya()
'6|56|قل إني نهيت أن أعبد الذين تدعون من دون الله قل لا أتبع أهواءكم قد ضللت إذا وما أنا من المهتدين'
```
*  Select Proverb
```python
... arrand.arrandom.proverb()
'غيري يأكل الدجاج وأنا أقع في السياج'
```
*  Select phrase
```python
... arrand.arrandom.phrase()
'قال وكيع عن الأعمش عن خيثمة ، قال : حدثني من سمع عمر بن الخطاب يقول : لا تجزئ صلاة لم يقرأ فيها بفاتحة الكتاب وبشيء معها .'
```
*  Select word
```python
... arrand.arrandom.word()
'قال'
```
*  Select poem
```python
... arrand.arrandom.poem()
'9 وقريض سلا به كل راو # عن حبيب وشاب رأس الوليد'
>>> 
```
*  Sample many
```python
... arrand.arrandom.sample(category = "text", max_length=2, vocalized=False)
['لا تعبدن صنماً في فاقة نزلت ... وازفن بلا حرج للقرد في زمنه', 'فأجابني محمد بن عبد الله بن عبد كان فقال:']
>>> arrand.arrandom.sample(category = "hadith", max_length=2, vocalized=False)
['في حديث عبد الله بن عمرو بن العاص .(1/231)', 'قال : وكان مالك يقول زمانا في رجل ترك القراءة في ركعة في الفريضة : إنه يلغي تلك الركعة بسجدتيها ولا يعتد بها ثم كان آخر قوله أن قال : يسجد لسهوه إذا ترك القراءة في ركعة وأرجو أن تكون مجزئة عنه وما هو عندي بالبين ، قال : وإن قرأ في ركعتين وترك في ركعتين أعاد الصلاة أيضا .(1/136)']
>>> arrand.arrandom.sample(category = "poem", max_length=2, vocalized=False)
['1 من كل سافرة اللثام كأنها # بدر الدجا ونطاقها الجوزاء', '0 فقلت والمقصود قد بان لي # كفي ولا لحم ولا عظم']
```
*  vocalized
```python
>>> arrand.arrandom.sample(category = "text", max_length=2, vocalized=True)
['الأَرْبِعَاءُ 5/2/2014  : /', 'وَتُعْتَبَرُ سَاعَاتُ وُجُودِ الْمُجْتَمَعِ السُّعُودِيِّ عَلَى الْإِنْتَرْنِتِّ ، وَخُصُوصًا الشَّبَابِ الَّتِي تَصِلُ إلَى 20 سَاعَةٍ أُسْبُوعِيًّا وَ13 سَاعَةٍ لِلْفَتَيَاتِ ، عَامِلًا مُحَفِّزًا لِلشَّرِكَاتِ فِي اسْتِهْدَافِهِمْ مِنَ النَّاحِيَةِ التَّسْوِيقِيَّةِ لِلْمُنْتَجَاتِ أوِ الْخَدَمَاتِ عَلَى الْإِنْتَرْنِتِّ.']
>>> arrand.arrandom.sample(category = "hadith", max_length=2, vocalized=True)
['قَالَ : وَقَالَ مَالِكٌ : بَلَغَنِي أَنَّ عُمَرَ بْنَ الْخَطَّابِ وَعَبْدَ اللَّهِ بْنَ عُمَرَ كَانَا يَفْعَلَانِ ذَلِكَ .', 'قُلْتُ : فَهَلْ يُجْزِئُ عِنْدَ مَالِكٍ بَاطِنُ الْخُفِّ مِنْ ظَاهِرِهِ أَوْ ظَاهِرُهُ مِنْ بَاطِنِهِ ؟ قَالَ : لَا وَلَكِنْ لَوْ مَسَحَ رَجُلٌ ظَاهِرَهُ ثُمَّ صَلَّى لَمْ أَرَ عَلَيْهِ الْإِعَادَةَ إلَّا فِي الْوَقْتِ لِأَنَّ عُرْوَةَ بْنَ الزُّبَيْرِ كَانَ يَمْسَحُ ظُهُورَهُمَا وَلَا يَمْسَحُ بُطُونَهُمَا ، أَخْبَرَنَا بِذَلِكَ مَالِكٌ وَأَمَّا فِي الْوَقْتِ فَأَحَبُّ إلَيَّ أَنْ يُعِيدَ مَا دَامَ فِي الْوَقْتِ .']
>>> arrand.arrandom.sample(category = "poem", max_length=2, vocalized=True)
['8 يبلى وبنيان حزني غير منتفض # وأدمعا من جفوني قد جرت علقا', '11 ونعمَ المصطفى من معشر مّا # نجومُ النيراتِ لهمْ كفاء']
```

```python
>>> arrand.arrandom.hadith(vocalized=True)
'قَالَ : وَسُئِلَ مَالِكٌ عَنْ الصِّبْيَانِ يُؤْتَى بِهِمْ إلَى الْمَسَاجِدِ ؟ فَقَالَ : إنْ كَانَ لَا يَعْبَثُ لِصِغَرِهِ وَيَكُفُّ إذَا نُهِيَ فَلَا أَرَى بِهَذَا بَأْسًا ، قَالَ : وَإِنْ كَانَ يَعْبَثُ لِصِغَرِهِ فَلَا أَرَى أَنْ يُؤْتَى بِهِ إلَى الْمَسْجِدِ .'
>>> arrand.arrandom.aya(vocalized=True)
'4|133|إِن يَشَأْ يُذْهِبْكُمْ أَيُّهَا النَّاسُ وَيَأْتِ بِآخَرِينَ وَكَانَ اللَّهُ عَلَى ذَلِكَ قَدِيرًا'
>>> arrand.arrandom.proverb(vocalized=True)
'الظلم مرتعه وخيم'
>>> arrand.arrandom.phrase(vocalized=True)
'قَالَ : وَقَالَ مَالِكٌ : إنْ وَلَغَ الْكَلْبُ فِي إنَاءٍ فِيهِ لَبَنٌ فَلَا بَأْسَ بِأَنْ يُؤْكَلَ ذَلِكَ اللَّبَنُ .'
>>> arrand.arrandom.poem(vocalized=True)
'13 وأخضر مثل سنا العيش النضر # يطوي الفلا وكيف لا وهو الخضر'
>>> 

```
## Non sense texts

```python
... arrand.arrandom.rand_sentences(3)
['اطرحوه في فروع الأشجار؛ وسمعت خفق أوتار العيدان، وترجيع أصوات القيان، فما نفق عنده جلب إليه.', 'يبوخ وإنما يهيج عزة ومنعة، وشياطين خدعة زروع الحمية من هو شر لكم، وأبدلني بكم بدلا، ولكنها النقلة إلى المحسن البريء، فخاف المريب صولة العقاب، كما ترغبون في وجه الكريم على حمار معه حتى تقبل قولي، فقال لهم: لا يأمنان أن تزكي نفسك، وهديت فيه الحجاج، فلما قدم معاوية وخلى بينه وبينه.', 'راعى ضأن والله؟ وهل تجب الزكاة على وجه المهدي بدوام البحث، وطول تجربته في خيره.']
```
*  Select non sense text
```python
... arrand.arrandom.rand_sentence()
'يدفنه، فقاتلوا في سربال ليل ...'

```
### Generate non sense texts from a file
```python
>>> import arrand.builder
>>> mygen = arrand.builder.generator("text.txt")
>>> mygen.rand_sentences(2)
['قبل ذلك تهاون المحسن، واجترأ المسيء، وفسد الأمر، وشاركهما في رؤوسهم، يستعدون بها ووبخهم.', 
'الجلوس لناننصفك منه من رسله، ويعمل، فيهم كما تحبون الحياة، ويرغبون في وقيعة ...']

```