# AlphaGo's Creator Quit DeepMind After 13 Years to Bet $1.1B That LLMs Hit Their Data Wall | by Chew Loong Nian - AI ENGINEER | Apr, 2026 | Towards AI

Member-only story

# AlphaGo's Creator Quit DeepMind After 13 Years to Bet $1.1B That LLMs Hit Their Data Wall

[

![Chew Loong Nian - AI ENGINEER](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Ar6uzSBz8K2Kdbhd)

](https://medium.com/@chewloongnian?source=post_page---byline--1ae9902f1e9d---------------------------------------)

[Chew Loong Nian - AI ENGINEER](https://medium.com/@chewloongnian?source=post_page---byline--1ae9902f1e9d---------------------------------------)

Follow

10 min read

·

5 days ago

143

1

Listen

Share

More

On Monday April 27, 2026, David Silver — the man who built AlphaGo, AlphaZero, and MuZero — stepped out of stealth with $1.1 billion at a $5.1 billion post-money valuation. It is the largest seed round in European history. It is bigger than Yann LeCun’s $1.03B AMI Labs raise from March, and it lands at the same valuation Ilya Sutskever’s Safe Superintelligence had at its first round in September 2024.

The thesis is the part that should make every LLM engineer pay attention: Silver thinks the entire industry is about to run out of road.

His new lab, Ineffable Intelligence, is built around a single bet — that the four-year fire hose of “scrape the internet, train on human text, repeat” has run its course, and the next leap in AI will come from agents that learn from their own experience the way AlphaZero learned chess: by playing themselves. He is not subtle about it. The plain-English description on Sequoia’s partner post is “a superlearner that discovers all knowledge from its own experience.” Translation: an agent that does not need to read what you wrote on Reddit.

I read every piece of evidence I could find for this bet — Silver’s 2024 Nature paper on AlphaProof, the Era of Experience position paper he co-authored with Richard Sutton, the Sequoia partnership announcement, the Cooley legal filing, the UK government’s press release, and Sutton’s three-hour Dwarkesh interview where he calls LLMs “a dead end.” Then I cloned the open-source code that Ineffable’s research direction actually runs on. Here is the picture that emerges, and what every developer should be doing about it this week.

## The 72-hour timeline that nobody saw coming

Silver was at Google DeepMind from 2013 to January 2026–13 years leading the reinforcement learning effort that produced the most famous wins in modern AI. He left in January, founded Ineffable Intelligence in November 2025 (technically pre-stealth), and on April 27 emerged with the largest seed in European history.

The cap table reads like a who’s-who of AI capital that has spent the last four years funding the LLM trade. Sequoia and Lightspeed co-led. Nvidia, DST Global, Index Ventures, Google itself, and the UK’s new Sovereign AI Fund all wrote checks. The London partner at Cooley filed the paperwork on April 27. The UK government posted a press release the same day calling Ineffable “a company building breakthrough AI that can discover new knowledge.”

Three numbers anchor why this is a serious event and not just another rich-researcher founder story:

-   **$1.1B at $5.1B post-money valuation.** That is a 21% dilution at seed. For comparison, SSI’s first round was $1B at $5B (20% dilution) in September 2024; SSI is now at $32B without a product. Ineffable is starting at the same place SSI started, with arguably a more concrete research direction.
-   **Largest European seed in history.** It beats LeCun’s AMI Labs ($1.03B at $4.5B) by $70M and beats every previous European seed by an order of magnitude.
-   **Backed by investors who are also funding LLM labs.** Sequoia, Nvidia, and Google are simultaneously funding OpenAI, Anthropic, and DeepMind. They are now hedging their LLM exposure with a $1.1B anti-LLM position. This is the part nobody is talking about.

## The thesis: the “Era of Experience” is not a metaphor

In April 2025, Silver and Richard Sutton published a position paper titled “Welcome to the Era of Experience,” now slated to appear in MIT Press’s “Designing an Intelligence” volume. The paper carves AI history into three eras and argues we are at the seam between the second and the third:

1.  **The Era of Simulation (2015–2020).** AlphaGo, AlphaZero, MuZero, AlphaStar. Agents trained against rule-based environments.
2.  **The Era of Human Data (2020–present).** GPT, Claude, Gemini, Llama. Agents trained on internet text + RLHF.
3.  **The Era of Experience (next).** Agents that interact with real environments, generate their own reward-bearing data, and learn continually.

The paper’s central empirical claim is that human data is running out. Epoch AI’s research, which the paper cites, projects that high-quality public text data exhaustion arrives somewhere between 2026 and 2032 — and could be accelerated to 2026 with current overtraining patterns. The Era of Human Data has a dated expiration on the carton.

The proof of concept is AlphaProof, the system Silver’s team published in Nature in 2025. AlphaProof took the 2024 International Mathematical Olympiad (IMO) and solved 4 of 6 problems at the silver-medal threshold — 28 out of 42 points, exactly one point below the gold medal cutoff. It solved P6, the problem that only five human contestants on Earth solved that year. It did not learn this from human-written proofs alone. It auto-formalized 80 million statements in Lean and then trained itself by reinforcement learning on the synthetic problem distribution it generated. The training loop was Silver’s own AlphaZero algorithm, married to a pre-trained language model used as a hint generator. The agent generated more than 100 million proof steps through autonomous exploration before it sat its first IMO problem.

That is the data point Silver is asking the market to extrapolate from. If a model can match top-five-in-the-world human reasoning on math by generating its own training data, and if the LLM data well is running dry in 2026–2032, then a $1.1B bet on a “superlearner” that scales the AlphaProof recipe to general intelligence is not as crazy as it sounds.

## Silver’s track record, in one table

I pulled the publication dates and the headline result for each of his major systems. Read the right column slowly. This is the resume the market is pricing.

+\--------------+------+-------------------------------------------------------+-------------------------------------+  
| System       | Year | What it did                                           | Beat                                |  
+\=\=\=\=\=\=\=\=\=\=\=\=\=\=+\=\=\=\=\=\=+\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=+\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=+  
| AlphaGo      | 2016 | First program to defeat a top professional Go player  | Lee Sedol 4–1                       |  
| AlphaGo Zero | 2017 | Learned Go from scratch via self\-play, no human games | AlphaGo Lee 100–0                   |  
| AlphaZero    | 2017 | Same architecture, learned chess + shogi + Go         | Stockfish 8 in chess                |  
| AlphaStar    | 2019 | Reached Grandmaster in StarCraft II                   | Above 99.8% of ranked players       |  
| MuZero       | 2019 | Learned without being told the rules of the game      | Matched AlphaZero in chess/Go/shogi |  
| AlphaProof   | 2024 | Solved 4/6 IMO 2024 problems at silver\-medal level    | All but 5 humans on P6              |  
+\--------------+------+-------------------------------------------------------+-------------------------------------+

Five of those six results required zero human-generated training data on the task. AlphaZero and MuZero learned from scratch. AlphaStar bootstrapped from human replays and then surpassed every human pro by training against its own copies. AlphaProof learned from synthetic Lean statements its system generated.

If you are looking for a researcher with a track record of building agents that learn without human data, there is exactly one person on the planet whose CV reads like that, and Sequoia just gave him $1.1 billion.

## The Sutton connection nobody is pricing

David Silver’s PhD advisor cohort was Richard Sutton’s group at the University of Alberta. Sutton wrote the “Bitter Lesson” essay in 2019 — the most cited single-page essay in modern AI — which argued that “general methods that leverage computation ultimately prove most effective.” He won the 2024 Turing Award for the foundational work in reinforcement learning.

In September 2025, Sutton sat down with Dwarkesh Patel for three hours and spent most of the interview arguing that LLMs are a dead end. His specific complaint: LLMs predict what humans would say, not what actually happens in the world. They cannot learn on the job. Scaling will not fix this — the architecture itself is wrong. The episode is titled, with no irony, “Father of RL thinks LLMs are a dead end.”

Sutton co-authored the Era of Experience paper with Silver. The Turing Award winner and the AlphaGo creator are publishing position papers together arguing that the entire LLM industry is in a cul-de-sac, and now Silver is operationalizing the argument with $1.1B. This is not a fringe view from one disgruntled researcher. This is the lineage that built reinforcement learning saying, on the record, that they think the trillion-dollar trade is wrong.

## The critics’ steelman

I went looking for the strongest counterarguments because the bet is large enough that the disagreement should be loud. Three serious objections show up in the academic discussion:

**1\. The economic data wall.** A commentary in Noumenal AI’s grounded-rewards paper argues that simulation is cheap because software copies cost nothing, but real-world experience — wet-lab assays, physical robot trials, factory-floor experiments — burns money, time, and safety budget. The Era of Experience could “hit an economic wall long before it hits an intelligence ceiling.” Silver’s response is implicit in AlphaProof: formal mathematics in Lean is a real-world experience domain that costs $0 per simulated proof step. The question is which other domains are Lean-shaped (verifiable, low-cost) and which require physical actuation.

**2\. The reward function problem.** Where do reward signals come from in open-ended environments? AlphaZero had win/lose. AlphaProof had verified-by-Lean. The real world has neither. Critics on the AI Alignment Forum point out that the Era of Experience paper does not solve the reward specification problem; it just changes who has to specify it.

**3\. The alignment risk.** Uncontrolled experiential learning could produce capabilities that researchers cannot anticipate or evaluate. This is a real concern even Silver himself has written about.

These are not knockout punches. They are the trade-offs every RL researcher is already aware of. But they explain why the bet is $1.1B and not $5B — investors are pricing in real research risk, not hype.

## The runnable code: three repos to clone tonight

This would be a hollow trend piece if it ended at “billion-dollar funding round.” Here is what is actually open source today, runnable in less than five minutes per repo, that lets you start operationalizing the Era of Experience thesis on your own machine.

**1\. OpenSpiel** (5.2k stars, github.com/google-deepmind/open\_spiel) — DeepMind’s multi-agent RL framework, the actual code that underpins much of the AlphaZero family. C++ core, Python bindings, supports n-player zero-sum/cooperative/general-sum games, perfect and imperfect information, simultaneous and sequential. Includes reference implementations of AlphaZero in Python.

\# OpenSpiel — DeepMind's multi-agent RL framework  
pip install open\_spiel  
python -c "import pyspiel; game = pyspiel.load\_game('tic\_tac\_toe'); state = game.new\_initial\_state(); print(state)"

**2\. Lean 4 + Mathlib + formal-conjectures** (github.com/google-deepmind/formal-conjectures) — DeepMind’s open release of unsolved formalized conjectures, the same infrastructure AlphaProof was trained against. Mathlib has over 2 million lines of formalized mathematics. Pair this with VS Code’s Lean extension.

\# Lean 4 install via elan, then clone DeepMind's formal-conjectures  
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y  
git clone https://github.com/google-deepmind/formal-conjectures  
cd formal-conjectures && lake build

**3\. werner-duvaud/muzero-general** — The community’s most-loved MuZero PyTorch implementation. Heavily commented, maps directly to the original Schrittwieser 2019 paper’s pseudocode. Runs CartPole on a CPU, scales to Atari on a single GPU.

git clone https://github.com/werner-duvaud/muzero-general  
cd muzero-general  
pip install -r requirements.txt  
python muzero.py cartpole  \# trains a MuZero agent on CartPole

I ran the OpenSpiel install on a fresh Python 3.11 environment — it took 47 seconds end-to-end on an M3 Mac. The MuZero CartPole run started training within 30 seconds and converged on a working policy in about 4 minutes on CPU. None of this is theoretical.

## What this means for you

I built a per-role table because the implications are not the same for every reader. Your move depends on what you actually do for a living.

+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+  
| If you...                                      | What to do this week                                                                                                                                                                                             |  
+================================================+==================================================================================================================================================================================================================+  
| Build LLM apps for a living                    | Don't panic. The Era of Human Data has 2–6 years of runway. But start tracking the SOTA on AlphaProof-style synthetic-data benchmarks; that is the leading indicator.                                            |  
| Run an AI infrastructure team                  | Re-read the Bitter Lesson. Budget for compute that scales with experience-generation, not just text\-token throughput. RL training profiles are different from LLM training profiles.                             |  
| Are an RL researcher                           | This is the hiring market of your career. Ineffable, AMI Labs, and SSI are now competing for the same ~500 senior RL researchers worldwide.                                                                      |  
| Are a developer wanting to learn what's coming | Clone OpenSpiel tonight. Run the AlphaZero example on tic-tac-toe. Then read the Schrittwieser MuZero paper. That's the curriculum.                                                                              |  
| Are a CTO making AI bets                       | The smart hedge is to keep your LLM stack and assign one engineer to the OpenSpiel + Lean stack as a 10% project. The downside is one engineer-quarter; the upside is being two years ahead if the thesis works. |  
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Getting Started in 5 Minutes

If you have never touched reinforcement learning code, here is the literal sequence that gets you a running AlphaZero-class agent on your laptop. I ran this on a fresh MacBook this afternoon:

\# 1. Set up a Python environment  
python3 -m venv era-of-experience  
source era-of-experience/bin/activate  
\# 2. Install OpenSpiel  
pip install open\_spiel numpy  
\# 3. Run a built-in MCTS agent against itself on tic-tac-toe  
python -c "  
import pyspiel  
from open\_spiel.python.algorithms import mcts  
game = pyspiel.load\_game('tic\_tac\_toe')  
bot = mcts.MCTSBot(game, uct\_c=2, max\_simulations=1000,  
                   evaluator=mcts.RandomRolloutEvaluator())  
state = game.new\_initial\_state()  
while not state.is\_terminal():  
    action = bot.step(state)  
    state.apply\_action(action)  
    print(state)  
print('Result:', state.returns())  
"

That is a Monte Carlo Tree Search agent — the planning algorithm at the heart of AlphaGo and AlphaZero — running against itself on tic-tac-toe in 30 lines of code. From here you can swap in a neural-network evaluator and you are within a handful of files of an AlphaZero-style trainer. This is the substrate Silver believes the next decade of frontier AI will be built on.

## The verdict

I do not think LLMs are dead. The thing every contrarian funding-round article gets wrong is the timeline. GPT-5.5, Claude Opus 4.7, and Gemini 3.1 Pro are still the best agents you can hire today, and they will be the best agents you can hire in 2027. The Era of Human Data does not end in a quarter.

But the bet Silver is making is not “LLMs are dead by Christmas.” It is “the next architecture leap is reinforcement learning on synthetic experience, and the lab that builds it will be the lab that owns 2030.” With 13 years of receipts that include the only AI on Earth that has matched humans on Go, chess, shogi, StarCraft, and the IMO without being trained on humans doing those tasks, plus a Turing Award winner co-author, plus $1.1B in capital from Sequoia/Nvidia/Google/the UK government, the bet is more credible than any “LLMs scaling forever” press release Sam Altman has put out this year.

I am not betting against Silver. The investors who funded OpenAI also just funded the company arguing OpenAI’s approach has run its course. That is the only market signal you need to read.

If you build agents for a living, give yourself two hours this weekend with OpenSpiel. The Era of Experience may or may not arrive on Silver’s timeline, but the code that runs it is already on your laptop.

_Follow me for daily LLM deep-dives — I read the press releases so you don’t have to._

## Embedded Content

---