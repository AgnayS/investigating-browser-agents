import { startBrowserAgent } from "magnitude-core";
import dotenv from "dotenv";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: resolve(__dirname, "../../.env") });

async function main() {
  const agent = await startBrowserAgent({
    url: "https://news.ycombinator.com",
    narrate: true,
    llm: {
      provider: "anthropic",
      options: {
        model: "claude-sonnet-4-20250514",
        apiKey: process.env.ANTHROPIC_API_KEY,
      },
    },
  });

  await agent.act("Find and tell me the title of the top post");
  await agent.stop();
}

main().catch(console.error);
