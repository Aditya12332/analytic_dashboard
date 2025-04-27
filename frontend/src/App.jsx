import { useState, useEffect } from "react";
import CampaignTable from "./components/CampaignTable";

export default function App() {
  const [campaigns, setCampaigns] = useState([]);
  const [filter, setFilter] = useState("All");

  useEffect(() => {
    fetch("http://localhost:8000/campaigns")  // FastAPI endpoint :contentReference[oaicite:2]{index=2}
      .then(r => r.json())
      .then(setCampaigns);
  }, []);

  const filtered = campaigns.filter(c => filter === "All" || c.status === filter);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <header className="mb-6 flex flex-col sm:flex-row justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-800">Campaign Analytics</h1>
        <select
          className="mt-4 sm:mt-0 px-3 py-2 border rounded"
          value={filter}
          onChange={e => setFilter(e.target.value)}
        >
          {["All","Active","Paused"].map(s => <option key={s}>{s}</option>)}
        </select>
      </header>
      <CampaignTable data={filtered} />
    </div>
  );
}
