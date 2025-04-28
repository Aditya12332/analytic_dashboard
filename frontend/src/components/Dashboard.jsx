import React, { useState, useEffect } from 'react';
import CampaignTable from './CampaignTable';
export default function Dashboard() {
  const [campaigns, setCampaigns] = useState([]);
  const [filter, setFilter] = useState('Active');

  // Fetch campaigns from backend
  useEffect(() => {
    fetch('https://analyticdashboard-production.up.railway.app/campaigns/')
      .then(res => res.json())
      .then(data => setCampaigns(data))
      .catch(console.error);
  }, []);

  const displayed = campaigns.filter(c => (filter ? c.status === filter : true));

  return (
    <div className="container mx-auto p-4 space-y-6"> 
      {/* Table card */}
      <div className="bg-white rounded-lg shadow p-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-lg font-semibold">Campaigns</h2>
          <select
            className="border rounded px-3 py-1"
            value={filter}
            onChange={e => setFilter(e.target.value)}
          >
            <option value="">All</option>
            <option value="Active">Active</option>
            <option value="Paused">Paused</option>
          </select>
        </div>
        <CampaignTable data={displayed} />
      </div>
    </div>
  );
}
