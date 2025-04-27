import React from 'react';

export default function CampaignTable({ data }) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full text-left border-collapse">
        <thead className="border-b">
          <tr className="bg-gray-100">
            {['Campaign Name','Status','Clicks','Cost','Impressions'].map(h => (
              <th key={h} className="px-4 py-2 text-sm font-medium text-gray-600">{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map(c => (
            <tr key={c.id} className="hover:bg-gray-300 border-b color-gray-200">
              <td className="px-4 py-2">{c.name}</td>
              <td className="px-4 py-2">
                <span className={`px-2 py-1 text-xs rounded-full text-white ${
                  c.status === 'Active' ? 'bg-green-500' : 'bg-gray-500'
                }`}>
                  {c.status}
                </span>
              </td>
              <td className="px-4 py-2">{c.clicks}</td>
              <td className="px-4 py-2">${Number(c.cost).toFixed(2)}</td>
              <td className="px-4 py-2">{new Intl.NumberFormat().format(c.impressions)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
