# Perplexity MCP Server - Usage Examples

This document shows how to use the Perplexity MCP Server with real-world examples.

## Table of Contents
1. [Basic Queries](#basic-queries)
2. [Advanced Reasoning](#advanced-reasoning)
3. [Research & Synthesis](#research--synthesis)
4. [Customizing Parameters](#customizing-parameters)
5. [Integration with Claude](#integration-with-claude)

---

## Basic Queries

### Simple Information Request
Get quick answers to straightforward questions with real-time web search.

**Query:**
```
Ask Perplexity: "What are the latest developments in artificial intelligence in 2025?"
```

**Model:** `sonar` (default, lightweight)

**Response:**
You'll get an answer with the latest AI developments and citations to source websites.

---

### Current Events
Stay up-to-date with real-time information.

**Query:**
```
Ask Perplexity with sonar model: "What happened in tech news today?"
```

**Result:** Real-time search results with citations showing the sources.

---

## Advanced Reasoning

### Step-by-Step Problem Solving
Use reasoning models for complex analysis and multi-step explanations.

**Query:**
```
Ask Perplexity with sonar-reasoning model: "Explain how neural networks learn. Break it down step-by-step."
```

**Parameters:**
- Model: `sonar-reasoning`
- temperature: `0.7` (default - balanced creativity)
- max_tokens: `2000`

**What you get:** Detailed step-by-step reasoning with the AI showing its thought process.

---

### Deep Technical Analysis
For complex technical topics requiring advanced reasoning.

**Query:**
```
Ask Perplexity with sonar-reasoning-pro model: "How do transformers work in machine learning? Include mathematical concepts."
```

**Parameters:**
- Model: `sonar-reasoning-pro` (DeepSeek-R1 powered)
- temperature: `0.5` (more focused, less creative)
- max_tokens: `3000`

**Result:** Advanced multi-step reasoning with deep technical insights.

---

## Research & Synthesis

### Long-Form Research Report
Generate comprehensive research documents on complex topics.

**Query:**
```
Ask Perplexity with sonar-deep-research model: "Write a comprehensive report on the current state of renewable energy technologies in 2025."
```

**Parameters:**
- Model: `sonar-deep-research`
- max_tokens: `5000`

**Result:** A detailed research synthesis with multiple perspectives and citations.

---

### Comparative Analysis
Compare multiple options or approaches systematically.

**Query:**
```
Ask Perplexity with sonar-pro model: "Compare Python vs JavaScript for building web servers. Include pros and cons."
```

**Parameters:**
- Model: `sonar-pro` (Enhanced search with richer context)
- max_tokens: `2000`

**Result:** Comprehensive comparison with current best practices.

---

## Customizing Parameters

### Temperature Control (Creativity vs Focus)

**For Creative Outputs (temperature: 1.5)**
```
Ask Perplexity: "Generate creative ideas for a sci-fi story set in 2100"
temperature: 1.5
model: sonar
```
Higher temperature = more creative and varied responses.

**For Focused, Accurate Answers (temperature: 0.3)**
```
Ask Perplexity: "What is the exact definition of quantum entanglement?"
temperature: 0.3
model: sonar
```
Lower temperature = more focused and consistent responses.

---

### System Message for Context
Provide custom instructions to guide the AI's responses.

**Query:**
```
Ask Perplexity with system message: "You are a Python expert. Answer all questions from a Python developer's perspective."
question: "What are the best practices for building APIs?"
model: sonar-pro
```

**Result:** Answers tailored to Python-specific best practices.

---

### Max Tokens Control
Adjust response length based on your needs.

**Quick Answer (max_tokens: 500)**
```
Ask Perplexity: "What is machine learning?"
max_tokens: 500
model: sonar
```

**Detailed Explanation (max_tokens: 3000)**
```
Ask Perplexity: "Explain machine learning with examples"
max_tokens: 3000
model: sonar-pro
```

---

## Integration with Claude

### Using Perplexity as a Research Tool
When you need to research current information while working on a task.

**Scenario:** You're writing about recent AI trends
```
Me: "Help me write about the latest AI developments"

Claude uses Perplexity to:
1. Ask: "What are the major AI breakthroughs in 2025?"
2. Get current information with citations
3. Incorporate findings into your writing
```

---

### Fact-Checking and Verification
Verify claims or get the latest information.

**Scenario:** Verifying a technical claim
```
Me: "Is Python still the most popular language for AI?"

Claude uses Perplexity:
1. Ask: "What is the most popular programming language for AI development in 2025?"
2. Get current data and statistics
3. Verify or correct assumptions
```

---

### Real-Time Market Research
Get current information for business decisions.

**Scenario:** Researching market trends
```
Ask Perplexity with sonar-deep-research: "What are the emerging trends in the SaaS market in 2025?"
```

**Result:** Current market analysis with sources you can cite.

---

## Model Selection Guide

| Task | Recommended Model | Why |
|------|-------------------|-----|
| Quick facts | `sonar` | Fast, lightweight, sufficient for basic queries |
| Detailed research | `sonar-pro` | Richer context, better for complex topics |
| Step-by-step explanation | `sonar-reasoning` | Shows reasoning process |
| Advanced analysis | `sonar-reasoning-pro` | DeepSeek-R1 powered, best for complex problems |
| Long-form synthesis | `sonar-deep-research` | Designed for comprehensive reports |

---

## Tips for Best Results

### 1. Be Specific
**Poor:** "Tell me about AI"
**Better:** "What are the latest breakthroughs in large language models as of 2025?"

### 2. Use System Messages for Context
```
system_message: "You are a cybersecurity expert"
question: "What are the latest security threats?"
```

### 3. Choose the Right Model
- **Simple queries** → `sonar`
- **Context-rich topics** → `sonar-pro`
- **Reasoning-heavy** → `sonar-reasoning-pro`
- **Report writing** → `sonar-deep-research`

### 4. Control Temperature Based on Use Case
- **Factual information**: temperature 0.3-0.5
- **Creative tasks**: temperature 1.5-2.0
- **Balanced**: temperature 0.7 (default)

### 5. Citations Matter
Always check the sources provided - they're real URLs you can verify!

---

## Common Workflows

### Research Paper Writing
```
1. Ask: "What are the latest findings on topic X?" (sonar-pro)
2. Get overview with citations
3. Ask: "Deep dive into aspect Y" (sonar-reasoning-pro)
4. Ask: "Write a summary suitable for a research paper" (sonar-deep-research)
```

### Coding Help with Current Libraries
```
1. Ask: "What's the latest version of [library] and its key features?" (sonar)
2. Ask: "How do I implement [feature] in [library]?" (sonar-pro)
3. Get real-time documentation and examples
```

### Learning New Topics
```
1. Ask: "Explain [topic] for beginners" (sonar-pro)
2. Ask: "What are the key concepts?" (sonar-reasoning)
3. Ask: "Show me practical examples" (sonar-pro)
```

---

## Troubleshooting

### "No response" or "Empty response"
- Your query might be too vague
- Try being more specific and detailed

### "HTTP 401" error
- Your API key is invalid or expired
- Check your PERPLEXITY_API_KEY in `.env`

### Getting outdated information
- Some models (like `sonar`) search the web for current info
- If you need the latest data, use `sonar` or `sonar-pro`

---

## Next Steps

- Check the [README.md](README.md) for installation
- Review the [available models](#model-selection-guide) above
- Start with simple queries and experiment with different parameters
- Build your own workflows!

Happy researching! 🚀
