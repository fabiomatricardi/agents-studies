## _**What All Top AI Labs Are Wrong About.**_ 

_How RLTs Are, For Once, Original Research_ 

_13 min read · Jul 2, 2025_ 

**==> picture [17 x 18] intentionally omitted <==**

_Ignacio de Gregorio Following_ 

**==> picture [540 x 360] intentionally omitted <==**

_Source: Author using GPT-4o_ 

In an industry where most research focuses on improving existing solutions by 1% in hopes of receiving a call from a top AI Lab, _Sakana AI_ , Japan’s top AI Lab _,_ has published a paper that feels like a breath of fresh air coming from Mount Fuji. 

They propose a complete rethink on how we approach teacher distillation, a key component of all top AI labs' playbooks, promising to make the hugely expensive process cheaper and, interestingly, better, all while being as intuitive as research can be. 

Furthermore, the results are highly promising and represent a first in AI: the ability to train stronger models using weaker ones, which was considered impossible. 

Today, you’ll learn the key intuitions behind distillation, you’ll understand the intricate nature of AI training, and why this new method is exciting and different from anything we've seen before. 

## _**Why One of AI’s Pillars is Done Wrong.**_ 

In an industry as hyped and well-capitalized as AI, one would think that everything runs smoothly and is highly optimized. 

## _**A Waste Machine**_ 

Waste is a very real issue here, as AI Labs are continuously under pressure to deliver ‘breakthroughs’ every few months to maintain momentum. 

This trade-off between go-to-market speed and real progress means that timely product shipping is much more important than delivering products that, well, generate revenue or actually improve the status quo. 

In other words, even if your newest model is going to burn your cash reserves to the ground in return for pennies on the dollar, you are still incentivized to ship it and keep momentum around your brand and hope the next funding round allows you to exist for a few more months. 

_In a nutshell, product intelligence (the measure of progress) is simply the only thing that matters; we’ll worry about profits later._ 

But there are limits. 

Even cash-rich OpenAI, the best well-funded AI startup on the planet, with a recent funding round of $40 billion, had to sunset its GPT-4.5 model because it was simply too expensive. 

In fact, all Frontier AI Labs withhold their smartest models because they are too expensive. Luckily, though, there’s a way to release models that offer a significant portion of the performance of top models while requiring a fraction of the cost. 

This technique, known as distillation, has become the primary go-to-market strategy, serving as a structural component of any top AI lab’s business model; most models you interact with today are distilled models. 

_But what are they?_ 

## _**Distillation, the Teacher-Student Method**_ 

In essence, what distillation enables is to distill a model’s capabilities into a smaller package (a smaller model). 

Instead of training a small model from scratch, we train a large (and inefficient to run) model and use it as a teacher for a smaller model, which is the one you eventually receive as a user. 

The key intuition behind this idea is pretty straightforward if we use a human analogy: 

Instead of giving a kid an enormous pile of books and telling them to study everything from scratch, we humans train some among us as teachers and use them to teach kids the material, relieving them from having to figure everything out by themselves. 

_It would be nice if all of us were born with the innate capabilities of Srinivasa Ramanujan and learn everything by ourselves, but that’s not the case for most of us._ 

_The bottom line is clear: it’s easier to learn from someone than to figure it out ourselves. Interestingly, this idea applies beautifully to AI, too._ 

A model learns faster and better if they are taught by another model than if it has to learn everything by itself. And as I was saying, this is the go-to-market strategy AI Labs use: 

o4-mini is a distillation from o4 (unreleased until GPT-5 drops) 

- Gemini 2.5 Flash is a distillation of Gemini 2.5 Pro 

- Claude 4 Sonnet is a distillation of Claude 4 Opus. 

Mistral Medium 3 and Mistral Small 3 are distillations of Mistral Large 3 (unreleased) 

Even those serving as teachers above are most likely students of even larger models that AI Labs don’t disclose because they are too expensive to serve. 

Having understood the importance of distillation, _how does it work?_ Before we answer that, we first need to understand: _how do we train the teacher?_ 

## _**Learning to Imitate Data… and Models**_ 

All Generative AI models, including large language models (LLMs) ubiquitous in our lives, learn by imitation; we train them by showing them a large amount of data and asking them to replicate it. 

The process is straightforward: 

1. We give them a sentence such as: _“A frog is an animal,”_ 

2. We hide (‘mask’ in AI parlance) the last word, ‘animal’, and ask the model the following: 

3. If the sentence starts with _“A frog is an…”_ , _what comes next?_ 

4. The model then assigns a probability to all the words it knows, although we are primarily concerned with the probability it assigns to the correct one, in this case, ‘animal.’ 

5. If the assigned probability to ‘animal’ is low, such as 20%, it means the model is uncertain about what the next word should be, resulting in an 80% error rate, which we then use as a learning signal. In contrast, if the model assigns 99% probability to the word ‘animal’, it means the model is predicting well, and thus the loss is small. 

_Before any statistician comes at me, let me clarify:_ 

_Although models are said to output probabilities, these aren’t real probabilities in the sense that they are not calibrated. But for all intents and purposes, they behave like probabilities and are interpreted as such._ 

And by doing the above next-word predicting exercise for trillions of words, just like that, you get your first LLM, which we usually call ‘base LLM,’ a model that is essentially a great word predictor. 

_This LLM then undergoes additional training to refine behaviors such as refusal to harmful requests, although I won’t cover them as they aren’t particularly relevant to today’s topic._ 

But before we move on, I want to double-click on the crucial idea that will be relevant later that models not only predict one word but also assign probabilities to all the words they know as likely next-word candidates (in the image below, the vocabulary size is 5, with ‘Playground’ being the most likely next word according to this model). 

**==> picture [472 x 408] intentionally omitted <==**

**==> picture [24 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source<br>**----- End of picture text -----**<br>


Moving on, at this point, we have the famous LLMs, sometimes referred to as ‘non-reasoning’ LLMs. 

_In the case of reasoning models, we add a sixth stage called Reinforcement Learning, where we present the LLM with a complex question we know the answer to and instruct the model to try various approaches until it obtains the correct answer._ 

Fully understood how models are trained, it’s important to note that both the trainer and the student are trained this way. That is, in standard distillation, both the teacher and the student have been trained following a very similar process. 

_But why is this relevant?_ 

Simple, because if both models are trained the same way, the student can never be smarter than the teacher. Therefore, the teacher’s “intelligence” represents the upper-bound of the intelligence the student model can aspire to (we’ll soon understand why this is very problematic). 

But as I was saying, the large model is almost always too expensive to run, unofficially destined to become a ‘teacher model’. 

And with all we know now, we are finally ready to understand how distillation is done and why Sakana wants to change the paradigm altogether. 

## _**The Basics of Distillation**_ 

If basic imitation learning, as we have just described above (formally known as ‘cross-entropy’), implies a model imitating its training data to learn from, distillation adds another layer: a model trained via distillation learns to mimic both the training data and a teacher. 

While maintaining the training objective of predicting the next word in the text passages of the training data, we introduce a new training objective: the model will now also imitate the teacher, or more precisely, imitate how the teacher would respond. 

In other words, every prediction the student makes is evaluated in two ways: 

1. The probability it assigned to the ground-truth word (just like any other LLM), 

2. And the difference between the student’s output distribution and the teacher’s output distribution over the next word. 

Focusing on the latter, as we mentioned earlier (previous image), models output their entire word vocabulary ranked by probability of being the next word. 

Thus, besides measuring the probability they assigned to the most likely word (point 1), for the student we also measure the divergence between the teacher's output distribution (the teacher’s word vocabulary ranked by probability) and the student’s, thereby becoming a student of the teacher. 

## _But what does it mean to imitate the teacher’s response distribution?_ 

If we could visualize the distribution of responses of the teacher and the student in two dimensions (this is obviously a huge simplification), then the goal is for the student’s distribution to ‘move into’ the teacher’s. In plain English, the goal is to make the student respond to questions similarly (in both content and style) to how the teacher would, minimizing the ‘divergence’ in the responses: 

**==> picture [450 x 149] intentionally omitted <==**

_Source_ 

_As I was saying, by doing this, we are essentially telling the student to behave like the teacher, or to be clearer, ‘respond similarly to how the teacher would have responded.’_ 

As a result, we get a smaller student who behaves like the teacher without having to be as large and ‘smart’ as the latter; it just needs to pretend to be as smart. 

And the model that emerges from that is the model that we all eventually use in our daily lives. 

## Okay, _but all this for what?_ 

Simply put, Sakana argues that this entire process, which all AI Labs follow religiously, is flawed. 

## _**Reinforcement-Learned Teachers**_ 

## _**The Current Method is Broken**_ 

As we have discussed, while we train teachers to be great reasoners, they aren’t utilized for reasoning but rather as teachers, resulting in a clear distribution shift (we aren’t using them for what they were trained to do). 

Yet, despite having the teacher to be extremely smart (give it a challenging problem, train it to find the correct solution) which makes all the sense if you think about it, that doesn’t mean that same model, which we will never use as a production model and instead as a trainer, will be a good teacher. 

Let me put it another way: human teachers don’t need to be extremely smart as long as they are good at explaining complex concepts, which may sound the same, but it isn’t. 

Therefore, we are spending enormous amounts of money and human capital training larger-than-life models only for them to be used for purposes for which they weren’t explicitly trained for, which, worse off, can be done for much cheaper with one small change. 

That doesn’t sound very efficient. It appears to be quite broken and wasteful. 

So, the proposed idea is simple: _Why don’t we train them to be, well, teachers?_ 

## _**Training Teachers to be Teachers**_ 

Funnily enough, the ‘breakthrough’ here is to train models for what they are going to be used for. 

In Sakana’s new method, we raise the following question: Instead of training teachers to be super bright by just giving them the question and them having to figure out the answer, _what if we provide the teacher both the question and the answer, and train it to “connect the dots”, to explain why the solution is what it is instead of forcing it to find it?_ 

## _But why do that?_ 

Simple, because it’s much easier to explain why something is what it is than prove it, in the same way that a physics teacher can explain Newton’s laws of gravity without having to be as smart as Newton or having to discover the laws of gravity first before explaining them. 

_Therefore, the takeaway is that, instead of training a teacher by how well it can solve problems on its own, we are going to train a teacher by how smart its students become._ 

**==> picture [514 x 196] intentionally omitted <==**

_Source_ 

## _But how do we do that?_ 

Sakana completely upends the teacher’s training. As seen below in an honestly hard-to-follow graph, this training method measures two things to evaluate the quality of a teacher: 

1. rSS reward: Giving the student a question and the teacher’s explanation, see whether it can generate the solution, given both. As researchers describe it, here we are measuring _“an explanation’s usefulness to understand the question’s solution.”_ 

2. rKL reward: Here, we measure how likely the student is to create the explanation for the solution given the question, and how it compares to the teacher's. Here, we reward the teacher whenever the student generates a thought process similar to the teacher’s (essentially, whether the student behaves in a manner consistent with the teacher's). 

**==> picture [273 x 440] intentionally omitted <==**

**==> picture [24 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source<br>**----- End of picture text -----**<br>


In a nutshell, instead of rewarding teachers for finding solutions to problems, we will only reward the teacher when it generates explanations that actually yield a better student outcome, rather than training a huge reasoning model and crossing our fingers that its solutions serve as a good learning signal for students. 

Fine, _but all this for what? Do we actually create better results?_ 

## _**Better and Cheaper**_ 

The answer is yes, absolutely. 

**==> picture [332 x 240] intentionally omitted <==**

_Source_ 

_In layman’s terms, these new teachers are better teachers than models that are much, much larger and smarter than they are._ 

But this method also introduces a first in AI: we can use smaller models to train larger ones. 

Instead of requiring a 100-billion-parameter teacher for a 32-billion-parameter student, Sakana achieves better results with a 7-billion-parameter teacher for the same student model. 

_But how is that possible? How can a dumber model train stronger models?_ 

_Well, because that was really never a hard requisite, in the same way it has never been a requisite for human teaching; a good teacher isn’t necessarily more intelligent than the student, it’s just optimized for teaching._ 

From a technical perspective, this counterintuitive result (dumber teaching smarter) also makes total sense. 

As the teacher is trained using a more straightforward task (explaining a solution instead of finding it), it’s logical that the teacher can get away with being small, and, importantly, smaller than the student. 

In a more technical sense, the teacher’s training objective is simpler than the student’s objective: one has access to the solutions and needs to generate better explanations, whereas the student must figure out the solutions. 

As a result, the teacher’s solution space (the space of possible explanations) is much smoother and easier to learn for. Therefore, we can indeed get away with smaller models doing the teaching job. 

_For the geeks among you seeking a more technical explanation, there’s also a ‘reward-based’ explanation._ 

_Unlike traditional teachers, who are only rewarded when they find the solution, which is a sparsely-rewarded training regime, in the explanation training regime, the rewards are dense, as every part of the explanation is measured by how well the student has internalized it. Put in simpler terms, as teachers only improve when they yield better responses from students, the feedback is immediate and constant._ 

_What this translates to is that, during the training process, the teacher has much higher guidance on what makes a good teacher or not, compared to the traditional method, and thus it’s trivial to see why the outcome is a better teacher._ 

## _**Common Sense**_ 

Ultimately, successful AI research is largely driven by intuition. The best research is the kind of research that you read and say, ‘It makes sense.’ 

Yes, AI exhibits some highly counterintuitive behavior that can only be discovered through empirical approaches (such as hyperparameter tuning, which is the closest thing to alchemy we have in modern AI). 

Yet, most breakthroughs come from approaching issues from a common-sense perspective. 

- Global attention mechanisms that models leverage today make total sense to work; if the model pays attention to everything, it will not forget anything. 

- Reasoning models came from the idea that more computing power to solve a problem improves solution likelihood. 

- Distillation comes from the idea that imitation of a model is easier than imitation from data, as the teacher has done the learning heavy-lifting and, thus, students can be smaller. 

Most successful AI research is just applied common sense. 

_And today’s case is no different, as the ‘breakthrough’ was to train teachers to be good teachers; it really is that simple._ 

_No incredibly insightful discoveries or out-of-this-world prescience; it was just training models to do what they were trained for, which is to teach._ 

As a result, we now have a way to deploy powerful AIs at a significantly lower cost (and with improved performance). 

_What’s not to like about research that 1. makes sense, and 2. just works?_ 

_Technology Artificial Intelligence Programming Data Science Machine Learning_ 

**==> picture [34 x 35] intentionally omitted <==**

**==> picture [59 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
Following<br>**----- End of picture text -----**<br>


## _Written by Ignacio de Gregorio_ 

_182K followers · 25 following_ 

